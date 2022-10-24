# video_compression_mvp
Created as part of the university course "TDT4290 Kundestyrt prosjekt" at the Norwegian University of Science and Technology for the customer Bulbitech AS. The code is based in large part on the group projects [main repository](https://github.com/Siguhau/FFmpeg-video-compression).

The repository is the minimum viable product that aims to compress a stream of images in RAM. It can encode the video both on the CPU as well as a Nvidia GPU and can be extended to more codecs.

The people that worked on the research and the code are:

- [Adrian Arthur Andersen](https://github.com/AdrianAndersen)
- [Leonhard Benkert](https://github.com/Leonhard-Benkert)
- [Sigurd Hauan](https://github.com/Siguhau)
- [Ellen Yu](https://github.com/ellnyu)
- Tuva Heggen Thiis

## Setup
The file `main.py` begins with a number of variables that need to be set for the project to run correctly. This includes the input and output paths (as relative paths within the project directory) as well as the GPU use. It is strongly recommended to put the files into the `assets` folder as no further ajustments to the `docker-compose` are necessary then.

## Run scrip with docker (recommended)
Make sure to install docker on your computer ([MacOS](https://docs.docker.com/desktop/install/mac-install/), [Linux](https://docs.docker.com/desktop/install/linux-install/), [Windows](https://docs.docker.com/desktop/install/windows-install/)).

After finishing the setup, run the following command in the project directory: 
``` bash
$ docker compose up
```
After the script exists, the compressed video should appear in the `assets` folder.

## Run script manually

FFmpeg *must* be installed on the os-level to run this project. FFmpeg is available for download [here](https://ffmpeg.org/download.html).

Other requirements can be installed with the following command:
``` bash
$ pip install -r requirements.txt
```
To run the script, execute the following command in the `src` directory:
``` bash
$ python3 main.py
```