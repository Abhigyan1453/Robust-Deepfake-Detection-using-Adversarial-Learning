from flask import Flask, render_template, request
import os
import urllib.request
import yt_dlp # type: ignore
from detect import process_video

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    video_file = request.files.get('video')
    allowed_video_exts = ['.mp4', '.avi', '.mov', '.mkv', '.wmv']
    if video_file and not any(video_file.filename.lower().endswith(ext) for ext in allowed_video_exts):
        return "❌ Invalid file type. Please upload a valid video file."
    video_url = request.form.get('video_url')
    if video_url.endswith(('.jpg', '.png', '.jpeg', '.webp')):
        return "❌ Image links are not supported, please use video links only."
    filename = ""

    if video_file and video_file.filename != "":
        filename = os.path.join(UPLOAD_FOLDER, video_file.filename)
        video_file.save(filename)

    elif video_url:
        try:
            filename = os.path.join(UPLOAD_FOLDER, 'downloaded_video.mp4')

            # Check if it's a YouTube link
            if 'youtube.com' in video_url or 'youtu.be' in video_url:
                ydl_opts = {
                    'outtmpl': filename,
                    'format': 'best[ext=mp4]/best',
                    'quiet': True
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])
            else:
                # Direct video URL (e.g., .mp4)
                urllib.request.urlretrieve(video_url, filename)

        except Exception as e:
            return f"<h3>❌ Failed to download video: {str(e)}</h3>"

    else:
        return "<h3>⚠️ Please upload a file or enter a valid URL.</h3>"

    # Run detection
    result = process_video(filename)
    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
