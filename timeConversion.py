import sys

time = input().strip()

keep = time[2:-2]
hour = int(time[:2])
check = time[-2:]

if check == "PM" and hour != 12:
    hour += 12

if check == "AM" and hour == 12:
    hour = 0

out = str(hour) + keep
if hour < 10:
    out = "0" + out

print(out)
