import subprocess
import os

class StreamSYS:
    def __init__(self):
        self.video_file = ""
        self.audio_file = ""
        self.loop_video = False
        self.loop_audio = False
        self.size = "1080x720"
        self.fps = "30"
        self.token = ""
        self.service = ""
        self.preset = "veryfast"

    def stream(self):
        print("Starting stream...")

    def video(self, video_file):
        self.video_file = video_file

    def videoBucle(self, loop):
        self.loop_video = loop

    def audio(self, audio_file):
        self.audio_file = audio_file

    def audioBucle(self, loop):
        self.loop_audio = loop

    def streamSize(self, size):
        self.size = size

    def streamFPS(self, fps):
        self.fps = fps

    def streamToken(self, token):
        self.token = token

    def streamService(self, service):
        self.service = service

    def streamPreset(self, preset):
        self.preset = preset

    def start_stream(self):
        video_loop_flag = "-stream_loop -1" if self.loop_video else ""
        audio_loop_flag = "-stream_loop -1" if self.loop_audio else ""
        
        service_url = self.get_service_url()

        ffmpeg_command = (
            f"ffmpeg {video_loop_flag} -re -i {self.video_file} "
            f"{audio_loop_flag} -re -i {self.audio_file} "
            f"-vf 'scale={self.size}' -vcodec libx264 -pix_fmt yuv420p "
            f"-preset {self.preset} -r {self.fps} -g 60 "
            f"-c:a aac -b:a 128k -ar 44100 -strict experimental "
            f"-f flv {service_url}"
        )

        print(f"Executing FFmpeg command: {ffmpeg_command}")

        process = subprocess.Popen(
            ffmpeg_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )

        while True:
            output = process.stdout.readline()
            if output == b"" and process.poll() is not None:
                break
            if output:
                print(output.decode().strip())

    def get_service_url(self):
        if "youtube" in self.service.lower():
            return f"rtmp://a.rtmp.youtube.com/live2/{self.token}"
        elif "twitch" in self.service.lower():
            return f"rtmp://live.twitch.tv/app/{self.token}"
        else:
            raise ValueError("Unsupported streaming service")

