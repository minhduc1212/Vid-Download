import subprocess

# Paths to the input video and audio files
video_file = "video.mp4"
audio_file = "audio.mp4"
output_file = "output.mp4"

# Command to merge video and audio using ffmpeg 
# use this case when you want to merge quickly and don't care about the output capacity
command = [
    "ffmpeg",
    "-i", video_file,
    "-i", audio_file,
    "-c", "copy",
    "-map", "0:v",
    "-map", "1:a",
    output_file
]

# Run the command
subprocess.run(command, check=True)


# use this case when you want to merge slowly but small capacity

#this command will re-encode the video to a new file
command_1 = [
    "ffmpeg",
    '-i', video_file,
    output_file
]

command = [
    "ffmpeg",
    "-i", video_file,
    "-i", audio_file,
    "-c", "copy",
    "-map", "0:v",
    "-map", "1:a",
    output_file
]