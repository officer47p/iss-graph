from datetime import datetime

# Your data-set file name
file = open("coordinates_demo.csv", "r")
lines = [int(eval(line)["ts"]) for line in file.readlines()]
firts_t = (lines[0])
last_t = (lines[-1])

print("First fetch was in {}".format(datetime.utcfromtimestamp(firts_t)))
print("Last fetch was in {}".format(datetime.utcfromtimestamp(last_t)))
print("It has taken {} to make the data-set.".format(datetime.utcfromtimestamp(last_t) - datetime.utcfromtimestamp(firts_t)))
