from PIL import Image
from PIL import ImageFilter

angel = Image.open("1.png")
print(angel.size)
print(angel.format)

area = (340, 0, 1050, 768)#first two parameters are top left corner coordinates, last two are for bottom right corner
cropped_angel = angel.crop(area)#saving cropped image in new image

#combining two images together #pasting one image on another
adam = Image.open("4.png")
area2 = (0, 0, 710, 768)
adam.paste(cropped_angel, area2)#pasting cropped angel on adam
#adam.show()#opens up image

#breaking up an image into individual channels
red_spot = Image.open("5.png")
print(red_spot.mode)
r, g, b = red_spot.split()#returns a tuple with three values
#r.show()
#g.show()
#b.show()
new_img = Image.merge("RGB", (g, r, b))#gives different result for different order of r, g and b
#new_img.show()

#merging images
r2, g2, b2 = angel.split()
merged_img = Image.merge("RGB", (r2, g, b))#merging two images together
#merged_img.show()

#resizing image
square_spot = red_spot.resize((500, 500))#resizes the image to 500 x 500
#square_spot.show()

#flipping image
flip_spot = red_spot.transpose(Image.FLIP_LEFT_RIGHT)#flips image horizontally
flip_spot_2 = red_spot.transpose(Image.FLIP_TOP_BOTTOM)#flips image vertically
#flip_spot.show()
#flip_spot_2.show()

#spinning image
spin_spot = red_spot.transpose(Image.ROTATE_90)
#spin_spot.show()

#converting image modes
bnw = red_spot.convert("L")#L stands for black and white
cmyk = red_spot.convert("CMYK")#Cyan, Magenta, Yellow, Black
#bnw.show()
#cmyk.show()

#using image filters
blur = red_spot.filter(ImageFilter.BLUR)
#blur.show()
detail = red_spot.filter(ImageFilter.DETAIL)
#detail.show()
edges = red_spot.filter(ImageFilter.FIND_EDGES)
#edges.show()