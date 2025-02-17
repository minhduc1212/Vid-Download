import requests
from requests.exceptions import ChunkedEncodingError

def download_one_video(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Referer': 'https://cdn3.kingpower123iii.online/streaming?id=4a1b920e888f4c9faaca9c10bc7d0092&subId=&web=bluphim2.com&token1=90b8d69&token2=896c022&token3=43420f2&cdn=https://cdn3.kingpower123iii.online&lang=vi'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        with open('2.mp4', "wb") as f:
            f.write(response.content)
    except ChunkedEncodingError:
        # Retry the request in case of ChunkedEncodingError
        download_one_video(url)

url='https://cdn3.kingpower123iii.online/s7/segment/4a1b920e888f4c9faaca9c10bc7d0092/v_0.jpg'
download_one_video(url)