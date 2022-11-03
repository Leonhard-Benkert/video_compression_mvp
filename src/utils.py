import cv2
import os


def get_framerate(path: str) -> int:
    """
    returns the framerate of the video on given path
    :param path: absolute path to a video file
    :return: framerate of video in fps
    """
    vidcap = cv2.VideoCapture(path)
    fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    return fps


def generate_ffmpeg_cmd(frame_width: int, frame_height: int, video_fps: int, output_path: str, use_nvidia_gpu=False) -> list[str]:
    """
    generates the command to use ffmpeg
    :param frame_width: number of pixels in the x-axis of the video
    :param frame_height: number of pixels in the y-axis of the video
    :param video_fps: desired framerate of the output video
    :param output_path: absolute path including filename where the video will be saved to
    :param use_nvidia_gpu: uses a nvidia compression codec for the compression
    :return: command array
    """
    codec = "h264_nvenc" if use_nvidia_gpu else "h264"
    return [
        "ffmpeg",
        "-loglevel", "error", # reduce console output by ffmpeg\
        "-y", # override output file if existent
        "-an", # specify that video does not have sound
        
        # input
        "-f", "rawvideo", # the input is undecoded
        "-pix_fmt", "bgr24",
        "-s", f"{frame_width}x{frame_height}", # needed as the input is raw video
        "-r", str(video_fps),
        "-i", "-", # needed as the frames are fed to ffmpeg through a pipe
        
        # output
        "-vcodec", codec,
        "-preset", "fast",
        "-r", str(video_fps),
        "-pix_fmt", "bgr24",
        output_path
    ]


def print_video_size_info(path_original: str, path_compressed: str) -> None:
    '''
    prints the sizes of the original and compressed video as well as the compression ratio
    :param path_original: absolute path to the uncompressed video file
    :param path_compressed: absolute path to the uncompressed video file
    :return: None
    '''
    def get_file_size(path: str) -> float:
        '''
         :param path: absolute path to the file
         :return: file size in mb
        '''
        return os.stat(path).st_size / (1024 * 1024)

    size_original_mb = get_file_size(path_original)
    size_compressed_mb = get_file_size(path_compressed)

    print(f"File size original: {round(size_original_mb, 4)} Mb")
    print(f"File size compressed: {round(size_compressed_mb, 4)} Mb")
    print(f"Compression ratio: {round(size_original_mb / size_compressed_mb, 4)}")

