import numpy as np

print("Question 1")
row = 3
col = 3
f = 3.7
x_points = [3.6, 3.8, 3.9]
y_points = [1.675, 1.436, 1.318]
matrix = np.zeros((row,col))

for i in range(row):
  matrix[i][0] = y_points[i]
  
for j in range(1,row):
  for k in range(1,j+1):
    V1 = (f - x_points[j-k]) * matrix[j][k-1]
    V2 = (f-x_points[j]) * matrix[j-1][k-1]

    matrix[j][k] = (V1 - V2) / (x_points[j] - x_points[j-k])

print(matrix[row-1][col-1])
print("\n")

print("Question 2")
row = 4
col = 4
x2_points = [7.2, 7.4, 7.5, 7.6] 
y2_points = [23.5492, 25.3913, 26.8224, 27.4589]

matrix2 = np.zeros((row,col))

for i in range(row):
  matrix2[i][0] = y2_points[i]

for j in range(row):
  for k in range(1,j+1):
    matrix2[j][k] = (matrix2[j][k-1] - matrix2[j-1][k-1])/(x2_points[j]-x2_points[j-k])

matrix2a = np.zeros(row-1)
for j in range(1,row):
  matrix2a[j-1] = (matrix2[j][j])
print(matrix2a)
print("\n")

print("Question 3")

f2 = 7.3

for j in range(1,row):
  for k in range(1,j+1):
    V1 = (f2 - x2_points[j-k]) * matrix2[j][k-1]
    V2 = (f2-x2_points[j]) * matrix2[j-1][k-1]

    matrix2[j][k] = (V1 - V2) / (x2_points[j] - x2_points[j-k])

print(matrix2[row-1][col-1])
print("\n")

print("Question 4")
