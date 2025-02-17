import requests

audio_url_temp = 'https://vod02-cdn.fptplay.net/POVOD/encoded/2024/10/31/pokemonultimatejourneystheseries-2021-jp-001-1730316012/H264/audio/und/mp4a.40.2/seg-{a}.m4s'
video_url_temp = 'https://vod02-cdn.fptplay.net/POVOD/encoded/2024/10/31/pokemonultimatejourneystheseries-2021-jp-001-1730316012/H264/video/avc1/4/seg-{b}.m4s'

mpd_url = 'https://vod02-cdn.fptplay.net/POVOD/encoded/2024/10/31/pokemonultimatejourneystheseries-2021-jp-001-1730316012/H264/stream.mpd'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://fptplay.vn/'
}

#lấy file .mpd
response_mpd = requests.get(mpd_url, headers=headers)
    
with open("output_fpt/stream.mpd", "wb") as f:
    f.write(response_mpd.content)

#lấy audio đầu tiên 
    first_audio_url = 'https://vod02-cdn.fptplay.net/POVOD/encoded/2024/10/31/pokemonultimatejourneystheseries-2021-jp-001-1730316012/H264/audio/und/mp4a.40.2/init.mp4'
    response_first_audio = requests.get(first_audio_url, headers=headers)
    with open(f"output_fpt/audio/und/mp4a.40.2/init.mp4", "wb") as f:
        f.write(response_first_audio.content)

#lấy video đầu tiên
    first_video_url = 'https://vod02-cdn.fptplay.net/POVOD/encoded/2024/10/31/pokemonultimatejourneystheseries-2021-jp-001-1730316012/H264/video/avc1/4/init.mp4'
    response_first_video = requests.get(first_video_url, headers=headers)
    with open(f"output_fpt/video/avc1/4/init.mp4", "wb") as f:
        f.write(response_first_video.content)

#lấy audio
for i in range(1, 355):
    
    #lấy audio tiếp theo
    audio_url = audio_url_temp.format(a=i)
    response_audio = requests.get(audio_url, headers=headers)
    with open(f"output_fpt/audio/und/mp4a.40.2/seg-{i}.m4s", "wb") as f:
        f.write(response_audio.content)
    
    #lấy video tiếp theo
    video_url = video_url_temp.format(b=i)
    response_video = requests.get(video_url, headers=headers)
    with open(f"output_fpt/video/avc1/4/seg-{i}.m4s", "wb") as f:
        f.write(response_video.content)

    print(f"Downloaded segment {i}")
    