import gtk.gdk
import cv2
from cv2 import cv
import numpy as np
from pymouse import PyMouse
import time

m = PyMouse()

def getimgpos(im1, im2):
	needle = cv2.imread(im1)
	haystack = cv2.imread(im2)
	
	result = cv2.matchTemplate(needle,haystack,cv2.TM_CCOEFF_NORMED)
	y,x = np.unravel_index(result.argmax(), result.shape)
	width, height,ch = needle.shape
	return x+width/2,y+height/2
	
while True:
	#get screenshot
	w = gtk.gdk.get_default_root_window()
	sz = w.get_size()
	pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
	pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
	pb.save("basketball_ss.png","png")
	
	#get positions of "things"
	x,y = getimgpos("basketball_hoop.png", "basketball_ss.png")
	ballx,bally = getimgpos("basketball_ball.png", "basketball_ss.png")
	mousex,mousey = m.position()
	
	print("Mouse position: " + str((mousex,mousey)))
	print("Ball position: " + str((ballx,bally)))
	print("Hoop position: "+str((x,y)))
	
	#calculate new hoop position (it's 3d-like, so you need to calculate angles. this code is dummy, but it works)
	offset = abs(ballx - x)
	if ballx > x:
		x += offset / 2
	else:
		x -= offset / 2
	
	print("Fixed hoop position: "+str((x,y)))

	#press at ball pos, move partially to the target (hoop) and release it
	m.press(ballx,bally)
	m.move(x - ballx / 3, y - bally / 3)
	m.move(x - ballx / 2, y - bally / 2)
	m.release(x,y)
	
	#wait until ball goes into hoop
	time.sleep(3)
