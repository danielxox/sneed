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

Automatically selects the VP8 codec as required by 4Chan. Limits the filesize to a maximum of 4 MB - this means it will stop encoding once the filesize limit is reached ignoring the durationg. Lower the bitrate or duration to stay under the FS limit.

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


