import pathlib

from src.utils.enums import Framerate
from src.utils.image_utils import ImageUtils


framerate = Framerate.TWO
first_frame_timestamp = 1722658554000

input_video = pathlib.Path("/home/swift/code/person-detection/.assets/videos/The-famous-Shibuya-crossing-90-seconds(720p).mp4")
image_output = pathlib.Path("/home/swift/code/person-detection/.assets/images/The-famous-Shibuya-crossing-90-seconds(720p)")

image_utils = ImageUtils()

image_utils.video_to_images(
    input_video_path=input_video,
    image_output_path=image_output,
    framerate=framerate,
    first_frame_timestamp=first_frame_timestamp
)

print("Done!")