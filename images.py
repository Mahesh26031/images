# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 10:18:47 2021

@author: Mahesh B
"""

from PIL import Image,ImageFilter
img=Image.open('./pokemon/pikachu.jpg')
print(img.format)
print(img.size)
print(img.mode)

a=img.filter(ImageFilter.BLUR)
a.save("blur.png",'png')

b=img.convert('L')
b.save("L.png",'png')

c=img.rotate(90)
c.save("rotate.png",'png')

d=img.resize((300,300))
d.save("resize.png",'png')

box=(100,100,400,400)
e=img.crop(box)
e.save("crop.png",'png')

img2=Image.open('./pokemon/astro.jpg')
print(img2.size)
img2.thumbnail((400, 200))
img2.save("thumbnail.png",'png')

img3=Image.open('./pokemon/squirtle.jpg')
img3.save("covertjpgtopng.png")



import os
directory = r'C:\Users\Mahesh B\OneDrive\Desktop\projects udemy\scripting\image'
c=1
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        im = Image.open(filename)
        name='img'+str(c)+'.png'
        im.convert('RGB')
        im.save(name)
        c+=1
        print(os.path.join(directory, filename))
        continue
    else:
        continue
