import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://www.olacabs.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print("Unique Titles and Links:\n")

seen_links = set()

for tag in soup.find_all("a"):
    title = tag.text.strip()
    link = tag.get("href")

    if not title or not link:
        continue

    if link.startswith("#") or link.startswith("javascript"):
        continue

    full_link = urljoin(url, link)

    if full_link not in seen_links:
        seen_links.add(full_link)
        print("Title:", title)
        print("Link:", full_link)
        print("-" * 40)

