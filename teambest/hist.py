from PIL import Image
import numpy
import bitify

def hist(in_file):
    img = Image.open(in_file)
    data = numpy.asarray(img)
    h, w, channels = data.shape

    data = data.reshape(h * w * channels)
    vals, _ = numpy.histogram(data)
    print " ".join(str(x) for x in vals)



hist("image1.jpg")
hist("image2.png")
hist("image2_obvious.png")
