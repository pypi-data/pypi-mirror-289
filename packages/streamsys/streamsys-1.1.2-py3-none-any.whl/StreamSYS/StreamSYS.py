import sys
import subprocess
import os

class Client:
    def __init__(self):
        self.video_file = None
        self.video_loop = False
        self.audio_file = None
        self.audio_loop = False
        self.stream_size = "1280x720"
        self.stream_fps = "30"
        self.stream_token = None
        self.stream_service = None
        self.stream_preset = "veryfast"

    def stream(self):
        print("Starting stream...")

    def video(self, video_file):
        self.video_file = video_file
        print(f"Video set to {video_file}")

    def videoBucle(self, loop):
        self.video_loop = loop
        print(f"Video loop set to {loop}")

    def audio(self, audio_file):
        self.audio_file = audio_file
        print(f"Audio set to {audio_file}")

    def audioBucle(self, loop):
        self.audio_loop = loop
        print(f"Audio loop set to {loop}")

    def streamSize(self, size):
        self.stream_size = size
        print(f"Stream size set to {size}")

    def streamFPS(self, fps):
        self.stream_fps = fps
        print(f"Stream FPS set to {fps}")

    def streamToken(self, token):
        self.stream_token = token
        print("Stream token set")

    def streamService(self, service):
        self.stream_service = service
        print(f"Stream service set to {service}")

    def streamPreset(self, preset):
        self.stream_preset = preset
        print(f"Stream preset set to {preset}")

    def start_stream(self):
        video_loop_flag = "-stream_loop -1" if self.video_loop else ""
        audio_loop_flag = "-stream_loop -1" if self.audio_loop else ""

        ffmpeg_command = [
            "ffmpeg",
            video_loop_flag, "-re", "-i", self.video_file,
            audio_loop_flag, "-re", "-i", self.audio_file,
            "-vf", f"scale={self.stream_size}",
            "-vcodec", "libx264", "-pix_fmt", "yuv420p",
            "-maxrate", "20k", "-bufsize", "8000k",
            "-preset", self.stream_preset,
            "-r", self.stream_fps, "-g", "60",
            "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
            "-strict", "experimental", "-b:v", "4000k",
            "-f", "flv", f"rtmp://live.{self.stream_service}.tv/app/{self.stream_token}"
        ]

        subprocess.run(ffmpeg_command)

def install_package(package_name):
    package_path = os.path.join(os.path.dirname(__file__), 'packages')
    if not os.path.exists(package_path):
        os.makedirs(package_path)

    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name, "--target", package_path])
        print(f"Package '{package_name}' installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install package '{package_name}'. Error: {e}")

def run_file(filename):
    package_path = os.path.join(os.path.dirname(__file__), 'packages')
    if os.path.exists(package_path):
        sys.path.insert(0, package_path)

    with open(filename, 'r') as file:
        code = file.read()

    exec(code, globals())

def main():
    if len(sys.argv) < 2:
        print("Usage: streamsys <command> [options]")
        sys.exit(1)

    command = sys.argv[1]

    if command == 'run':
        if len(sys.argv) != 3:
            print("Usage: streamsys run <filename.strS>")
            sys.exit(1)
        filename = sys.argv[2]
        if not filename.endswith('.strS'):
            print("File extension must be .strS")
            sys.exit(1)
        if not os.path.exists(filename):
            print(f"File '{filename}' not found.")
            sys.exit(1)
        run_file(filename)
    elif command == 'install':
        if len(sys.argv) != 3:
            print("Usage: streamsys install <package-name>")
            sys.exit(1)
        package_name = sys.argv[2]
        install_package(package_name)
    else:
        print("Unknown command")
        sys.exit(1)

if __name__ == "__main__":
    main()
