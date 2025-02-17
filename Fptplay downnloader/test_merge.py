import subprocess

# Paths to the input video and audio files
video_file = "video.mp4"
audio_file = "audio.mp4"
output_file = "output.mp4"

# Command to merge video and audio using ffmpeg
command = [
    "ffmpeg",
    "-i", video_file,
    "-i", audio_file,
    "-c:v", "copy",
    "-c:a", "aac",
    "-strict", "experimental",
    output_file
]

# Run the command
subprocess.run(command, check=True)