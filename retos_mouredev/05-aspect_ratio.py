from PIL import Image
import requests
from io import BytesIO
import sys

def simplify_fraction(numerator, denominator):
    i = 2
    while i < numerator and i < denominator:
        #print(i, ":", end=" ")
        if numerator % i == 0 and denominator % i == 0:
            numerator = numerator // i
            denominator = denominator // i
            #print(numerator, ", ", denominator, end="")
        else:
            i += 1
        #print()
    return numerator, denominator

url = sys.argv[1]
response = requests.get(url)
img = Image.open(BytesIO(response.content))
print("Image size:", img.width, "x", img.height)
ratio = simplify_fraction(img.width, img.height)
print("Aspect ratio:", ratio[0], ":", ratio[1])
