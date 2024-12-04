import os
import subprocess
from multiprocessing import Pool

def concatenate_mp4_files(input_files, output_file):
    # Xây dựng lệnh ffmpeg để ghép các file MP4
    cmd = ['ffmpeg', '-i', 'concat:' + '|'.join(input_files), '-c', 'copy', output_file]

    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    # Đường dẫn của các file MP4 cần ghép
    input_files = os.listdir("D:/Phim (Part D)/Kẻ Kiến Tạo")

    # Tên file đầu ra sau khi ghép
    output_file = 'D:/Phim (Part D)/Kẻ Kiến Tạo/output.mp4'

    # Số lượng process để sử dụng
    num_processes = os.cpu_count()

    # Chia danh sách các file thành các nhóm nhỏ để xử lý song song
    file_groups = [input_files[i:i+10] for i in range(0, len(input_files), 10)]

    # Tạo một Pool với số lượng process tương ứng
    pool = Pool(processes=num_processes)

    # Sử dụng Pool để gọi hàm concatenate_mp4_files cho từng nhóm file
    pool.starmap(concatenate_mp4_files, [(files, output_file) for files in file_groups])

    # Đợi cho tất cả các process hoàn thành
    pool.close()
    pool.join()