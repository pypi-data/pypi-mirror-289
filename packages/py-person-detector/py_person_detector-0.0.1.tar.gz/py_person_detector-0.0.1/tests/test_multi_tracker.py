import cv2

from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO("models/yolov10x.pt")

# Open the video file
video_path = "/home/swift/code/person-detection/.assets/videos/ManchesterCity-ManchesterUnited1-3(1976-77).mp4"
cap = cv2.VideoCapture(video_path)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True, conf=0.3, iou=0.5, tracker="botsort.yaml")

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        boxes = results[0].boxes.xywh.cpu().tolist()
        print(f"Boxes: {boxes}")
        if len(boxes) > 0:
            track_ids = results[0].boxes.id.int().cpu().tolist()
            print(f"Track IDs: {track_ids}")

        # Display the annotated frame
        cv2.imshow("YOLOv10 Tracking", annotated_frame)
        cv2.waitKey(1)