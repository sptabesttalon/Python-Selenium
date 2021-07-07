# import pyttsx3

# robot_brain = "I dell hear du, try ờ gên"

# robot_mouth = pyttsx3.init()
# robot_mouth.say(robot_brain)
# robot_mouth.runAndWait()

# import time

# t = time.localtime()
# current_time = time.strftime("%H:%M:%S", t)
# print(current_time)
from datetime import date
from datetime import datetime

today = date.today()
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)
print("Today's date:", today)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
