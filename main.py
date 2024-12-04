import requests

def download_one_video(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Referer': 'https://cdn.linkneverdie.com/'
    }

    try:
        response = requests.get(url, headers=headers)

        with open('D:/Phim (Part D)/Kẻ Kiến Tạo(1)/{}.mp4'.format(urls.index(url)), "wb") as f:
            f.write(response.content)
    except :
        download_one_video(url)

with open("url.txt", "r") as f:
    urls = f.read()
    urls = urls.split("\n")

for url in urls:
    download_one_video(url)

with open("videos_list.txt", "w", encoding='utf-8') as f:
    for i in range(0, len(urls)+1):
        str = "file ", f"\'{i}.mp4\'\n"
        f.write(str[0] + str[1])