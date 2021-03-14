# sneed
A simple tool that lets you create a video, webm or gif from any video file.

**Requirements**
* python3
* ffmpeg 4.3.2 (with --enable-libass, --enable-libdav1d, libavcodec, libavformat)

**How To Use**

**Option 1: Video**

Can be used to create or extract videos out of an input files in various formats and can convert the input file.

* Input file name must include extension e.g. input.mp4, input.mkv. 
* Specify a start and end time by using the (hh:mm:ss) format, e.g. (00:01:32) for 1 minute 32 seconds.
* Available Resolutions: 4k, 1080p, 720p, 480p, 360p. Simply type '720p' to select a resolution of 1280x720p or leave blank to use the resolution of the input file.
* Available Codecs: H264, VP8, VP9, AV1. Simply type 'VP9' to select the VP9 codec or leave blank to use default H264. Always use VP8 for .webms.
* Available Bitrates: 0.5M, 1M or 2M. Simply type '0.5M' to select a bitrate of 0.5M or leave blank to use default 0.5M.
* Remove Audio by typing 'remove' when prompted or leave blank to include the audio.
* Output file name must include extensions e.g. output.mp4, output.mkv. Convert the input file by changing output file type e.g. input.mkv -> output.mp4.

**Option 2: 4Chan Webm**

Automatically selects the VP8 codec as required by 4Chan. Limits the filesize to a maximum of 4 MB - this means it will stop encoding once the filesize limit is reached ignoring the duration. Lower the bitrate or duration to stay under the FS limit.

* Input file name must include extension e.g. input.mp4, input.mkv. 
* Specify a start and end time by using the (hh:mm:ss) format, e.g. (00:01:32) for 1 minute 32 seconds.
* Available Resolutions: 4k, 1080p, 720p, 480p, 360p. Simply type '720p' to select a resolution of 1280x720p or leave blank to use the resolution of the input file.
* Select any bitrate you want by using the 0.5M, 1M or 2M syntax. Example: Type 1.5M to select a bitrate of 1.5M or 0.1M to select a bitrate of 0.5M. 
* Remove Audio by typing 'remove' when prompted or leave blank to include the audio. Audio has to be removed to be accepted by 4Chan unless it is for /gif/ & /wsg/.
* Output file type is .webm. Simply type the name of your output file e.g. output and it will create output.webm.

**Option 3: Hardcoded Subtitles**

Creates an output file with hardcoded subtitles pulled from the stream of the input file. .srt option will be added later. Can be used to create .mp4s, .webms with hardcoded subtitles and sound or no sound. 
Most .mkvs set english as the default subtitle stream - if this is not the case you can use 'ffprobe input.mkv' in the terminal to get detailed file information or check vlc, mpv to get a number for the subtitle stream you want e.g. mpv shows "Subtitle (5) - Eng)" == Subtitle Stream ID = 5.
Make sure codecs and output files are compatible with subtitles. Certain conversions do not work. .mkv to H264 mp4 or VP8 webm generally works and is recommended.


* Input file name must include extension e.g. input.mp4, input.mkv. 
* Specify a start and end time by using the (hh:mm:ss) format, e.g. (00:01:32) for 1 minute 32 seconds.
* Specify the subtitle stream id. Get it by using ffprobe or vlc/mpv.
* Available Resolutions: 4k, 1080p, 720p, 480p, 360p. Simply type '720p' to select a resolution of 1280x720p or leave blank to use the resolution of the input file.
* Available Codecs: H264, VP8, VP9, AV1. Simply type 'VP9' to select the VP9 codec or leave blank to use default H264. Always use VP8 for .webms.
* Available Bitrates: 0.5M, 1M or 2M. Simply type '0.5M' to select a bitrate of 0.5M or leave blank to use default 0.5M.
* Remove Audio by typing 'remove' when prompted or leave blank to include the audio.
* Output file name must include extensions e.g. output.mp4, output.mkv. Convert the input file by changing output file type e.g. input.mkv -> output.mp4.


**Option 4: Gifs**

Creates a .gif with reasonable quality and filesize. 

* Input file name must include extension e.g. input.mp4, input.mkv.
* Specify a start and end time by using the (hh:mm:ss) format, e.g. (00:01:32) for 1 minute 32 seconds.
* Output file type is .gif. Simply type the name of your output file e.g. output and it will create output.gif.

**Option 5: Exit**

Quits out of the program.


**FFMPEG Commands**

Here are the ffmpeg commands used in this program. Use them to create your own or modify them to modify the program.

**Video**

Code:

```ffmpeg -i {filename} -ss {start} -to {end} {resolution} {codec} {bitrate} {audio} {output}```

Example:
 
```ffmpeg -i input.mkv -ss 00:00:00 -to 00:00:10 -vf scale=1280:720 -vcodec libx264 -b:v = 0.5M -an output.mp4```

Creates a H264 .mp4 with a duration of 10 second starting from 00:00:00 with a resolution of 720p and a bitrate of 0.5M.

**Webm**

Code:

```ffmpeg -ss {start} -to {end} -i {filename} -fs 4M -vcodec libvpx -b:v {bitrate} {audio} {output}.webm```

Example:

```ffmpeg -ss 00:00:00 -to 00:00:10 -i input.mkv -fs 4M -vcodec libvpx -b:v 1M -an output.webm```

Creates a VP8 .webm with a duration of 10 seconds starting from 00:00:00 using the resolution of the input file with a maximum filesize of 4MB, bitrate of 1M and without sound (-an flag).

**Hardcoded Subtitles**

Code:

```ffmpeg -ss {start} -copyts -i {filename} -vf subtitles={filename}:si={stream} -ss {start} -to {end} {resolution} {codec} {bitrate} {audio} {output}```

Example:

```ffmpeg -ss 00:00:00 -copyts -i input.mkv -vf subtitles=input.mkv:si=1 -ss 00:00:00 -to 00:00:10 -vf scale=1280:720 -vcodec libvpx -0.5M -an output.webm```

Creates a VP8 .webm with a duration of 10 seconds with hardcoded subtitles from subtitle stream 1 starting from 00:00:00 with a resolution of 720P and a bitrate of 0.5M and no sound.

**Gifs**

Code:

```ffmpeg -ss {start} -to {end} -i {filename} -filter_complex \"[0:v] fps=12,scale=480:-1,split [a][b];[a] palettegen [p];[b][p] paletteuse\" {gifname}.gif```

Example:

```ffmpeg -ss 00:00:00 -to 00:00:5 -i input.mp4 -filter_complex \"[0:v] fps=12,scale=480:-1,split [a][b];[a] palettegen [p];[b][p] paletteuse\" output.gif```

Creates a .gif with a duration of 5 seconds from input.mp4 starting from 00:00:00.





