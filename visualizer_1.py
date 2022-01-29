import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('pokeball.png', 0)
A = np.array(img)
m, n = A.shape

print(A.shape)
points = []
for i in np.linspace(0,1,A.shape[0]):
     for j in np.linspace(0,1,A.shape[1]):
         points.append((i, j))
points = np.array(points)
print(points.shape)
# plt.scatter(points[:,0], points[:,1], s=1,  c = A)
# plt.show()

def b(x, y):
    if 0 <= x and x <= 1/2:
        return (2 * x, y / 2)
    else:
        return (2 * x - 1, (y + 1) / 2)
vec_b = np.vectorize(b)

# # points  = np.linspace((0,1),(0,1), (A.shape[0], A.shape[1]))
# print(points.shape)
# # i = 0
N = 10 # iterations
while i < N:
    plt.clf()
    plt.scatter(points[:,0], points[:,1], s=1,  c = A)
    c = vec_b(points[:, 0], points[:, 1])
    points[:, 0],  points[:, 1] = c[0], c[1]
    plt.draw()
    plt.show()
    i = i + 1
    pass

