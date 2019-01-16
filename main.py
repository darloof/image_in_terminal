from PIL import Image, ImageOps, ImageDraw
from sys import argv
def makeprint(n):
    if (n == 1):
        print(' ', end=' ')
    elif (n == 2):
        print('.', end=' ')
        # print(chr(10625), end=' ')
    elif (n == 3):
        print(chr(11821), end=' ')
    elif (n == 4):
        print(chr(11568), end=' ')
    elif (n == 5):
        print(chr(9967), end=' ')
    elif (n == 6):
        print(chr(10049), end=' ')
    elif (n == 7):
        print(chr(42485), end=' ')
    elif (n == 8):
        print(chr(9673), end=' ')
    elif (n == 9):
        print(chr(11204), end=' ')
#filename = '/home/mohammadreza/w/dice_portrait/image1.jpg'
filename = argv[1]
img = Image.open(filename)
img = ImageOps.grayscale(img)
img = ImageOps.autocontrast(img)


sqw = int(argv[2])
#sqw = 100
sqsize = int(img.width / sqw)
sqh = int(img.height * sqsize / sqw)

for y in range(0, img.height-sqsize, sqsize):
    for x in range(0, img.width-sqsize, sqsize):
        thisSectorColor = 0
        for sqx in range(0, sqsize):
            for sqy in range(0, sqsize):
                thisColor = img.getpixel((x+sqx,y+sqy))
                thisSectorColor += thisColor
        thisSectorColor /= (sqsize ** 2)
        thisSectorNumber = (255 - thisSectorColor) * 9 / 255 + 1
        thisSectorNumber = int(thisSectorNumber)
        makeprint(thisSectorNumber)
    print()
