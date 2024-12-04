import requests
from requests.exceptions import ChunkedEncodingError

def download_one_video(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Referer': 'https://cdn.linkneverdie.com/'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        with open('1.mp4', "wb") as f:
            f.write(response.content)
    except ChunkedEncodingError:
        # Retry the request in case of ChunkedEncodingError
        download_one_video(url)

url='https://cdn2.xyncdn.tech/s1/segment/4ac0d1b2660b4e39a7dcd35b30551ed9/v_0.jpg'
download_one_video(url)