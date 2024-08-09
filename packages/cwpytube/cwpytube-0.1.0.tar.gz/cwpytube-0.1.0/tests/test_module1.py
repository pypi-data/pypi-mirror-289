import unittest
import os
from cwpytube.module1 import download_youtube_video, convert_video, list_videos, watch_video

class TestModule1(unittest.TestCase):
    def test_download_youtube_video(self):
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # Example URL
        output_path = 'test_video.mp4'
        result = download_youtube_video(url, output_path)
        self.assertTrue(os.path.exists(result))
        os.remove(output_path)

    def test_convert_video(self):
        input_path = 'test_video.mp4'
        output_path = 'test_video.avi'
        download_youtube_video('https://www.youtube.com/watch?v=dQw4w9WgXcQ', input_path)
        result = convert_video(input_path, output_path, 'libx264')
        self.assertTrue(os.path.exists(result))
        os.remove(input_path)
        os.remove(output_path)

    def test_list_videos(self):
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # Example URL
        output_path = 'test_video.mp4'
        download_youtube_video(url, output_path)
        videos = list_videos('.')
        self.assertIn(output_path, videos)
        os.remove(output_path)

    def test_watch_video(self):
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # Example URL
        output_path = 'test_video.mp4'
        download_youtube_video(url, output_path)
        try:
            watch_video(output_path)
        except Exception as e:
            self.fail(f"watch_video raised an exception: {e}")
        os.remove(output_path)

if __name__ == '__main__':
    unittest.main()
