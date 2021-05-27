"""
You are given a 2D matrix of dimension  and a positive integer . You have to rotate the matrix  times and print the resultant matrix. Rotation should be in anti-clockwise direction.

Rotation of a  matrix is represented by the following figure. Note that in one rotation, you have to shift elements by one step only.

matrix-rotation

It is guaranteed that the minimum of m and n will be even.

As an example rotate the Start matrix by 2:

    Start         First           Second
     1 2 3 4       2  3  4  5      3  4  5  6
    12 1 2 5  ->   1  2  3  6 ->   2  3  4  7
    11 4 3 6      12  1  4  7      1  2  1  8
    10 9 8 7      11 10  9  8     12 11 10  9
Function Description

Complete the matrixRotation function in the editor below.

matrixRotation has the following parameter(s):

int matrix[m][n]: a 2D array of integers
int r: the rotation factor
Prints
It should print the resultant 2D integer array and return nothing. Print each row on a separate line as space-separated integers.

Input Format

The first line contains three space separated integers, , , and , the number of rows and columns in , and the required rotation.
The next  lines contain  space-separated integers representing the elements of a row of .
"""

def matrixRotation(matrix, r):
    pass

if __name__ == "__main__":
    imp_data = list(map(int,input().split()))
    array = list()
    for _ in range(imp_data[0]):
        temp = list(map(int,input().split()))
        array.append(temp)
    matrixRotation(array,imp_data[-1])
    