import sys
import pytube as pt
import whisper
import datetime

def download_and_transcribe_youtube_video(video_url):
    model = whisper.load_model("large")

    date_now = datetime.datetime.now()
    date_format = "%Y-%m-%d_%H-%M-%S"
    date_string = date_now.strftime(date_format)

    yt = pt.YouTube(video_url)
    stream = yt.streams.filter(only_audio=True)[0]
    stream.download(filename="audio_spanish.mp3")

    result = model.transcribe("audio_spanish.mp3", fp16=False)

    file_name = f"file_{date_string}.txt"

    with open(file_name, "w") as file:
        file.write(result["text"])
    print(result["text"])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <youtube_video_url>")
        sys.exit(1)

    youtube_video_url = sys.argv[1]
    download_and_transcribe_youtube_video(youtube_video_url)