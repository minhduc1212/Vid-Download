import subprocess
import os

def merge_m4s_with_ffmpeg(audio_path, video_path, output_path):
    """
    Gộp các file .m4s video và audio lại thành một file video hoàn chỉnh bằng ffmpeg.

    Args:
        audio_path: Đường dẫn đến thư mục chứa các file audio .m4s.
        video_path: Đường dẫn đến thư mục chứa các file video .m4s.
        output_path: Đường dẫn và tên file output (ví dụ: "output.mp4").
    """

    try:
        # Lấy danh sách các file video và audio, sắp xếp theo thứ tự
        video_files = sorted([f for f in os.listdir(video_path) if f.startswith("video_") and f.endswith(".m4s")], key=lambda x: int(x.split("_")[1].split(".")[0]))
        audio_files = sorted([f for f in os.listdir(audio_path) if f.startswith("audio_") and f.endswith(".m4s")], key=lambda x: int(x.split("_")[1].split(".")[0]))

        # Tạo đường dẫn đầy đủ đến các file
        video_paths = [os.path.join(video_path, f) for f in video_files]
        audio_paths = [os.path.join(audio_path, f) for f in audio_files]

        # Tạo file tạm để chứa danh sách các file video
        with open("video_files.txt", "w") as f:
            for video_file in video_paths:
                f.write(f"file '{video_file}'\n")

        # Tạo file tạm để chứa danh sách các file audio
        with open("audio_files.txt", "w") as f:
            for audio_file in audio_paths:
                f.write(f"file '{audio_file}'\n")

        # Tạo chuỗi lệnh cho ffmpeg
        command = [
            "ffmpeg",
            "-f", "concat",
            "-safe", "0",
            "-i", "video_files.txt",
            "-f", "concat",
            "-safe", "0",
            "-i", "audio_files.txt",
            "-c:v", "libx264",
            "-c:a", "aac",
            output_path
        ]

        # Chạy lệnh ffmpeg bằng subprocess và capture output
        result = subprocess.run(command, capture_output=True, text=True)

        # Kiểm tra kết quả và in thông tin lỗi nếu có
        if result.returncode != 0:
            print(f"Lỗi khi chạy ffmpeg: {result.stderr}")
        else:
            print(f"Video đã được tạo thành công tại: {output_path}")

        # Xóa các file tạm
        os.remove("video_files.txt")
        os.remove("audio_files.txt")

    except subprocess.CalledProcessError as e:
        print(f"Lỗi khi chạy ffmpeg: {e}")
    except FileNotFoundError:
        print("Lỗi: ffmpeg không được tìm thấy. Vui lòng cài đặt ffmpeg và đảm bảo nó có trong PATH.")
    except Exception as e:  # Catch các lỗi khác
        print(f"Có lỗi xảy ra: {e}")

# Sử dụng hàm
audio_path = "D:/LT/LT From Laptop/Download Vid/output_fpt/audio"  
video_path = "D:/LT/LT From Laptop/Download Vid/output_fpt/video"  
output_path = "output.mp4"
merge_m4s_with_ffmpeg(audio_path, video_path, output_path)