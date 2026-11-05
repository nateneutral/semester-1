import timeit
from image1D import Image
i = Image()

#print(timeit.timeit('i.read("../../images/plus.pgm")', setup = 'from image 1D import Image; i=Image()'))
#print(timeit.timeit('char in text', setup='text = "sample string"; char = "g"'))
print(timeit.timeit("Image.read('plus.pgm')", setup = "from image1D import Image"))