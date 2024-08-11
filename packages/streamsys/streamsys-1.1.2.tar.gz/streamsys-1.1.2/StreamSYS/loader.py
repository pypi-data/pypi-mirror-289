import re
from .client import Client

def streamsysLoad(file_path):
    client = Client()

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            # Match and execute commands
            if line == "Client.stream();":
                client.stream()

            elif match := re.match(r'Client.video\("(.+?)"\);', line):
                client.video(match.group(1))

            elif match := re.match(r'Client.videoBucle\((True|False)\);', line):
                client.videoBucle(match.group(1) == "True")

            elif match := re.match(r'Client.audio\("(.+?)"\);', line):
                client.audio(match.group(1))

            elif match := re.match(r'Client.audioBucle\((True|False)\);', line):
                client.audioBucle(match.group(1) == "True")

            elif match := re.match(r'Client.streamSize\("(.+?)"\);', line):
                client.streamSize(match.group(1))

            elif match := re.match(r'Client.streamFPS\("(\d+)"\);', line):
                client.streamFPS(match.group(1))

            elif match := re.match(r'Client.streamToken\("(.+?)"\);', line):
                client.streamToken(match.group(1))

            elif match := re.match(r'Client.streamService\("(.+?)"\);', line):
                client.streamService(match.group(1))

            elif match := re.match(r'Client.streamPreset\("(.+?)"\);', line):
                client.streamPreset(match.group(1))

            else:
                print(f"Comando desconocido: {line}")
