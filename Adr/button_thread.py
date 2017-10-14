from threading import Lock, Thread
import launchpad_py
import time
import objs
import random

class button_thread(Thread):
	def __init__(self, launchpad, execute_lock):
		super(button_thread, self).__init__()
		self.lh = launchpad
		self.el = execute_lock
		self.flag = 0

	def stopt(self):
		self.flag = 1

	def run(self):
		while not self.flag:
			ll = []

			self.el.acquire()
			ll = self.lh.ButtonStateXY()
			self.el.release()

			if(len(ll) != 0):
				if ll[0] == 0 and ll[1] == 0 and ycoord < YMAX: # up
					ycoord += 1

				elif ll[0] == 0 and ll[1] == 1 and ycoord > YMIN: #down
					ycoord -= 1

				elif ll[0] == 0 and ll[1] == 2 and xcoord > XMIN: # izquierda
					xcoord -= 1

				elif ll[0] == 0 and ll[1] == 3 and xcoord < XMAX: # derecha
					xcoord += 1