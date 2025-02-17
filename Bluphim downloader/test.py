import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://fptplay.vn/'
}

#lấy video đầu tiên
first_video_url = 'https://vod02-cdn.fptplay.net/POVOD/encoded/2024/10/31/pokemonultimatejourneystheseries-2021-jp-001-1730316012/H264/video/avc1/4/init.m4s'
response_first_video = requests.get(first_video_url, headers=headers)
with open(f"D:/LT/LT From Laptop/Download Vid/output_fpt/video/init.m4s", "wb") as f:
    f.write(response_first_video.content)