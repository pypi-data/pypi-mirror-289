import subprocess

class Client:
    def __init__(self):
        self.video_file = None
        self.audio_file = None
        self.video_loop = False
        self.audio_loop = False
        self.stream_size = "1920x1080"
        self.stream_fps = "30"
        self.stream_token = None
        self.stream_service = None
        self.stream_preset = "veryfast"

    def stream(self):
        # Placeholder for actual streaming logic
        print("Streaming started...")

    def video(self, video_file):
        self.video_file = video_file
        print(f"Video set to: {video_file}")

    def videoBucle(self, loop):
        self.video_loop = loop
        print(f"Video loop set to: {loop}")

    def audio(self, audio_file):
        self.audio_file = audio_file
        print(f"Audio set to: {audio_file}")

    def audioBucle(self, loop):
        self.audio_loop = loop
        print(f"Audio loop set to: {loop}")

    def streamSize(self, size):
        self.stream_size = size
        print(f"Stream size set to: {size}")

    def streamFPS(self, fps):
        self.stream_fps = fps
        print(f"Stream FPS set to: {fps}")

    def streamToken(self, token):
        self.stream_token = token
        print(f"Stream token set to: {token}")

    def streamService(self, service):
        self.stream_service = service
        print(f"Stream service set to: {service}")

    def streamPreset(self, preset):
        self.stream_preset = preset
        print(f"Stream preset set to: {preset}")

    def execute_stream(self):
        # Construct the ffmpeg command
        command = [
            "ffmpeg",
            "-stream_loop", "-1" if self.video_loop else "1",
            "-re", "-i", self.video_file,
            "-stream_loop", "-1" if self.audio_loop else "1",
            "-re", "-i", self.audio_file,
            "-vf", f"scale={self.stream_size}",
            "-vcodec", "libx264",
            "-pix_fmt", "yuv420p",
            "-maxrate", "20k",
            "-bufsize", "8000k",
            "-preset", self.stream_preset,
            "-r", self.stream_fps,
            "-g", "60",
            "-c:a", "aac",
            "-b:a", "128k",
            "-ar", "44100",
            "-strict", "experimental",
            "-b:v", "4000k",
            "-f", "flv",
            f"rtmp://live.twitch.tv/app/{self.stream_token}"
        ]

        print(f"Running command: {' '.join(command)}")
        subprocess.run(command)
