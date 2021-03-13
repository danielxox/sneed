import subprocess

print("This program extracts a clip out of any video file")

dict = {
  
  "4k"    : str("-vf scale=3840:2160"),
  "1080p" : str("-vf scale=1920:1080"),
  "720p"  : str("-vf scale=1280:720"),
  "480p"  : str("-vf scale=852:480"),
  "360p"  : str("-vf scale=480:360"),
  "H264"  : str("-vcodec libx264"),
  "VP8"   : str("-vcodec libvpx"),
  "VP9"   : str("-vcodec libvpx-vp9"),
  "AV1"   : str("-vcodec libaom-av1"),
  "0.5M"  : str("-b:v 0.5M"),
  "1M"    : str("-b:v 1M"),
  "2M"    : str("-b:v 2M"),
  "remove": str("-an")

    }

def menu():
  print("[01] Video")
  print("[02] 4Chan Webm")
  print("[03] Hardcoded Subtitles")
  print("[04] Gif")
  print("[05] Exit Program")

menu()

option = int(input("Select an option: "))

while option != 0:
  if option == 1:
    print("Extracs, creates or converts a video. Follow instructions. Leave field blank to choose the default option.")
    filename = input("Filename must include extension e.g. video.mp4 \n Enter the filename: ")
    start = input("Enter the start time (hh:mm:ss): ")
    end = input("Enter the end time (hh:mm:ss): ")
    res = input("Options: 4k, 1080p, 720p, 480p, 360p (default: blank for inputfile resolution) \n Enter the resolution: ")
    codec = input("Options: H264, VP8, VP9, AV1 (default: H264) \n Specify Codec: ")
    bit = input("Options: 0.5M, 1M, 2M (default: 0.5M) \n Enter Bitrate: ")
    aud = input("Type 'remove' to remove Audio or leave blank to include audio: ")
    output = input("Filename must include extension. Use extension different from input to convert the video, e.g. .mp4 -> .webm \n Enter the new filename: ")
    resolution = dict.get(res, "")
    codec = dict.get(codec, "-vcodec libx264")
    bitrate = dict.get(bit, "-b:v 0.5M")
    audio = dict.get(aud, "")

    subprocess.call(f"ffmpeg -i {filename} -ss {start} -to {end} {resolution} {codec} {bitrate} {audio} {output}", shell=True)

    print(f"Successfully created {output} from {filename} starting from {start} until {end}")

  elif option == 2:

    print("Creates a .webm with a maximum Filesize of 4MB. Lower Duration or Bitrate if duration exceeds the filesize")
    filename = input("Enter the filename: ")
    start = input("Enter the start time (hh:mm:ss): ")
    end = input("Enter the end time (hh:mm:ss): ")
    res = input("Options: 4k, 1080p, 720p, 480p, 360p (default: blank for inputfile resolution) \n Enter the resolution: ")
    bitrate = input("Enter Bitrate (e.g. 0.5M, 1M, 2M): ")
    aud = input("Type 'remove' to remove Audio or leave blank to include audio: ")
    output = input("Enter .webm name: ")
    resolution = dict.get(res, "")
    audio = dict.get(aud, "")

    subprocess.call(f"ffmpeg -ss {start} -to {end} -i {filename} -fs 4M -vcodec libvpx -b:v {bitrate} {audio} {output}.webm", shell=True)

  elif option == 3:

    print("Hardcodes a subtitle stream into the output file. You can use ffprobe to get the subtitle stream ID. ")
    filename = input("Enter the filename: ")
    stream = input("Specify subtitle stream id: ")
    start = (input("Enter the start time (hh:mm:ss): "))
    end = (input("Enter the end time (hh:mm:ss): "))
    res = input("Options: 4k, 1080p, 720p, 480p, 360p (default: blank for inputfile resolution) \n Enter the resolution: ")
    codec = input("Options: H264, VP8, VP9, AV1 (default: H264) \n Specify codec (H264 for mp4 / VP8 for webm): ")
    bit = input("Options: 0.5M, 1M, 2M (default: 0.5M) \n Enter Bitrate: ")
    aud = input("Type 'remove' to remove Audio or leave blank to include audio: ")
    output = input("Filename must include extension. Use extension different from input to convert the video, e.g. .mp4 -> .webm \n Enter the new filename: ")
    resolution = dict.get(res, "")
    codec = dict.get(codec, "-vcodec libx264")
    bitrate = dict.get(bit, "-b:v 0.5M")
    audio = dict.get(aud, "")

    subprocess.call(f"ffmpeg -ss {start} -copyts -i {filename} -vf subtitles={filename}:si={stream} -ss {start} -to {end} {resolution} {codec} {bitrate} {audio} {output}", shell=True)

  elif option == 4:

    print("Creates a .gif with reasonable filesize.")
    filename = input("Enter the filename: ")
    start = (input("Enter the start time (hh:mm:ss): "))
    end = (input("Enter the end time (hh:mm:ss): "))
    gifname = input("Enter a gif name: ")

    subprocess.call(f"ffmpeg -ss {start} -to {end} -i {filename} -filter_complex \"[0:v] fps=12,scale=480:-1,split [a][b];[a] palettegen [p];[b][p] paletteuse\" {gifname}.gif", shell=True)
  
  elif option == 5:
    quit()
  
  else:
    print ("Invalid Option")

  print()
  menu()
  option = int(input("Select an option: "))

