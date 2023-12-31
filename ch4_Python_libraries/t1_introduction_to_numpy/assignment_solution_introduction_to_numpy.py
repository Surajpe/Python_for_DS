# -*- coding: utf-8 -*-
"""Assignment Solution - Introduction to NumPy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kwDyUDhY2LvcZa9jPpH-COvRVjZ_gDGc

# <u>**Problem 1**</u>

### Construct a 2-D 10*10 matrix with the following constraints:

*  ####  The element at [0,0] should be 1
*  ####   The element at [0,9] should be 100
* ####   The element at [9,0] should be 50
* ####   The interval between elements in rows should be constant
* ####   The interval between elements in columns should be constant
"""

# Your code here
import numpy as np
rows = np.linspace(1,50,10)
lists=[]
for i in rows:
    lists.append(np.linspace(i,i+99,10))

# for each of these elements in first row creating linearly separated values in column
array=np.around(np.array(lists).reshape(10,10),1)
array

"""#<u>**Problem 2**</u>

### Construct a 2-D 10*10 matrix with the diagonal elements equal to zero and all the other elements equal to 1
"""

import numpy as np
#method 1
x = np.ones((10, 10), dtype=int)
for i in range(len(x)):
  for j in range(len(x[i])):
    if i==j:
      x[i,j] = 0
print(x)

"""# <u>**Problem 3**</u>

### Construct a list of first 100 natural numbers. Find the square of each number and output that in the form of another list containing 10 lists each.

"""

import numpy as np
size = 100
L = [num**2 for num in range(1,size+1,1)]
A = np.asarray(L)
A.shape = (10,10)
print(A)

"""#<u>**Problem 4**</u>

### You are given an image below. Experiment with the numpy slice operation to only get the face of the person in the image
"""

# Importing data from the skimage library. Don't worry much about it
 from skimage import data
 camera = data.camera()

# Camera is 2-D array object
camera.shape

camera

# You can plot the camera object and see the image
import matplotlib.pyplot as plt
plt.imshow(camera)

# Perform your slice operation here to get the face of the person
camera_slice = camera[75:160,180:265]
plt.imshow(camera_slice)

