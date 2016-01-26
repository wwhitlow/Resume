from Myro import *
#init()
p = takePicture()
def imageCleanUp(p):
    for x in range(0,500): #HORIZONTAL LINE TEST2
        for y in range(0,500):
             pix = getPixel(p,x,y)
             green = getGreen(pix)
             if green > 50:
                setGreen(pix,0)
                setBlue(pix,0)
                setRed(pix,0)
    return p
pic = imageCleanUp(p)
show(pic)
def imageProcessing(picture):
   width = 10
   btotal = 0
   rtotal = 0
   gtotal = 0
   start = 0
   while width < 200:
     for x in range(10,15): #HORIZONTAL LINE TEST
        for y in range(start,width):
             pix = getPixel(p,x,y)
             blue = getBlue(pix)
             red = getRed(pix)
             green = getGreen(pix)
             btotal = btotal + blue
             rtotal = rtotal+red
             gtotal = gtotal+green
             if btotal - gtotal > 1000 and btotal - rtotal >  1000:
                turnLeft(1,1)
                turnRight(1,1)
                beep(2,800)
                wait(2)
                beep(2,1600)
                return None
             if rtotal - gtotal > 1000 and rtotal - btotal > 1000:
                turnLeft(1,1)
                turnRight(1,1)
                beep(1,800)
                return None
     for x in range(200,205): #HORIZONTAL LINE TEST2
        for y in range(start,width):
             pix = getPixel(p,x,y)
             blue = getBlue(pix)
             red = getRed(pix)
             green = getGreen(pix)
             btotal = btotal + blue
             rtotal = rtotal+red
             gtotal = gtotal+green
             if btotal - gtotal > 1000 and btotal - rtotal >  1000:
                turnLeft(1,1)
                turnRight(1,1)
                beep(2,800)
                wait(2)
                beep(2,1600)
                return None
             if rtotal - gtotal > 1000 and rtotal - btotal > 1000:
                turnLeft(1,1)
                turnRight(1,1)
                beep(1,800)
                return None
        start = width
        width = width + 10
   width = 10
   start = 0
   while width < 250:
      for x in range(start,width): #Vertical LINE TEST2
       for y in range(210,215):
             pix = getPixel(p,x,y)
             blue = getBlue(pix)
             red = getRed(pix)
             green = getGreen(pix)
             btotal = btotal + blue 
             rtotal = rtotal + red
             gtotal = gtotal + green
             if btotal - gtotal > 2500 and btotal - rtotal >  2500:
                forward(1,1)
                backward(1,1)
                beep(2,800)
                wait(2)
                beep(2,1600)
                return None
             if rtotal - gtotal > 2500 and rtotal - btotal > 2500:
                forward(1,1)
                backward(1,1)
                beep(1,800) 
                return None
      for x in range(start,width): #Vertical LINE TEST
       for y in range(10,15):
             pix = getPixel(p,x,y)
             blue = getBlue(pix)
             red = getRed(pix)
             green = getGreen(pix)
             btotal = btotal + blue
             rtotal = rtotal+red
             gtotal = gtotal+green
             if btotal - gtotal > 2500 and btotal - rtotal >  2500:
                forward(1,1)
                backward(1,1)
                beep(2,800)
                wait(2)
                beep(2,1600)
                return None
             if rtotal - gtotal > 2500 and rtotal - btotal > 2500:
                forward(1,1)
                backward(1,1)
                beep(1,800)
                return None  
      start = width
      width = width + 10   
    #COUNT BLUE AND RED PIXELS PER SAY AND THEN FIGURE OUT WHICH IS HIGHER
    #TO FIND THE  ORIENTATION
    #FOR HORIZONTAL LOOK AT THE SQUARES TO DETERMINE WHICH ONES HAVE COLOR
    #MULTIPLE FUNCTIONS FOR ALL THE TESTS
