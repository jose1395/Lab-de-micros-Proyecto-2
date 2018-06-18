import os
from gpiozero import Button
from signal import pause

button = Button(2)
def captura():
	os.system(‘fswebcam –r 320x240 –jpeg 50 save /home/pi/prueba.jpg’)

button.when_pressed = captura

pause()
