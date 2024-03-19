import cv2
import os

def decode_video(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video file")
        return

   
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

       
        frame_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)

        frame_count += 1
    cap.release()

    print(f"Frames saved: {frame_count}")

if __name__ == "__main__":
    video_path = "input_video.mp4"

    output_folder = "frames"

    decode_video(video_path, output_folder)
