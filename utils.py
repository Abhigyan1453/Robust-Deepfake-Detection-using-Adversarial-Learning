import cv2

def extract_frames(video_path, num_frames=10):
    vidcap = cv2.VideoCapture(video_path)
    frames = []
    total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    step = max(1, total_frames // num_frames)

    for i in range(num_frames):
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, i * step)
        success, image = vidcap.read()
        if success:
            frames.append(image)
    vidcap.release()
    return frames
