"""Main application entry point

Classes:
    Application: A class representing the entry point of the application and 
    handling command-line arguments, etc.
"""


import argparse
import pathlib

from src.detector import Detector
from src.tracker import Tracker
from src.utils.enums import Framerate
from src.utils.image_utils import ImageUtils


class Application:
    """A class representing the entry point of the application and handling 
    command-line arguments, etc.

    This class provides methods to:

        - Start the application with the given commend-line arguments

    Methods:

        start(args) -> None:
            Start application with the given command-line arguments.
    """

    @staticmethod
    def start() -> None:
        """Parse command-line arguments and start the application."""

        parser = argparse.ArgumentParser()

        data_group = parser.add_argument_group(
            "Required Data Input Options", 
            "Choose one of the following data input options."
        )

        data_group.add_argument(
            "-v",
            "--video", 
            help="The path to the video you would like to detect people in.",
            type=str
        )
        
        data_group.add_argument(
            "-i",
            "--image", 
            help="The path to an image you would like to detect people in. \
                  Currently only supports 'detect' functionality",
            type=str
        )

        data_group.add_argument(
            "-v2i",
            "--video2images",
            dest="video_to_images",
            help="The path to video you would like converted to a collection \
                  of images.",
            type=str
        )

        process_group = parser.add_argument_group(
            "Required Process Type Options", 
            "Choose one of the following process type options."
        )

        process_group.add_argument(
            "-d",
            "--detect", 
            help="People detection.",
            action="store_true"
        )

        process_group.add_argument(
            "-t",
            "--track",
            help="People tracking.",
            action="store_true"
        )

        additional_group = parser.add_argument_group(
            "Optional Additional Options", 
            "Choose one of the following additional options."
        )

        additional_group.add_argument(
            "-s",
            "--show",
            help="If this flag is set, visual output of detection/tracking \
                  will be displayed to the user.",
            action="store_true"
        )

        data_group.required = True
        process_group.required = True

        args = parser.parse_args()

        if args.image:
            if args.detect:
                Detector(show=args.show).detect_image(
                    image=pathlib.Path(args.image)
                )
            elif args.track:
                parser.error("ERROR: Tracking via images is currently not supported")

        if args.video:
            if args.detect:
                Detector(show=args.show).detect_video(
                    video=pathlib.Path(args.video)
                )
            elif args.track:
                Tracker().track(
                    video=args.video
                )

        if args.video_to_images:
            video_path = pathlib.Path(args.video_to_images)
            output_dir = pathlib.Path(".") / video_path.name
            ImageUtils().video_to_images(
                input_video_path=video_path,
                image_output_path=output_dir,
                framerate=Framerate.FOUR
            )


if __name__ == "__main__":
    Application.start()
