import requests
import schedule
import time
import re
import subprocess
import cStringIO
from PIL import Image

# TODO: Edit zj-58 driver to make the media size smaller?

subprocess.call(["stty", "-F", "/dev/ttyUSB0", "19200"])

def print_messages():
    print("hello")
    # r = requests.get("http://localhost:3001/messages")
    r = requests.get("https://polar-mountain-80188.herokuapp.com/messages")
    for message in r.json():
        id = message["id"]
        print(message["id"])
        print(message["text"])
        print(message["image"])

        image_data = re.sub('^data:image/.+;base64,', '', message["image"]).decode('base64')

        image = Image.open(cStringIO.StringIO(image_data))
        image.save("drawing.png")

        image = image.convert("L")
        image.save("drawing_gray.png")

        image = image.convert("1")
        image.save("drawing_1bit.bmp")

        # subprocess.call(["lp", "-o fit-to-page", "drawing_1bit.bmp"])
        # subprocess.call(["echo", "-e", message["text"], ">", "/dev/ttyUSB0" ])

        # requests.delete("http://localhost:3001/messages/%s" %(id))
        requests.delete("https://polar-mountain-80188.herokuapp.com/messages/%s" %(id))

print_messages()
schedule.every(5).seconds.do(print_messages)

while True:
    schedule.run_pending()
    time.sleep(1)
