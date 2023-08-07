from datetime import datetime

now = datetime.now()

current_hour = now.strftime("%H")
current_min = now.strftime("%M")
nxt_min = int(current_min) + 1
print("Current time = ", current_hour)
print("Current minute =", current_min)
print("Current minute =", nxt_min)