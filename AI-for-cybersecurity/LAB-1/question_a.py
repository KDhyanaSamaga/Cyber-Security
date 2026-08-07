import numpy as np

class Matrix:
    def matrix_add(matrix1,matrix2):
        return np.add(matrix1,matrix2)

    def matrix_subtract(matrix1,matrix2):
        return np.subtract(matrix1,matrix2)

    def matrix_multiply(matrix1,matrix2):
        return np.multiply(matrix1,matrix2)

    def matrix_division(matrix1,matrix2):
        return np.divide(matrix1,matrix2)

    def matrix_dot(matrix1,matrix2):
        return np.dot(matrix1,matrix2)

    def matrix_transpose(matrix):
        return np.transpose(matrix)
    

matrix1 = np.array([
    [2, 1, 3], 
    [1, 4, 1], 
    [3, 2, 5]
])

matrix2 = np.array([
    [3, 5, 2], 
    [2, 1, 4], 
    [1, 3, 2]
])

print("Matrix-A:",matrix1)
print("Matrix-B:",matrix2)

print("\n````Matrix opeartions````")
print(f"Matrix Addition:\n{matrix1}+{matrix2}:\n",Matrix.matrix_add(matrix1,matrix2))
print("\n")
print(f"Matrix Subtraction:\n{matrix1}-{matrix2}:\n",Matrix.matrix_subtract(matrix1,matrix2))
print("\n")
print(f"Matrix Multiplication:\n{matrix1}X{matrix2}:\n",Matrix.matrix_multiply(matrix1,matrix2))
print("\n")
print(f"Matrix Division:\n{matrix1}/{matrix2}:\n",Matrix.matrix_division(matrix1,matrix2))
print("\n")
print(f"Transpose of matrix1:{matrix1} is",Matrix.matrix_transpose(matrix1))
print("\n")
print(f"Transpose of matrix2:{matrix2} is",Matrix.matrix_transpose(matrix2))
print("\n")
print(f"Matrix Division:\n{matrix1}.{matrix2}:\n",Matrix.matrix_dot(matrix1,matrix2))
print("\n")
