import cv2
import numpy as np

img = cv2.imread('../img/blank_500.jpg')

colors = {'black':(0,0,0),
         'red' : (0,0,255),
         'blue':(255,0,0),
         'green': (0,255,0)}

title = 'name tag'

insertColor = 'blue'
textColor = 'black'

count = 0
textCount = 0

def makeNameTag(insertColor, textColor):

    color = colors[insertColor]
    color2 = colors[textColor]
    cv2.rectangle(img, (80, 50), (390, 150), color, 10)        
    cv2.ellipse(img, (80, 100), (50, 50), 90, 0, 180, color, 10)
    cv2.ellipse(img, (390, 100), (50, 50), 270, 0, 180, color, 10)      
    cv2.putText(img, "Chae Seunghoon", (100, 110), cv2.FONT_HERSHEY_DUPLEX, 1, color2)  
    pts1 = np.array([[80,50], [150,10], [235,50], [320,10], [390,50]], dtype=np.int32) 
    cv2.polylines(img, [pts1], False, color, 10)

    cv2.imshow(title, img)

makeNameTag(insertColor, textColor)

def onMouse(event, x, y, flags, param):
    global count
    global textColor
    global textCount
    if event == cv2.EVENT_LBUTTONDOWN:
        if flags & cv2.EVENT_FLAG_CTRLKEY :
            textCount += 1
            if (textCount%2) == 1:
                textColor = 'green'
            else:
                textColor = 'black'
        count += 1
        if (count % 3) == 1:
            insertColor = 'green'
        elif (count % 3) == 2:
            insertColor = 'red'
        elif (count % 3) == 0:
            insertColor = 'blue'
        makeNameTag(insertColor, textColor)

cv2.setMouseCallback(title, onMouse)

while True:
    if cv2.waitKey(0) & 0xFF == 27:
        break
cv2.destroyAllWindows()
