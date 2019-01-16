import requests
import schedule
import time

def print_messages():
    print("hello")
    r = requests.get("http://localhost:3001/messages")
    for message in r.json():
        id = message["id"]
        print(message["id"])
        print(message["text"])
        print(message["image"])
        requests.delete("http://localhost:3001/messages/%s" %(id))

schedule.every(5).seconds.do(print_messages)

while True:
    schedule.run_pending()
    time.sleep(1)
