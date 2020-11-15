#DATA_MANIPULATION_NUMPY_GETTING_STARTED

import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]

#Numerical Data

cnt = 0
for height in heights:
  if height > 188:
    cnt +=1
print("HEIGHTS_SUM_PLUS_188:",cnt)

#Introduction to Numpy

heights_arr = np.array(heights)
print("\nHEIGHTS_SUM_PLUS_188:",(heights_arr > 188).sum())

#Size and Shape

print("\nHEIGHTS_SIZE:",heights_arr.size)
print("\nHEIGHTS_SHAPE:",heights_arr.shape)

heights_and_ages = heights + ages 
heights_and_ages_arr = np.array(heights_and_ages)
print("\nHEIGHTS_AGE_SHAPE:",heights_and_ages_arr.shape)

#Reshape

print("\nHEIGHTS_AGE_INT_ARRAY:\n\n",heights_and_ages_arr.reshape((2,45)))

#Data Type

print("\nTYPE_HEIGHTS_AGE_INT_ARRAY:",heights_arr.dtype)

heights_float = [189.0, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

heights_float_arr = np.array(heights_float)
print("\nHEIGHTS_FLOAT_ARRAY :\n\n",heights_float_arr)
print("\nTYPE_HEIGHTS_AGE_FLOAT_ARRAY:",heights_float_arr.dtype)
