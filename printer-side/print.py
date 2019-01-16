import requests
import schedule
import time
import re
import cStringIO
from PIL import Image

# TODO: Edit zj-58 driver to make the media size smaller?

def print_messages():
    print("hello")
    r = requests.get("http://localhost:3001/messages")
    for message in r.json():
        id = message["id"]
        print(message["id"])
        print(message["text"])
        print(message["image"])

        image_data = re.sub('^data:image/.+;base64,', '', message["image"]).decode('base64')
        image = Image.open(cStringIO.StringIO(image_data))
        image.save("test_drawing.png")
        # image = image.convert("L")
        # image.save("test_drawing_gray.png")
        image = image.convert("1")
        image.save("test_drawing_1bit.bmp")
        requests.delete("http://localhost:3001/messages/%s" %(id))

schedule.every(5).seconds.do(print_messages)

while True:
    schedule.run_pending()
    time.sleep(1)
