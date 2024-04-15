import requests
from bs4 import BeautifulSoup
import re
import os
import sys
from urllib.parse import urljoin

def extract_js_links(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            js_links = []
            for script in soup.find_all('script', src=True):
                src = script['src']
                if src.endswith('.js'):
                    js_links.append(src)
            return js_links
        else:
            print("Failed to fetch the website. Status code:", response.status_code)
            return []
    except Exception as e:
        print("An error occurred:", str(e))
        return []

def save_js_files(js_links, output_dir):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for link in js_links:
            filename = link.split('/')[-1]
            url = urljoin(website_url, link)
            with open(os.path.join(output_dir, filename), 'wb') as f:
                response = requests.get(url)
                f.write(response.content)
            print(f"Saved {filename} successfully.")

    except Exception as e:
        print("An error occurred while saving the JS files:", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <website_url>")
        sys.exit(1)

    website_url = sys.argv[1]
    js_links = extract_js_links(website_url)
    if js_links:
        output_dir = "js_files"
        save_js_files(js_links, output_dir)
    else:
        print("No JavaScript files found on the website.")
