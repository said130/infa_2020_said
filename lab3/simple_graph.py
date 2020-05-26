from graph import *
"""Draw siple picture
"""


brushColor("yellow") #Draw an oval face
circle(250, 250, 100)

brushColor("black") #Draw a mouth
rectangle(200, 300, 300, 320)

brushColor("red") #Draw the left red eye
circle(200, 230, 20)

brushColor("red") #Draw right red eye
circle(300, 230, 15)

brushColor("black") #Draw left black eye
circle(200, 230, 8)

brushColor("black") #Draw right black eye
circle(300, 230, 7)

brushColor("black") #Draw left eyebrow
polygon([(155, 165), (230, 210), (225, 220), (150, 175)])

brushColor("black") #Draw right eyebrow
polygon([(350, 170), (270, 220), (275, 225), (350, 175)])

run()
