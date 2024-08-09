import os
import subprocess
from pytube import YouTube
from moviepy.editor import VideoFileClip

def download_youtube_video(url, output_path='video.mp4'):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    stream.download(filename=output_path)
    return output_path

def convert_video(input_path, output_path, output_format):
    clip = VideoFileClip(input_path)
    clip.write_videofile(output_path, codec=output_format)
    return output_path

def list_videos(directory='.'):
    return [f for f in os.listdir(directory) if f.endswith(('.mp4', '.avi', '.mkv', '.mov'))]

def watch_video(file_path):
    if os.name == 'nt':  # For Windows
        os.startfile(file_path)
    elif os.name == 'posix':  # For macOS and Linux
        subprocess.call(('open', file_path) if sys.platform == 'darwin' else ('xdg-open', file_path))