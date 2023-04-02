"""
The NumPy ndarray: A Multidimensional Array Object
One of the key features of NumPy is its N-dimensional array object, or ndarray, which is a fast, flexible container for large datasets in Python. 
Arrays enable you to perform mathematical operations on whole blocks of data using similar syntax to the equivalent operations between scalar elements.
Yani, tekil sayilar uzerinde islem yapar gibi bir syntax ile sayi dizileri uzerinde islem yapabiliyoruz.

An ndarray is a generic multidimensional container for "homogeneous" data; that is, all of the elements must be the same type. 
Every array has a shape, a tuple indicating the size of each dimension, and a dtype, an object describing the data type of the array

Arithmetic with NumPy Arrays
Arrays are important because they enable you to express batch operations on data without writing any for loops. 
NumPy users call this "vectorization". Any arithmetic operations between equal-size arrays applies the operation element-wise.

"""

# Import the numpy package as np
import time
import numpy as np


def compare_time():
    # NumPy-based algorithms are generally 10 to 100 times faster (or more) than their pure Python counterparts and use significantly less memory.
    # To give you an idea of the performance difference,
    # consider a NumPy array of one million integers, and the equivalent Python list, and multiply each sequence by 2:

    my_arr = np.arange(1_000_000)
    my_list = list(range(1_000_000))

    # Measure the starting time
    start_cpu = time.process_time()
    start_real = time.time()

    for _ in range(10):
        my_arr2 = my_arr * 2

    end_cpu = time.process_time()
    end_real = time.time()

    elapsed_cpu = end_cpu - start_cpu
    elapsed_real = end_real - start_real

    print("Numpy array time: ")
    print(f"Elapsed CPU time: {elapsed_cpu} seconds")
    print(f"Elapsed real time: {elapsed_real} seconds")

    # Measure the starting time
    start_cpu = time.process_time()
    start_real = time.time()

    for _ in range(10):
        my_list2 = [x * 2 for x in my_list]

    end_cpu = time.process_time()
    end_real = time.time()

    elapsed_cpu = end_cpu - start_cpu
    elapsed_real = end_real - start_real

    print("Python list time: ")
    print(f"Elapsed CPU time: {elapsed_cpu} seconds")
    print(f"Elapsed real time: {elapsed_real} seconds")


def simple_nd():
    print("N-Dimensional (Nested) Lists")
    print("----------------------------")

    """
               Math  Sci  Hist  Econ
     Harry       60   70    80    90
     Ron         65   75    85    95
     Hermione    69   79    89    99

    """

    # 1d python lists:
    # no labels in the data structure, names of lists (kind of) represents row indexes:
    scores_harry = [60, 70, 80, 90]
    scores_ron = [65, 75, 85, 95,]
    scores_hermione = [69, 79, 89, 99]

    # create ndarray form python lists:
    np_harry = np.array(scores_harry)
    np_ron = np.array(scores_ron)
    np_hermione = np.array(scores_hermione)

    print(f"{np_harry=}, {np_harry.shape=}")    # array([60, 70, 80, 90]), np_harry.shape=(4,)

    # 2d list, as a collection of lists:  [ list, list, list ]
    # Shape is (rows, columns)
    scores_Hogwarts = [scores_harry, scores_ron, scores_hermione]
    scores_Beauxbatons = [[70, 71, 72, 73], [80, 81, 82, 83], [90, 91, 92, 93]]
    scores_Durmstrang = [[20, 21, 22, 23], [30, 31, 32, 33], [40, 41, 42, 43]]

    # create ndarray form python nested (2D) list: (list of lists)
    np_Hogwarts = np.array(scores_Hogwarts)
    np_Beauxbatons = np.array(scores_Beauxbatons)
    np_Durmstrang = np.array(scores_Durmstrang)

    print(f"{np_Hogwarts=}, {np_Hogwarts.shape=}")
    """
     array([[60, 70, 80, 90],
          [65, 75, 85, 95],
          [69, 79, 89, 99]])
    """

    # 3d list, as a list of 2d lists. [ 2dlist, 2dlist ]
    # 3D lists are List of Lists of Lists.
    # In other words, they are List of martices (tables) - where each matrix is a list of lists.)
    # 3 okuldaki 3'er ogrencinin 4'er dersten notları - 3D
    scores_all_schools = [scores_Hogwarts, scores_Beauxbatons, scores_Durmstrang]

    # create ndarray form python nested (3D) list:
    np_all_schools = np.array(scores_all_schools)

    print(f"{np_all_schools=}")
    """
    array([[[60, 70, 80, 90],
            [65, 75, 85, 95],
            [69, 79, 89, 99]],

           [[70, 71, 72, 73],
            [80, 81, 82, 83],
            [90, 91, 92, 93]],

           [[20, 21, 22, 23],
            [30, 31, 32, 33],
            [40, 41, 42, 43]]])
    """

    # IN SUMMARY,
    # 1D Lists are like rows
    # 2D Lists are list of like tables, or matrices.
    # 3D Lists are like list of tables.

    # Option 2A - Think in terms of a dictionary
    # A dictionary where keys are the "column names" and values are the lists:
    # Note that column names are visible in this version. (vs. nested lists)
    names = ['Harry', 'Ron', 'Hermione']
    math = [60, 65, 69]
    sci = [70, 75, 79]
    hist = [80, 85, 89]
    econ = [90, 95, 99]

    scores_Hogwarts_dict = {'Name': names, 'Math': math, 'Sci': sci, 'Hist': hist, 'Econ': econ}

    print(scores_Hogwarts_dict)
    """
    {
     'Name': ['Ron', 'Harry', 'Hermione'], 
     'Math': [65, 60, 69], 
     'Sci': [65, 60, 69], 
     'Hist': [65, 60, 69], 
     'Econ': [65, 60, 69]
     }
    """

    # Option 2B - Think in terms of a dictionary
    # A dictionary with keys = row indexes an values are dictionaries where keys are columnnames:
    scores_gryffindor_rowindexaskey = {
        'Harry': {
            'Math': 60,
            'Sci': 70,
            'Hist': 80,
            'Econ': 90
        },
        'Ron': {
            'Math': 65,
            'Sci': 75,
            'Hist': 85,
            'Econ': 95
        },
        'Hermione': {
            'Math': 69,
            'Sci': 79,
            'Hist': 89,
            'Econ': 99
        }
    }


