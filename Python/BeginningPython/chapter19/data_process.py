import json
from base64 import b64encode

filename = 'unravel.mp4'
with open(filename, 'rb') as file_object:
    video_data = b64encode(file_object.read()).decode('utf-8')

data = {
    'name': filename,
    'type': 'mp4',
    'perfomer': 'Xi',
    'data': video_data
}

encoded = (json.dumps(data, indent=4)).encode('utf-8')

with open('video_data.dat', 'wb') as file_object:
    file_object.write(encoded)