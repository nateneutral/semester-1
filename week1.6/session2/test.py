from image import Image
import timeit

i = Image()

print(timeit.timeit("Image.read('images/coins.pgm')", setup = "from image import Image;"))
