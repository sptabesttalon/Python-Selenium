import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

friday = pyttsx3.init()

def speak(audio):
	print('F.R.I.D.A.Y.: '+ audio)
	friday.say(audio)
	friday.runAndWait()

def time():
	Time=datetime.datetime.now().strftime("%I:%M:%p")
	speak(Time)
def welcome():
	hour=datetime.datetime.now().hour
	if hour>=6 and hour<12:
		speak("Good Morning Sir")
	if hour>=13 and hour<18:
		speak("Good Afternoon Sir")
	if hour>=18 and hour<24:
		speak("Good Night Sir")
	speak('How can i help you')
# Đây trở lên ok!!!

def command():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		r.pause_threshold=2
		audio = r.listen(source)
	try:
		query=r.Recognition_google(audio,language='en')
		print("Tony Stark :" + query)
	except sr.UnknownValueError:
		print("Please repeat or typing the command ")
		query=str(input('You order is: '))
	return query

if __name__ =="__main__":
	welcome()
	while True:
		query=command().lower()
		if "google" in query:
			speak("What should I search boss??")
			search=command().lower()
			url=f"https://www.google.com/search?q={search}"
			wb.get().open(url)
			speak(f'Here is your {search} on google')
		if "Youtube" in query:
			speak("What should I search boss??")
			search=command().lower()
			url=f"https://www.youtube.com/search?q={search}"
			wb.get().open(url)
			speak(f'Here is your {search} on youtube')
		elif  "open video":
			meme=r""
			os.startfile(meme)
		elif "time" in query:
			time()
		elif "quit" in query:
			speak("Friday is quitting sir.Goodbye boss")
			quit()