#!/usr/bin/python3

"""
- define the function
- initialize your new_matrix using the copy function to copy the old matrix value to get the rows and columns.
- loop through the given matrix using a random variable
- update your new_matrix of the variable chosen to loop equals  a square values mapped into a list taking in the matrix of the variable as a parameter.
- return your new_matrix
"""
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for i in range(len(matrix)):
        new_matrix = list(map(lambda x: x * x, matrix[i]))
    return (new_matrix)


