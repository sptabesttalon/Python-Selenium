import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 3
button = Button.left
start_stop_key=KeyCode(char='s')
exit_key=KeyCode(char='e')

class ClickMouse(threading.Thread):
	def __init__(self,delay,button):
		super(ClickMouse, self).__init__()
		self.delay = delay
		self.button = button
		self.running = False
		self.program_running=True
	def star_clicking(self):
		self.running=True
	def stop_clickinng(self):
		self.running=False
	def exit(self):
		self.running=True
	def run(self):
		while self.program_running:
			while self.running:
				mouse.click(self.button)
				time.sleep(self.delay)
mouse=Controller()
click_thread=ClickMouse(delay,button)
click_thread.start()