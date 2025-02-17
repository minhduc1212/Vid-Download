import cloudscraper
import requests
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()
headers =   {
                'Referer': 'https://cdn2.bluesky987cc.site'
            }
url = 'https://cdn.bluesky987cc.site/segment/38c49b04cd38492fb21a7cc6ed41b9e2/?token1=cd9c436&token3=4d24aad'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
# Save it to a 3mu8 file
with open("NHỮNG KỶ NGUYÊN CỦA TAYLOR SWIFT.3mu8", "wb") as f:
    f.write(response.content)
