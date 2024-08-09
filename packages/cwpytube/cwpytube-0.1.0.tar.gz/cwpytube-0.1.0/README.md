### Library Overview

The library, `cwPytube`, provides functionality to download YouTube videos, convert them to different formats, list video files in a directory, and watch video files. It leverages the `pytube` library for downloading YouTube videos and the `moviepy` library for video conversion.

### Installation

To install the library, you can use the following command:

```bash
pip install cwPytube
```

### Usage

Here's how you can use the various functions provided by your library:

1. **Download a YouTube Video**

```python
from cwpytube import download_youtube_video

# Download a YouTube video
video_path = download_youtube_video('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
print(f"Video downloaded to: {video_path}")
```

2. **Convert the Downloaded Video to a Different Format**

```python
from cwpytube import convert_video

# Convert the downloaded video to a different format
converted_path = convert_video('video.mp4', 'output_video.avi', 'libx264')
print(f"Video converted to: {converted_path}")
```

3. **List All Video Files in the Current Directory**

```python
from cwpytube import list_videos

# List all video files in the current directory
videos = list_videos()
print("Videos in the current directory:", videos)
```

4. **Watch a Video File**

```python
from cwpytube import watch_video

# Watch a video file
watch_video('video.mp4')
```

### Unit Tests

Your unit tests cover the following functionalities:

1. **Downloading a YouTube Video**

```python
def test_download_youtube_video(self):
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # Example URL
    output_path = 'test_video.mp4'
    result = download_youtube_video(url, output_path)
    self.assertTrue(os.path.exists(result))
    os.remove(output_path)
```

2. **Converting a Video**

```python
def test_convert_video(self):
    input_path = 'test_video.mp4'
    output_path = 'test_video.avi'
    download_youtube_video('https://www.youtube.com/watch?v=dQw4w9WgXcQ', input_path)
    result = convert_video(input_path, output_path, 'libx264')
    self.assertTrue(os.path.exists(result))
    os.remove(input_path)
    os.remove(output_path)
```

3. **Listing Video Files**

```python
def test_list_videos(self):
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # Example URL
    output_path = 'test_video.mp4'
    download_youtube_video(url, output_path)
    videos = list_videos('.')
    self.assertIn(output_path, videos)
    os.remove(output_path)
```

4. **Watching a Video**

```python
def test_watch_video(self):
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'  # Example URL
    output_path = 'test_video.mp4'
    download_youtube_video(url, output_path)
    try:
        watch_video(output_path)
    except Exception as e:
        self.fail(f"watch_video raised an exception: {e}")
    os.remove(output_path)
```

### Project Structure

Here's the updated project structure:

```
cwPytube/
│
├── cwpytube/
│   ├── __init__.py
│   └── module1.py
│    
│
├── tests/
│   ├── __init__.py
│   └──test_module1.py
│    
│
├── setup.py
├── README.md
└── requirements.txt
```
## Usage

```python
from cwpytube import download_youtube_video, convert_video, list_videos, watch_video

# Download a YouTube video
video_path = download_youtube_video('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
print(f"Video downloaded to: {video_path}")

# Convert the downloaded video to a different format
converted_path = convert_video(video_path, 'output_video.avi', 'libx264')
print(f"Video converted to: {converted_path}")

# List all video files in the current directory
videos = list_videos()
print("Videos in the current directory:", videos)

# Watch a video file
watch_video(video_path)
```
```
