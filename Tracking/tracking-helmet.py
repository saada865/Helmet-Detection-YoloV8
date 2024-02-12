import cv2
from ultralytics import YOLO
# !pip3 install lap
from time import time

# Load the YOLOv8 model
model = YOLO('/Users/saadahmadmalik/Downloads/best.pt')

# Open the video file

video_path = "/Users/saadahmadmalik/Downloads/pexels_videos_2048246 (1080p).mp4"

#pexels-pavel-danilyuk-7817205 (1080p).mp4
#pexels_videos_2048246 (1080p).mp4

cap = cv2.VideoCapture(video_path)

loop_time = time()

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()


    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        fps_text = 1 / (time() - loop_time)
        print('FPS: {}'.format(fps_text))
        loop_time = time()



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

