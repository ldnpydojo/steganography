from PIL import Image
import numpy


def encode(in_file, secret_data, out_file):
    img = Image.open(in_file)
    data = numpy.asarray(img)
    h, w, channels = data.shape

    data = data.reshape(h * w * channels)
    data = list(data)

    for i in range(len(data)):
        data[i] = data[i] & 0b11111110

    for i in range(len(secret_data)):
        data[i] = data[i] | secret_data[i]

    data = numpy.array(data, dtype=numpy.uint8).reshape(h, w, channels)
    Image.fromarray(data).save(out_file)


def decode(in_file):
    img = Image.open(in_file)
    data = numpy.asarray(img)
    h, w, channels = data.shape

    data = data.reshape(h * w * channels)
    data = list(data)

    for i in range(len(data)):
        yield data[i] & 0b00000001


if __name__ == "__main__":
    secret_data = [0,1,0,1,1,1,1,1,0,0,0,1,0,1,1,1,0]
    print secret_data
    encode("image1.jpg", secret_data, "image2.png")

    print list(decode("image2.png"))[:len(secret_data)]
