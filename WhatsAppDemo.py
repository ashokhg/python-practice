import pywhatkit as pwt

from datetime import datetime

now = datetime.now()

current_hour = now.strftime("%H")
current_min = now.strftime("%M")
nxt_min = int(current_min) + 2
hour = int(current_hour)
min = nxt_min

#print(type(hour))
pwt.sendwhatmsg('+918317304808', 'Hello Durga : Abnormal Action Detected', hour, min)