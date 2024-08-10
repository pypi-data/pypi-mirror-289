"""This module provides functionality for working with Videos and Images. 

Developer warning: This module was not made to look pretty, but to be as 
efficient as possible while using the opencv library.

Classes:
    VideoUtils: A class for converting between video and image formats.

Examples:
    Convert a video to a collection of images:

    >>> python -m image_utils.py -v2i -i "path/to/video.py" \\
    ...     -o output/path/of/images \\
    ...     -t "1722658554432" \\
    ...     -f 4

"""

import os
import cv2
import logging
import pathlib
import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

import numpy

from src.utils import enums
from src.utils.datetime_utils import DateTimeUtils


class ImageUtils:
    """A class for converting between video and image formats.

    This class provides methods to:

        - Convert a video file to a sequence of images.
        - Create a video file from a sequence of images.

    Attributes:
        
        - BATCH_SIZE (int): The size of each batch of images in seconds

    Methods:

        video_to_images(
            input_video_path: pathlib.Path,
            image_output_path: pathlib.Path,
            first_frame_timestamp: str = None,
            framerate: int = None
        ) -> None:
            Converts a video to images, extracting frames at a specified rate.

        images_to_video(
            input_images_path: pathlib.Path, 
            video_output_path: pathlib.Path
        ) -> None:
            Creates a video from a sequence of images in a directory.
        
    """

    BATCH_SIZE = 60

    def video_to_images(
            self,
            input_video_path: pathlib.Path,
            image_output_path: pathlib.Path,
            framerate: enums.Framerate,
            first_frame_timestamp: int = None,
    ) -> None:

        """Extracts frames from a video file.

        Args:
            input_video_path (pathlib.Path): Path to the video file.

            image_output_path (pathlib.Path): Path to the output directory 
                where frames will be saved.

            framerate (enums.Framerate): The number of frames per second to be 
                extracted from the video.

            first_frame_timestamp (int): The timestamp of the first frame of the 
                video. If none is provided, the current timestamp will be used. 
                (default: None).

        Returns:
            None.

        Example:
            ```
            >>> input_video_path = pathlib.Path("path/to/video.mp4")
            >>> image_output_path = pathlib.Path("path/to/extracted_frames")
            >>> first_frame_timestamp = 1722658554000
            >>> framerate = enums.Framerate.FOUR
            >>> VideoUtils().video_to_images(
                    input_video_path=input_video_path, 
                    image_output_path=image_output_path,
                    first_frame_timestamp=first_frame_timestamp,
                    framerate=framerate
                )
            ```
        """

        framerate = framerate.value
        frame_time = 1000 / framerate

        if first_frame_timestamp is None:
            first_frame_timestamp = DateTimeUtils.datetime_to_timestamp(
                date_time=datetime.datetime.now()
            )

        cap = None
        try:
            cap = cv2.VideoCapture(str(input_video_path))
            if not cap.isOpened():
                raise FileNotFoundError(
                    f"Cannot open video file {input_video_path}"
                )

            video_fps = cap.get(cv2.CAP_PROP_FPS)
            frame_interval = int(video_fps / framerate)

            image_output_path.mkdir(exist_ok=True)

            frames = []
            frame_count = 0
            saved_frame_count = 0

            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                if frame_count % frame_interval == 0:
                    frame_timestamp = int(
                        first_frame_timestamp + (frame_time * saved_frame_count)
                    )
                    frames.append((frame, frame_count, frame_timestamp))
                    saved_frame_count += 1
                
                frame_count += 1

                if len(frames) >= framerate * self.BATCH_SIZE:
                    self.__process_batch(
                        frames,
                        image_output_path
                    )
                    frames = []

            # process any leftover frames
            if frames:
                self.__process_batch(
                    frames,
                    image_output_path
                )

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

    @staticmethod
    def __process_batch(
        frames: list,
        output_path: pathlib.Path
    ) -> None:
        """Process and save a batch of frames.
        
        Args:
            frames (list): a list, or batch, of frames to be processed and 
                saved.

            output_path (pathlib.Path): Output path for the batch of frames.
            
        Returns:
            None.
        """

        try:
            batch_timestamp = frames[0][2]
            batch_path = output_path / str(batch_timestamp)
            batch_path.mkdir(exist_ok=True)
            
            with ThreadPoolExecutor() as executor:
                futures = [
                    executor.submit(
                        ImageUtils.__save_frame, 
                        frame,
                        batch_path,
                        frame_timestamp)
                    for frame, _, frame_timestamp in frames
                ]
                for future in as_completed(futures):
                    future.result()

        except Exception as e:
            print(f"Error processing batch: {e}")

    @staticmethod
    def __save_frame(
        frame: numpy.ndarray, 
        batch_output_path: pathlib.Path,
        frame_timestamp: int
    ) -> None:
        """Resize and save a single frame.
        
        Args:
            frame (numpy.ndarray): A numpy array of frame data.

            batch_output_path (pathlib.Path): Output path for this batch of 
                frames.

            frame_timestamp (int): The unix timestamp of this frame.
            
        Returns:
            None.
        """

        try:
            output_file = os.path.join(
                batch_output_path, 
                f"{frame_timestamp}.jpg"
            )
            cv2.imwrite(output_file, frame)

        except cv2.error as e:
            print(f"OpenCV error while saving frame: {e}")

        except Exception as e:
            print(f"Unexpected error while saving frame: {e}")

    def images_to_video():
        """"""

        # Todo
        raise NotImplementedError


if __name__ == "__main__":
    # Todo: command line usage
    ...
