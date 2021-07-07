import speech_recognition

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	print("Robot: I'm Listening")
	audio = robot_ear.listen(mic)

try:
	You = robot_ear.recognizer_google(audio)
except:
	You == ""

print("You: " + you)