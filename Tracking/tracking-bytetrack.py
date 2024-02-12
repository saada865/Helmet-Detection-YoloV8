import cv2
from ultralytics import YOLO
import time

model = YOLO('/Users/saadahmadmalik/Downloads/best-50epochs.pt')

video_path = "/Users/saadahmadmalik/Downloads/pexels_videos_2795750 (360p).mp4"

cap = cv2.VideoCapture(video_path)

prev_frame_time = 0
new_frame_time = 0

# Saving Video
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

size = (frame_width, frame_height)

result = cv2.VideoWriter('/Users/saadahmadmalik/Documents/Coding/WORK/helmet-detection-pro/Saved-Videos/filename.avi',
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)


while cap.isOpened():

    success, frame = cap.read()

    if success:

        font = cv2.FONT_HERSHEY_SIMPLEX
        new_frame_time = time.time()

        fps = 1 / (new_frame_time - prev_frame_time)
        prev_frame_time = new_frame_time

        results = model.track(frame, persist=True, tracker="bytetrack.yaml")

        annotated_frame = results[0].plot()

        fps = int(fps)
        fps = str(fps)

        cv2.putText(annotated_frame, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)


        result.write(annotated_frame)
        cv2.imshow("YOLOv8 Tracking", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
result.release()

