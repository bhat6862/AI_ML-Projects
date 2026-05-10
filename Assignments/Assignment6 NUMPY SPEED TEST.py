'''Assignment (20/02/2026) 
Assignment Name : NumPy Speed Test 
Description : Compare Python lists vs NumPy arrays with 1M numbers, measure execution time, write 3 observations.'''
import time
import numpy as np

# Create 1 million numbers
n = 1000000

# Python List
python_list = list(range(n))

start = time.time()
python_result = [x * 2 for x in python_list]
end = time.time()

python_time = end - start

# NumPy Array
numpy_array = np.arange(n)

start = time.time()
numpy_result = numpy_array * 2
end = time.time()

numpy_time = end - start

# Display execution times
print("Execution Time Comparison")
print("--------------------------")
print("Python List Time :", python_time, "seconds")
print("NumPy Array Time :", numpy_time, "seconds")

'''Execution Time Comparison
--------------------------
Python List Time : 0.0904550552368164 seconds     
NumPy Array Time : 0.010501861572265625 seconds

Execution Time Comparison
--------------------------
Python List Time : 0.08657169342041016 seconds    
NumPy Array Time : 0.005677223205566406 seconds 

Execution Time Comparison
--------------------------
Python List Time : 0.09635686874389648 seconds    
NumPy Array Time : 0.005109548568725586 seconds  '''

#Observations
#1.NumPy performed the operation much faster than the Python list.In the output, the Python list took about 0.090 seconds, while the NumPy array took about 0.010 seconds.
#2.NumPy uses vectorized operations, which apply the calculation to the entire array at once, whereas Python lists process elements individually using loops or list comprehensions.
#3.NumPy is optimized for numerical computations and large datasets, so it is more efficient and suitable for tasks in data science, machine learning, and scientific computing.