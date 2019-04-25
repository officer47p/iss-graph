import requests
from time import sleep


while True:
    req = requests.get("http://api.open-notify.org/iss-now.json")
    res = req.json()
    print(res)
    with open("coordinates.csv", "a") as f:
        f.write(str(res['iss_position']['latitude']) + "," + str(res['iss_position']['longitude']) + "\n")
    sleep(2)
