import sys
from wand.image import Image
from wand.color import Color

# Calculate perceived brightness then draw plot

# image -> Calculate perceived birghtness -> brightness number, phase (how will i get phase?)
# Calculate perceived brightness: convert to grayscale (done), access pixel color value (done), add brightness value of each pixel(done), normalize(done), calc average of brightness(done)

# Draw plot:

with Image(filename='renders/cube/0001.jpg') as img:
    img.type = 'grayscale';
    img.save(filename='renders/cube/gr0001.jpg');
    print(img.width);
    print(img.height);

    pixels = img.width * img.height;
    total_sum = 0;
    i = 0;
    j = 0;

    for i in img:
        for j in i:
            total_sum += j.blue;        # all the colors are the same anyway, we are in grayscale
            print(j.blue);
            sys.stdin.read(1);
            
    print(total_sum);

    brightness = total_sum / pixels;
