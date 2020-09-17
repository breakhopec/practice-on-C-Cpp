import json
from base64 import b64decode

filename = 'video_data.dat'
with open(filename, 'rb') as file_object:
    origin = json.loads((file_object.read()).decode('utf-8'))

video_data = b64decode(origin['data'].encode('utf-8'))

with open('new.mp4', 'wb') as file_object:
    file_object.write(video_data)