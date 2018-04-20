#!/usr/bin/python3
from PIL import Image, ImageDraw
import numpy as np

# size of image
canvas = (10, 10)

# scale ration
scale = 5
thumb = canvas[0]/scale, canvas[1]/scale

# rectangles (width, height, left position, top position)
#frames = [(50, 50, 5, 5), (60, 60, 100, 50), (100, 100, 205, 120)]
frames = np.random.randint(10, size=(2,3))
print(frames)

# init canvas
#im = Image.new('RGB', canvas, (255, 255, 255))
#draw = ImageDraw.Draw(im)
#print("TEST")
# draw rectangles
i = 0
for frame in frames:

    im = Image.new('RGB', canvas, (255, 255, 255))
    draw = ImageDraw.Draw(im)

    x1, y1, d = frame[0], frame[1], frame[2]
    if (x1+d) > 10:
        x2 = 10
    else:
        x2 = x1+d

    if (y1+d) > 10:
        y2 = 10
    else:
        y2 = y1+d
    print ("x1=",x1," x2=",x2, " d=",d, " i=",i)
    i = i+1
    draw.rectangle(((x1, y1), (x2, y2)), fill="black")
    imgname = "im"+str(i)+".png"
    print ("name",imgname)
    im.save(imgname)
    im.close()

# make thumbnail
#im.thumbnail(thumb)

# save image
#im.save('im.png')
