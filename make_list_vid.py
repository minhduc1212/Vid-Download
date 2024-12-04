
with open("videos.txt", "w", encoding='utf-8') as f:
    for i in range(1, 2321):
        str = "file ", f"\'D:/Phim (Part D)/Kẻ Kiến Tạo/{i}.mp4\'\n"
        f.write(str[0] + str[1])