compare_time()
simple_nd()

# Creating ndarrays
# 1. The easiest way to create an array is to use the array() function. This accepts any sequence-like object(including other arrays)
# and produces a new NumPy array containing the passed data:
numbers = [1, 2, 3, 4, 5]
np_numbers = np.array(numbers)

print(f"{numbers=}")        # [1, 2, 3, 4, 5]
print(f"{np_numbers=}")     # array([1, 2, 3, 4, 5])

# In addition to np.array(), there are a number of other functions for creating new arrays.
# 2. zeros() and ones() create arrays of 0s or 1s, respectively, with a given length or shape.
# empty creates an array without initializing its values to any particular value
scores = np.zeros(shape=10)       # given length - array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
scores2 = np.ones(shape=(3, 6))   # given shape -
'''
array([[1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1.]])
'''
print(f"{scores=}")
print(f"{scores2=}")

# 3. full() produces an array of the given shape and dtype with all values set to the indicated “fill value”
scores3 = np.full(shape=(2, 4), fill_value=-1)
print(f"{scores3=}")
"""
array([[-1, -1, -1, -1],
       [-1, -1, -1, -1]])
"""

# 4. arange() is an array-valued version of the built-in Python range function:
g7 = np.arange(7)   # array([0, 1, 2, 3, 4, 5, 6])
print(f"{g7=}")

# 5. Generate a 3x4 array of random numbers from a standard normal distribution (mean 0 and standard deviation 1)
arr_rand_1 = np.random.randn(5)  # array([-0.20175391, -0.87452102,  1.21002324,  0.45234304, -1.2349739])
print(f"{arr_rand_1=}")

mu, sigma = 70, 10  # mean and standard deviation
samples = np.random.normal(mu, sigma, size=(3, 4))
print(f"{samples=}")
"""
array([[64.1577162 , 60.43640588, 98.0346746 , 52.98271233],
       [80.02077676, 71.77543143, 67.09012764, 65.35728612],
       [73.67353157, 71.38648497, 75.87520192, 74.16910517]])
"""

# Arithmetic with NumPy Arrays
# Arrays are important because they enable you to express batch operations on data without writing any for loops.
# NumPy users call this "vectorization". Any arithmetic operations between equal-size arrays applies the operation element-wise.
# Arithmetic operations with scalars propagate the scalar argument to each element in the array:

height_cm = [180, 215, 210, 210, 188]
weight_kg = [100, 90, 90, 90, 78]

# Create a numpy array from list and divide by a scalar
np_height_m = np.array(height_cm) / 100
np_weight_kg = np.array(weight_kg)

# Print out np.array
print(type(height_cm), height_cm)       # <class 'list'> [180, 215, 210, 210, 188]
print(type(np_height_m), np_height_m)   # <class 'numpy.ndarray'> [1.8  2.15 2.1  2.1  1.88]

# Calculate bmi
# mathematical operations on whole blocks of data using similar syntax to the equivalent operations between scalar elements:
bmi = np_weight_kg / (np_height_m ** 2)
print("BMI", type(bmi), bmi)

# Comparisons between arrays of the same size yield boolean arrays.
# Compare two NumPy arrays element-wise:
# Example 1
grades_std1 = np.array([70, 80, 90, 80, 60, 70])
grades_std2 = np.array([65, 95, 65, 85, 55, 75])

