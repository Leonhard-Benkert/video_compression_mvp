# video_compression_mvp
Created as part of the university course "TDT4290 Kundestyrt prosjekt" at the Norwegian University of Science and Technology for the customer Bulbitech AS. The code is based in large part on the group projects [main repository](https://github.com/Siguhau/FFmpeg-video-compression).

The repository is the minimum viable product that aims to compress a stream of images in ram. It can encode the video both on the CPU as well as a Nvidia GPU and can be extended to more codecs.

The people that worked on the research and the code are:

- [Sigurd Hauan](https://github.com/Siguhau)
- [Ellen Yu](https://github.com/ellnyu)
- [Adrian Arthur Andersen](https://github.com/AdrianAndersen)
- Tuva Heggen Thiis
- [Leonhard Benkert](https://github.com/Leonhard-Benkert)

## Setup
FFmpeg *must* be installed to run this project. FFmpeg is available for download [here](https://ffmpeg.org/download.html).

The file main.py begins with a number of variables that need to be set for the project to run correctly. This includes the input and output paths (as relative paths within the project directory) as well as the GPU use.

To run the script, execute `python3 main.py` in the `src` directory.