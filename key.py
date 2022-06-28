import time
import keyboard
while True:
	for i in range(200):
		time.sleep(1)
		keyboard.send('up arrow')
	for i in range(200):
		time.sleep(1)
		keyboard.send('down arrow')