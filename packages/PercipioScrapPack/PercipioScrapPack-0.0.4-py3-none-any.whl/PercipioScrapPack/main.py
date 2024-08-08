# my_package/main.py

import json
import time
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
import html2text
import markdown2
import pdfkit
from urllib.parse import urljoin

def parse_args():
    parser = argparse.ArgumentParser(description='Dynamic URL loading script.')
    parser.add_argument('url', type=str, help='URL of the page to load')
    return parser.parse_args()

def inject_capture_script(driver):
    # Włączenie logowania żądań i odpowiedzi dla XMLHttpRequest
    driver.execute_script("""
        window.performance_log = window.performance_log || [];
        const originalOpen = XMLHttpRequest.prototype.open;
        XMLHttpRequest.prototype.open = function(method, url) {
            this.addEventListener('load', function() {
                if (url.endsWith('.xhtml')) {
                    window.performance_log.push({
                        url: url,
                        status: this.status,
                        response: this.responseText
                    });
                }
            }, false);
            originalOpen.apply(this, arguments);
        };
    """)
    print("Capture script injected.")

def html_to_markdown(html_content, base_url):
    # Użycie BeautifulSoup do parsowania HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Konwersja znaczników <img> na pełne URL i zamiana na Markdown
    for img in soup.find_all('img'):
        src = img.get('src')
        alt = img.get('alt', '')
        if src:
            full_img_url = urljoin(base_url, src)
            markdown_img = f"![{alt}]({full_img_url})"
            img.replace_with(markdown_img)

    # Konwersja zmodyfikowanego HTML na Markdown za pomocą html2text
    modified_html_content = str(soup)
    markdown_content = html2text.html2text(modified_html_content)

    return markdown_content

def capture_xhtml_files(driver, results):
    # Zmniejszenie czasu oczekiwania na załadowanie zasobów
    time.sleep(1)

    # Pobieranie zarejestrowanych odpowiedzi
    performance_log = driver.execute_script("return window.performance_log")
    new_entries = 0
    for entry in performance_log:
        if not any(result['url'] == entry['url'] for result in results):
            # Konwersja XHTML na Markdown
            base_url = entry['url']
            markdown_content = html_to_markdown(entry['response'], base_url)
            results.append({
                'url': entry['url'],
                'status': entry['status'],
                'response': markdown_content
            })
            new_entries += 1
    print(f"Captured {new_entries} new .xhtml files.")

def click_next_and_capture(driver, results):
    while True:
        try:
            # Czekanie na przycisk "Next section" i kliknięcie go
            next_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Next Section')]"))
            )
            next_button.click()
            print("Clicked 'Next Section' button.")
            
            # Zmniejszenie czasu oczekiwania na załadowanie następnej strony
            time.sleep(1)

            # Wstrzyknięcie skryptu przechwytywania na nowej stronie
            inject_capture_script(driver)

            # Przechwytywanie plików .xhtml na następnej stronie
            capture_xhtml_files(driver, results)

        except Exception as e:
            print("No more pages or an error occurred:", str(e))
            break

def main():
    args = parse_args()
    url = args.url

    # Ustawienia dla Selenium
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    options.add_argument('--headless')  # Uruchomienie w trybie bezgłowym
    options.add_argument('--disable-gpu')  # Wyłączenie GPU
    options.add_argument('--no-sandbox')  # Wyłączenie piaskownicy
    options.add_argument('--disable-dev-shm-usage')  # Wyłączenie współdzielenia pamięci

    # Inicjalizacja przeglądarki
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Otwórz stronę
    driver.get(url)

    # Zaczekaj, aż strona się załaduje
    driver.implicitly_wait(3)

    # Włączenie Network
    driver.execute_cdp_cmd('Network.enable', {})

    # Lista do przechowywania wyników
    results = []

    # Wstrzyknięcie skryptu przechwytywania na pierwszej stronie
    inject_capture_script(driver)

    # Przechwytywanie plików .xhtml na pierwszej stronie
    capture_xhtml_files(driver, results)

    # Użycie wielowątkowości do równoległego przetwarzania stron
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(click_next_and_capture, driver, results) for _ in range(4)]
        for future in futures:
            future.result()

    # Zamknięcie przeglądarki
    driver.quit()

    # Wyświetlanie wyników
    print(f"Total captured .xhtml files: {len(results)}")
    for result in results:
        print(f"URL: {result['url']}")
        print(f"Status: {result['status']}")
        print(f"Content:\n{result['response'][:200]}")  # Wyświetlanie pierwszych 200 znaków zawartości

    # Zapisywanie wyników do jednego pliku Markdown
    markdown_filename = 'results.md'
    with open(markdown_filename, 'w', encoding='utf-8') as f:
        for result in results:
            f.write(result['response'])
            f.write("\n\n")  # Dodanie odstępu między wpisami

    # Konwersja Markdown na HTML
    with open(markdown_filename, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    html_content = markdown2.markdown(markdown_content)

    # Dodanie metatagu UTF-8 do pliku HTML
    html_content = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
    {html_content}
    </body>
    </html>"""

    # Zapisywanie HTML do pliku tymczasowego
    html_filename = 'results.html'
    with open(html_filename, 'w', encoding='utf-8') as f:
        f.write(html_content)

    # Konfiguracja ścieżki do wkhtmltopdf
    pdfkit_config = pdfkit.configuration(wkhtmltopdf='C://Program Files//wkhtmltopdf//bin//wkhtmltopdf.exe')

    # Konwersja HTML na PDF
    pdf_filename = 'results.pdf'
    pdfkit.from_file(html_filename, pdf_filename, configuration=pdfkit_config)

    print(f"PDF saved as {pdf_filename}")

if __name__ == '__main__':
    main()
