from subprocess import Popen, PIPE
import os
import time
import cv2
import numpy as np

from utils import get_framerate, print_video_size_info, generate_ffmpeg_cmd

'''manual inputs'''
input_path_relative = os.path.join("assets", "in.avi") # USER: add video file to project folder and update filename
output_path_relative = os.path.join("assets", "out.avi") # USER: choose filename for output
use_nvidia_gpu = False # USER: set True if computer has a nvidia gpu and the correct sdk

'''setup'''
images: list[np.ndarray] = [] # contains the images after splitting
project_dir = os.path.dirname(os.getcwd())
input_path = os.path.join(project_dir, input_path_relative) # getting the absolute paths to input and output files
output_path = os.path.join(project_dir, output_path_relative)
fps = get_framerate(input_path) # getting framerate of original video


'''splitting video into individual frames'''
print("Splitting video...")
start_time_split = time.time()
capture = cv2.VideoCapture(input_path)

while True:
    success, frame = capture.read() # reading induvidual frames from video
    if success:
        images.append(frame)
    else:
        break

capture.release()
print(f"Time splitting: {round(time.time() - start_time_split, 4)}s")


'''compressing the images in a video'''
print("Compressing video...")
height, width, _ = images[0].shape # getting the frame size
start_time_compression = time.time()

cmd = generate_ffmpeg_cmd(width, height, fps, output_path, use_nvidia_gpu)
pipe = Popen(cmd, shell=False, stdin=PIPE) # opening a pipe with ffmpeg

for image in images: # writing all frames to the pipe
    pipe.stdin.write(image.tobytes())

pipe.stdin.close()
pipe.wait() # wait for the ffmpeg process to finish

print(f"Time compressing: {round(time.time() - start_time_compression, 4)}s")

print_video_size_info(input_path, output_path)