comp = grades_std1 > grades_std2    # Note the operands: NDArray > NDArray
print("Is std1 greater than std2?:", comp)  # [True False True False True False]

# Example 2
# Create a boolean numpy array: the element should be True if the corresponding BMI is below 21.
light = bmi < 21

# Print out light
print("LIGHT", type(light), light)

# Filter:
# Print out BMIs of all baseball players whose BMI is below 21
# print(bmi[light])
print("bmi[bmi<21]", bmi[bmi < 21])

# Example 3
# Compare two NumPy arrays element-wise.
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# Which areas in my_house are smaller than the ones in your_house?
print("Compare arrays:", my_house[my_house < your_house])


# Indexing elements in a NumPy array
# same as python nested lists, like 2d matrix
# the elements of the list are lists themselves - Each inner list is like a row
arr2d = np.array([[10, 11, 12], [20, 21, 22], [30, 31, 32]])    # [row0, row1, row2] where row0 is [10, 11, 12]
print(f"{arr2d[1]=}")       # array([20, 21, 22])   - the elements of the list are lists themselves. Each inner list is like a row
print(f"{arr2d[0][2]=}")    # =12

# Two-dimensional array slicing
"""
        +---+---+---+
   row0 |   | x | x |   rows 0 and 1, columns 1 and 2
        +---+---+---+
   row1 |   | x | x |   [:2, 1:]
        +---+---+---+
   row2 |   |   |   |
        +---+---+---+


        +---+---+---+
   row0 |   |   |   |   row3 (and all columns)
        +---+---+---+
   row1 |   |   |   |   [2:, :]
        +---+---+---+
   row2 | x | x | x |
        +---+---+---+

    
        +---+---+---+
   row0 | x | x |   |   (all rows and) columns 0 and 1
        +---+---+---+
   row1 | x | x |   |   [:, :2]
        +---+---+---+
   row2 | x | x |   |
        +---+---+---+
"""

# Reshaping and Transposing Arrays:

"""
Lets say we have data on grades:

std     math    sci     hist    econ    eng
mike    90      91      92      93      94
sam     70      71      72      73      74
joe     80      81      82      83      84
"""

# allscores = np.arange(15)
allscores = np.array([90,  91,  92,  93,  94,  70,  71,  72,  73,  74, 80,  81,  82,  83,  84])
print(f"{allscores=}")

# lets reshape this array on 3 students (rows) and 5 courses (columns)
arr_2d = allscores.reshape((3, 5))
print(f"{arr_2d=}")
"""
array([[90, 91, 92, 93, 94],
       [70, 71, 72, 73, 74],
       [80, 81, 82, 83, 84]])
"""

# Lets transpose this table (2d array)
# which simply means, switch column labels with row labels:
"""
course  mike    sam     joe
math    90      70      80
sci     91      71      81
hist    92      72      82
econ    93      73      83
eng     94      74      84

"""
arr_2d_transposed = arr_2d.T
print(f"{arr_2d_transposed=}")
"""
array([[90, 70, 80],
       [91, 71, 81],
       [92, 72, 82],
       [93, 73, 83],
       [94, 74, 84]])
"""


# NumPy Side Effects
# Python lists and numpy arrays sometimes behave differently, i.e. plus operator (+)
# numpy arrays cannot contain elements with different types.
# If you try to build such a list, some of the elements' types are changed to end up with a homogeneous list.
# This is known as type coercion.
x = np.array([True, 1, 2]) + np.array([3, 4, False])
print(x)        # [4, 5, 2]


# A list of lists
# mid1, mid2, final
grades = [[80, 78.4, 10], [90, 92.7, 10], [55, 68.5, 20], [100, 98.5, 20], [70, 75.2, 100]]

# Import numpy

# Create a 2D numpy array from python list
np_grades = np.array(grades)
print(np_grades.shape)      # (5, 3)  - (rows, colums)
print(np_grades)

# print grades of first student
print(np_grades[0, :])     # [80.  78.4 90. ]

# print final grades    (third column)
print(np_grades[:, 2])      # [90. 88. 60. 95. 80.]


# BASIC STATISTICS
mean = np.mean(np_grades[:, 2])        # [:, 2] -> (all rows,) second column
median = np.median(np_grades[:, 2])
std = np.std(np_grades[:, 2])

print(f"Final Statistics")
print(f"{mean=} {median=} {std=}")

# Generate data
height = np.round(np.random.normal(1.75, 0.2, 5000), 2)
weight = np.round(np.random.normal(60.33, 15, 5000), 2)
np_city = np.column_stack((height, weight))
# print(np_city)
print("City Statistics")
print("Average weight:", np.mean(np_city[:, 1]))


# Random Numbers
# Set the seed
np.random.seed(123)

# Simulate coin flip, 5 rounds:
draws = np.random.randint(low=0, high=2, size=5)      # array([0, 1, 0, 0, 0])
print(f"{draws=}")
