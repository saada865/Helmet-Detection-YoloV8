import cv2
from ultralytics import YOLO
# !pip3 install lap
import time

# Load the YOLOv8 model
model = YOLO('/Users/saadahmadmalik/Downloads/best-50epochs.pt')

# Open the video file

video_path = "/Users/saadahmadmalik/Downloads/pexels-pavel-danilyuk-7817205 (1080p).mp4"

#pexels-pavel-danilyuk-7817205 (1080p).mp4
#pexels_videos_2048246 (1080p).mp4

cap = cv2.VideoCapture(video_path)

prev_frame_time = 0

# used to record the time at which we processed current frame
new_frame_time = 0

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()


    if success:

        font = cv2.FONT_HERSHEY_SIMPLEX
        # time when we finish processing for this frame
        new_frame_time = time.time()

        fps = 1 / (new_frame_time - prev_frame_time)
        prev_frame_time = new_frame_time


        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True, tracker="bytetrack.yaml")

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        fps = int(fps)

        # converting the fps to string so that we can display it on frame
        # by using putText function
        fps = str(fps)

        # putting the FPS count on the frame
        cv2.putText(annotated_frame, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)



        # Display the annotated frame
        cv2.imshow("YOLOv8 Tracking", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()

