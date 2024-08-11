import os
import subprocess

class StreamSYS:
    def __init__(self):
        self.video_file = None
        self.audio_file = None
        self.video_bucle = False
        self.audio_bucle = False
        self.stream_size = "1080x720"
        self.stream_fps = 30
        self.stream_token = None
        self.stream_service = None
        self.stream_preset = "veryfast"

    def stream(self):
        print("Starting stream setup...")

    def video(self, video_file):
        self.video_file = video_file

    def videoBucle(self, loop):
        self.video_bucle = loop

    def audio(self, audio_file):
        self.audio_file = audio_file

    def audioBucle(self, loop):
        self.audio_bucle = loop

    def streamSize(self, size):
        self.stream_size = size

    def streamFPS(self, fps):
        self.stream_fps = fps

    def streamToken(self, token):
        self.stream_token = token

    def streamService(self, service):
        self.stream_service = service

    def streamPreset(self, preset):
        self.stream_preset = preset

    def start_stream(self):
        cmd = [
            "ffmpeg",
            "-stream_loop", "-1" if self.video_bucle else "1",
            "-re", "-i", self.video_file,
            "-stream_loop", "-1" if self.audio_bucle else "1",
            "-re", "-i", self.audio_file,
            "-vf", f"scale={self.stream_size}",
            "-vcodec", "libx264",
            "-pix_fmt", "yuv420p",
            "-maxrate", "20k",
            "-bufsize", "8000k",
            "-preset", self.stream_preset,
            "-r", str(self.stream_fps),
            "-g", "60",
            "-c:a", "aac",
            "-b:a", "128k",
            "-ar", "44100",
            "-strict", "experimental",
            "-b:v", "4000k",
            "-f", "flv", self.get_service_url()
        ]

        print(f"Running command: {' '.join(cmd)}")
        subprocess.run(cmd)

    def get_service_url(self):
        if "youtube" in self.stream_service.lower():
            return f"rtmp://a.rtmp.youtube.com/live2/{self.stream_token}"
        elif "twitch" in self.stream_service.lower():
            return f"rtmp://live.twitch.tv/app/{self.stream_token}"
        else:
            raise ValueError("Unsupported streaming service")

