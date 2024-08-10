"""This module contains classes and functionality to enable person detection.

Classes:
    Detector: A class containing datetime utility methods.
"""

import pathlib
from typing import List

import cv2
import ultralytics


class Detector:
    """A class for detecting people in images.

    This class provides methods to:

        - Detect people in an image

    Methods:

        detect(frame) -> int:
            Detect people in a given image.
    """

    def __init__(
            self, 
            model: str = "models/yolov10x.pt",
            show: bool = False
        ) -> None:
        """Default initializer.
        
        Args:
            model (str): YOLO detection model.
            show (bool): If True, visualization data will be displayed to the 
                user.
            
        Returns:
            None.
        """

        self.model = ultralytics.YOLO(model)
        self.show = show
        self.confidence = 0.5

    def detect_image(self, image: pathlib.Path) -> None:
        """Detect people in a given image.
        
        Args:
            frame: Image, or video frame.
        
        Returns:
            None.
        """

        try:
            frame = cv2.imread(image)

            results = self.model.predict(
                frame, 
                classes=[0], 
                conf=self.confidence)


            result = results[0]
            annotated_frame = result.plot()

            if self.show:
                cv2.imshow(
                    "YOLOv10 People Detection. Press any key to exit.", 
                    annotated_frame
                )

                cv2.waitKey(0)
        
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")

        except cv2.error as e:
            print(f"OpenCV error: {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")

        finally:
            cv2.destroyAllWindows()

    def detect_video(self, video: pathlib.Path):
        """
        Detect people in a given video.
        """
        try:
            cap = cv2.VideoCapture(video)

            while True:
                success, frame = cap.read()
                if not success:
                    break

                results = self.model.predict(
                    frame, 
                    classes=[0], 
                    conf=self.confidence
                )

                for result in results:
                    for box in result.boxes:
                        cv2.rectangle(
                            img=frame, 
                            pt1=(int(box.xyxy[0][0]), int(box.xyxy[0][1])),
                            pt2=(int(box.xyxy[0][2]), int(box.xyxy[0][3])), 
                            color=(255, 0, 0), 
                            thickness=2
                        )
                        cv2.putText(
                            img=frame, 
                            text=f"{result.names[int(box.cls[0])]}",
                            org=(int(box.xyxy[0][0]), int(box.xyxy[0][1]) - 10),
                            fontFace=cv2.FONT_HERSHEY_PLAIN, 
                            fontScale=1, 
                            color=(255, 0, 0), 
                            thickness=2
                        )

                cv2.imshow(
                    "Detections: press any key to close", 
                    frame
                )
                
                cv2.waitKey(1)

        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")

        except cv2.error as e:
            print(f"OpenCV error: {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")

        finally:
            cv2.destroyAllWindows()
            

if __name__ == "__main__":
    Detector().detect(
        image=pathlib.Path("assets/images/The-famous-Shibuya-crossing-90-seconds(720p)/1722658554000/1722658583500.jpg")
    )
