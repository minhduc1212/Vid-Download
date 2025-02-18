#Download and convert directly to 2 files mp4 audio and video
import requests

audio_url_temp = 'https://vod02-cdn.fptplay.net/POVOD/encoded/2024/10/31/pokemonultimatejourneystheseries-2021-jp-001-1730316012/H264/audio/und/mp4a.40.2/seg-{a}.m4s'
video_url_temp = 'https://vod02-cdn.fptplay.net/POVOD/encoded/2024/10/31/pokemonultimatejourneystheseries-2021-jp-001-1730316012/H264/video/avc1/4/seg-{b}.m4s'


audio_segments = []
video_segments = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://fptplay.vn/'
}

# Lấy audio đầu tiên
first_audio_url = 'https://vod02-cdn.fptplay.net/POVOD/encoded/2024/10/31/pokemonultimatejourneystheseries-2021-jp-001-1730316012/H264/audio/und/mp4a.40.2/init.mp4'
response_first_audio = requests.get(first_audio_url, headers=headers)
audio_segments.append(response_first_audio.content)

# Lấy video đầu tiên
first_video_url = 'https://vod02-cdn.fptplay.net/POVOD/encoded/2024/10/31/pokemonultimatejourneystheseries-2021-jp-001-1730316012/H264/video/avc1/4/init.mp4'
response_first_video = requests.get(first_video_url, headers=headers)
video_segments.append(response_first_video.content)

# Lấy các segment audio và video tiếp theo
for i in range(1, 355):
    # Lấy audio tiếp theo
    audio_url = audio_url_temp.format(a=i)
    response_audio = requests.get(audio_url, headers=headers)
    audio_segments.append(response_audio.content)
    
    # Lấy video tiếp theo
    video_url = video_url_temp.format(b=i)
    response_video = requests.get(video_url, headers=headers)
    video_segments.append(response_video.content)

    print(f"Downloaded segment {i}")

# Ghi các segment audio vào file
with open("audio.mp4", "wb") as f:
    for segment in audio_segments:
        f.write(segment)

# Ghi các segment video vào file
with open("video.mp4", "wb") as f:
    for segment in video_segments:
        f.write(segment)