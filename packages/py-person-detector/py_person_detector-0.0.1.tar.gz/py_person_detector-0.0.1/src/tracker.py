"""This module contains classes and functionality to enable person tracking.

Classes:
    Tracker: A class containing datetime utility methods.
    Track: A class for storing track data"""

import pathlib
from typing import List

import cv2
import ultralytics
import ultralytics.engine
import ultralytics.engine.results


class Tracker:
    """A class for tracking people in video footage.

    This class provides methods to:

        - Track people in a given video

    Methods:

        start(
            video: pathlib.Path
        ) -> None:
            Start tracking people in a given video.
    """

    def __init__(
            self, 
            model: str = "models/yolov10x.pt",
            show: bool = True
        ) -> None:
    
        """Default initializer.
        
        Args:
            model (str): YOLO detection model.
            
        Returns:
            None.
        """

        self.model = ultralytics.YOLO(model)
        self.tracks = list()
        self.show = show

    def track(self, video: pathlib.Path) -> None:
        """Start tracking of people in a given video.
        
        Args:
            video (pathlib.Path): Path to video file with people to track.
        
        Returns:
            None.
        """

        try:
            cap = cv2.VideoCapture(video)

            while cap.isOpened():
                success, frame = cap.read()

                if success:
                    results = self.model.track(
                        source=frame, 
                        persist=True, 
                        conf=0.45, 
                        iou=0.5,
                        classes=[0],
                        tracker="bytetrack.yaml"
                    )

                    result = results[0]
                    annotated_frame = result.plot()

                    if self.show:
                        cv2.imshow(
                            "YOLOv10 People Tracking. Press 'q' to stop.", 
                            annotated_frame
                        )

                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
        
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")

        except cv2.error as e:
            print(f"OpenCV error: {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")

        finally:
            if cap is not None:
                cap.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    Tracker().track(
        video="assets/videos/Temple_Bar_Webcam_Dublin_by_EarthCam.mp4"
    )
