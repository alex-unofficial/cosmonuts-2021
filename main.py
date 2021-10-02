import sys
import numpy as np
from wand.image import Image
from wand.color import Color

# Calculate perceived brightness then draw plot

# image -> Calculate perceived birghtness -> brightness number, phase (how will i get phase?)
# Calculate perceived brightness: convert to grayscale (done), access pixel color value (done), add brightness value of each pixel(done), normalize(done), calc average of brightness(done)

# Draw plot:
def calculate_brightness(filename):
    with Image(filename='renders/cube/' + filename) as img:
        img.type = 'grayscale';
        #img.save(filename='gr0001.jpg');
        #print(img.width);
        #print(img.height);

        pixels = img.width * img.height;
        total_sum = 0;
        i = 0;
        j = 0;

        for i in img:
            for j in i:
                total_sum += j.blue;        # all the colors are the same anyway, we are in grayscale
                #print(j.blue);
                #sys.stdin.read(1);
                

        brightness = total_sum / pixels;

        #print(brightness);

        return brightness;


cube=""

for i in range(1, 81):
    print("index: " + f"0{i:03}.png")
    print(calculate_brightness(f"0{i:03}.png"))

