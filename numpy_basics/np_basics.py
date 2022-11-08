# Alternative to Python List: NumPy Array
# numpy is great for doing vector arithmetic
# NumPy arrays is for only one type

# Import the numpy package as np
import numpy as np

# Python list
height_cm = [180, 215, 210, 210, 188, 176, 209, 200]
weight_kg = [100, 90, 90, 90, 78, 76, 109, 65]

# Create a numpy array from list
np_height_m = np.array(height_cm) / 100
np_weight_kg = np.array(weight_kg)

# Print out np.array
print(type(height_cm), height_cm) 
print(type(np_height_m), np_height_m)   # <class 'numpy.ndarray'> [180 215 210 210 188 176 209 200]

# Calculate bmi
bmi = np_weight_kg / (np_height_m ** 2)
print(type(bmi), bmi) 

# Create a boolean numpy array: the element should be True if the corresponding BMI is below 21. 
light = bmi < 21

# Print out light
print(type(light), light) 

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])


# NumPy Side Effects
# Python lists and numpy arrays sometimes behave differently, i.e. plus operator (+)
# numpy arrays cannot contain elements with different types. 
# If you try to build such a list, some of the elements' types are changed to end up with a homogeneous list. 
# This is known as type coercion.
x = np.array([True, 1, 2]) + np.array([3, 4, False])    
print(x)        # [4, 5, 2]


# A list of lists
# mid1, mid2, final
grades = [[80, 78.4, 10],[90, 92.7, 10],[55, 68.5, 20],[100, 98.5, 20],[70, 75.2, 100]]

# Import numpy
import numpy as np

# Create a 2D numpy array from python list
np_grades = np.array(grades)
print(np_grades.shape)      # (5, 3)  - (rows, colums)
print(np_grades) 

# print grades of first student
print( np_grades[0, :])     # [80.  78.4 90. ]

# print final grades    (third column)
print(np_grades[:, 2])      # [90. 88. 60. 95. 80.]


# BASIC STATISTICS
mean = np.mean(np_grades[:, 2])        # [:, 2] -> (all rows,) second column
median = np.median(np_grades[:, 2])
std = np.std( np_grades[:, 2])

print(f"Final Statistics")
print(f"{mean=} {median=} {std=}")

# Generate data
height = np.round( np.random.normal(1.75, 0.2, 5000), 2 )
weight = np.round( np.random.normal(60.33, 15, 5000), 2 )
np_city = np.column_stack((height, weight))
# print(np_city)
print("City Statistics")
print("Average weight:", np.mean(np_city[:, 1]))



