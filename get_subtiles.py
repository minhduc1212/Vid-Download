import cloudscraper
import requests
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()
headers =   {
                'Referer': 'https://cdn2.bluesky987cc.site/'
            }
url = 'https://cdn.bluesky987cc.site/subtitle/1efdf0c73b564f1895c506736086aca6?web=BluPhim.Net&token2=8fb24e8'
response = requests.get(url, headers=headers)
print(response.status_code)
# Save it to a 3mu8 file
with open("test_sub.srt", "wb") as f:
    f.write(response.content)
