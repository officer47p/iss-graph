import requests
import time


while True:
    try:
        req = requests.get("http://api.open-notify.org/iss-now.json")
        res = req.json()
        print(res)
        with open("coordinates.csv", "a") as f:
            data = {"pos": {"lat": res["iss_position"]["latitude"], "lon": res["iss_position"]["longitude"]}, "ts": res["timestamp"]}
            f.write(str(data) + "\n")
        time.sleep(2)
    except Exception as e:
        with open("logs.txt", "a") as f:
            f.write(str(e) + "\n")
        print("Error: {}".format(e))
