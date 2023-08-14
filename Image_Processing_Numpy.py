"""
The first assessment in the Udemy 
python for computer vision with opencv and deep learning course
"""
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


#Create a 5x5 array where every value is a 10
arr5x5 = np.ones(shape=(5,5)) * 10
print(arr5x5)

#Create an array of random numbers
np.random.seed(101)
arr = np.random.randint(low=0, high=100, size=(5,5))
print(arr)
print('The largest value = {}'.format(arr.max()))
print('The smallest value = {}'.format(arr.min()))

pic = Image.open('C:\\Computer-Vision-with-Python\\DATA\\00-puppy.jpg')
pic_arr = np.asarray(pic)
print(pic_arr.shape)
plt.imshow(pic_arr)
plt.show()

#Isolate the blue channel
pic_blue = pic_arr.copy()
# Red to zero
pic_blue[:,:,0] = 0
# Green to zero
pic_blue[:,:,1] = 0
plt.imshow(pic_blue)
plt.show()
