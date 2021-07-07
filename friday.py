import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime

robot_ear = speech_recognition.Recognizer()
you = robot_ear.recognizer_google(audio)
robot_mouth = pyttsx3.init()
robot_brain = ""

with speech_recognition.Microphone() as mic:
	print("Robot: I'm Listening")
	audio = robot_ear.listen(mic)

print("Robot:...")

try:
	you = robot_ear.recognizer_google(audio)
except:
	you == ""
print("You: " + you)

if you == "":
	robot_brain = "I dell hear du, try ờ gên"
elif you == "Hello":
	robot_brain = " Lô kum kẹc"
elif you == "Today":
	today = date.today()
	robot_brain = today.strftime("%B %d, %Y")
elif you == "Time"
	now = datetime.now()
	robot_brain = now.strftime("%H:%M:%S")	
else:
	robot_brain = " Eim ok en du"

print(robot_brain)

robot_brain = "I dell hear du, try ờ gên"

robot_mouth.say(robot_brain)
robot_mouth.runAndWait()