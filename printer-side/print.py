import requests
import schedule
import time
import re
import os
import subprocess
import cStringIO
import printer
from PIL import Image, ImageDraw

# TODO: Edit zj-58 driver to make the media size smaller?

subprocess.call(["stty", "-F", "/dev/ttyUSB0", "19200"])
#subprocess.call(["stty", "-F", "/dev/ttyAMA1", "19200"])

p = printer.ThermalPrinter()
#p = printer.ThermalPrinter(serialport="/dev/ttyAMA1")


def print_messages():
    print("hello")
    # r = requests.get("http://localhost:3001/messages")
    r = requests.get("https://send-nate-a-message.herokuapp.com/messages")
    for message in r.json():
        id = message["id"]
        print(message["id"])
        print(message["text"])
        print(message["image"])

        image_data = re.sub('^data:image/.+;base64,', '', message["image"]).decode('base64')

        image = Image.open(cStringIO.StringIO(image_data))
        image.save("drawing.png")
        # image.save("pictures/%s.png" %(int(round(time.time() * 1000))))

        # image = image.convert("L")
        # image.save("drawing_gray.png")

        # image = image.convert("1")
        # image.save("drawing_1bit.bmp")

        # image.save('drawing.pdf', 'pdf')

        if message["text"]:
            p.print_text(message["text"])
            p.print_text("\n")
            #os.system("echo %s > /dev/ttyUSB0" %(message["text"]))

        # i = Image.open("drawing.png")
        data = list(image.getdata())
        w, h = image.size
        p.print_bitmap_slow(data, w, h, True)
        #subprocess.call(["lp", "-o fit-to-page", "drawing.pdf"])
        # subprocess.call(["lp", "drawing.png"])

        requests.put("https://send-nate-a-message.herokuapp.com/messages/%s" %(id), params={ 'printed': True })
        # requests.delete("http://localhost:3001/messages/%s" %(id))
        # requests.delete("https://send-nate-a-message.herokuapp.com/messages/%s" %(id))

print_messages()
schedule.every(150).seconds.do(print_messages)

while True:
    schedule.run_pending()
    time.sleep(1)
