#CODED BY : Md Zahidul Islam ,Undergrad, CSE, IUT
import cv2
import numpy as np 

windowName = 'PAINT'
img = np.zeros((512,1024,3),np.uint8)
cv2.namedWindow(windowName)

#true if mouse is pressed
mousePressed = False
#true if mode is rectangle 
isRectangle = True
color = (0,0,0)

def emptyFunc():
    pass

#mouse callback function 
def draw_shape(event,x,y,flags,param):
    global ix,iy,drawing,mode,color
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        (ix,iy) = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if isRectangle == True:
                cv2.rectangle(img, (ix,iy), (x,y) ,color,-1)
            else:
                cv2.circle(img , (x,y), 3, color, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix,iy),(x,y),color,-1)
        else: 
            cv2.circle(img,(x,y),3,color,-1)
            
cv2.setMouseCallback(windowName, draw_shape)
cv2.createTrackbar('Blue',windowName,0,255,emptyFunc)
cv2.createTrackbar('Green',windowName,0,255,emptyFunc)
cv2.createTrackbar('Red',windowName,0,255,emptyFunc)
def main():
    global isRectangle
    global color
    while(True):
        cv2.imshow(windowName,img)
        if(isRectangle == True):
                
                text1 = " Drawing Rectangles."
                text2=" Press 'M' to switch to PaintBrush."
                cv2.rectangle(img,(0,0),(512,100),(0,0,0),-1)
                cv2.rectangle(img,(800,25),(850,75),color,-1)
                cv2.putText(img, text1,(25,25),cv2.FONT_HERSHEY_SIMPLEX,.5,(255,255,255 ))
                cv2.putText(img, text2,(25,50),cv2.FONT_HERSHEY_SIMPLEX,.5,(255,255,255 ))
        else:
                
                text1 = " Drawing with PaintBrush."
                text2=" Press 'M' to draw Rectangles." 
                cv2.rectangle(img,(0,0),(512,100),(0,0,0),-1)
                cv2.rectangle(img,(800,25),(850,75),color,-1)
                cv2.putText(img, text1,(25,25),cv2.FONT_HERSHEY_SIMPLEX,.5,(255,255,255 ))
                cv2.putText(img, text2,(25,50),cv2.FONT_HERSHEY_SIMPLEX,.5,(255,255,255 ))
        k = cv2.waitKey(1)
        if k==ord('m') or k==ord('M'):
            if(isRectangle == False):
                isRectangle = True
               
            else:
                isRectangle = False
           
        elif k == 27:
            break
        blue = cv2.getTrackbarPos('Blue',windowName)
        red = cv2.getTrackbarPos('Red',windowName)
        green = cv2.getTrackbarPos('Green',windowName)
        color = (blue,green,red)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()
    