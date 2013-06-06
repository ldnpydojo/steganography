from PIL import Image
import numpy
import bitify


def encode(in_file, secret_data, out_file):
    img = Image.open(in_file)
    data = numpy.asarray(img)
    h, w, channels = data.shape

    data = data.reshape(h * w * channels)
    data = list(data)

    for i in range(len(data)):
        data[i] = data[i] & 0b11111110

    for i,x in enumerate(secret_data):
        data[i] = data[i] | x

    data = numpy.array(data, dtype=numpy.uint8).reshape(h, w, channels)
    Image.fromarray(data).save(out_file)


def decode(in_file):
    img = Image.open(in_file)
    data = numpy.asarray(img)
    h, w, channels = data.shape

    data = data.reshape(h * w * channels)
    data = list(data)

    for x in data:
        yield x & 0b00000001


if __name__ == "__main__":
    secret_data = bitify.bitify('that\'s very secret, don\'t look')
    encode("image1.jpg", secret_data, "image2.png")

    print bitify.unbitify(decode("image2.png"))
