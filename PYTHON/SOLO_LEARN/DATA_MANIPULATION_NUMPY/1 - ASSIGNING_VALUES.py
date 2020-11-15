#DATA_MANIPULATION_NUMPY_ASSIGNING_VALUES

import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]
heights_arr = np.array(heights)
print("HEIGHTS :\n",heights_arr)
print("\nSHAPE_HEIGHTS :\n",heights_arr.shape)

ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]
ages_arr = np.array(ages)
print("\nAGES :\n",ages_arr)
print("\nSHAPE_AGES :\n",ages_arr.shape)

#Assigning Single Values 1.1
heights_arr[3] = 165
print("\nOPTION_1_HEIGHTS_ARRAY :\n\n",heights_arr)

#Assigning Single Values 1.2
heights_and_ages = heights + ages 
heights_and_ages_arr = np.array(heights_and_ages)
heights_and_ages_arr = heights_and_ages_arr.reshape((2,45))
heights_and_ages_arr[0, 3] = 165
print("\nOPTION_2_HEIGHTS_AGES_ARRAY :\n\n",heights_and_ages_arr)

#Assigning Single Values 1.3
heights_and_ages_arr[0,:] = 180
print("\nOPTION_3_HEIGHTS_AGES_ARRAY_180_TO_HEIGHTS :\n\n",heights_and_ages_arr)

#Assigning Single Values 1.4
heights_and_ages_arr[:2, :2] = 0
print("\nOPTION_4_HEIGHTS_AGES_ARRAY_0_TO_FIRST_2_HEIGHTS_AGES :\n\n",heights_and_ages_arr)

#Assigning an Array to an Array 2.1
heights_and_ages_arr[:, 0] = [190, 58]
print("\nOPTION_5 :\n\n",heights_and_ages_arr)

#Assigning an Array to an Array 2.2
new_record = np.array([[180, 183, 190], [54, 50, 69]])
heights_and_ages_arr[:, 42:] = new_record
print("\nOPTION_6 :\n\n",heights_and_ages_arr)

#Combining Two Arrays 3.1
print("\nOPTION_7_AGES_ARRAY_FIRST_3_AGES :\n\n",ages_arr[:3,])

#Combining Two Arrays 3.2
heights_arr = heights_arr.reshape((45,1))
ages_arr = ages_arr.reshape((45,1))
height_age_arr = np.hstack((heights_arr, ages_arr))
print("\nOPTION_8 :\n\n",height_age_arr.shape,"\n",height_age_arr[:3,])

#Combining Two Arrays 3.3
heights_arr = heights_arr.reshape((1,45))
ages_arr = ages_arr.reshape((1,45))
height_age_arr = np.vstack((heights_arr, ages_arr))
print("\nOPTION_9 :\n\n",height_age_arr.shape,"\n",height_age_arr[:,:3])

#Concatenate 4.1
heights_arr = heights_arr.reshape((45,1))
ages_arr = ages_arr.reshape((45,1))
height_age_arr = np.hstack((heights_arr, ages_arr))
print("\nRESULT_1 :\n\n",height_age_arr.shape)
height_age_arr = np.concatenate((heights_arr, ages_arr), axis=1)
print("\nRESULT_1_SAME :\n\n",height_age_arr.shape)
print("\nRESULT_1_SLICED :\n\n",height_age_arr[:3,:])

#Concatenate 4.2
heights_arr = heights_arr.reshape((1,45))
ages_arr = ages_arr.reshape((1,45))
height_age_arr = np.vstack((heights_arr, ages_arr))
print("\nRESULT_2 :\n\n",height_age_arr.shape)
height_age_arr = np.concatenate((heights_arr, ages_arr), axis=0)
print("\nRESULT_2_SAME :\n\n",height_age_arr.shape)
print("\nRESULT_2_SLICED :\n\n",height_age_arr[:,:3])
