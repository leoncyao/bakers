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
N = 0 # iterations
while i < N:
    plt.clf()
    plt.scatter(points[:,0], points[:,1], s=1,  c = A)
    c = vec_b(points[:, 0], points[:, 1])
    points[:, 0],  points[:, 1] = c[0], c[1]
    print(points.shape)
    plt.draw()
    # plt.pause(1)
    plt.show()
    i = i + 1
    pass



# N = 100 # number of iterations

# N = 100 # number of iterations
# M = 1 # number of points
# A = np.random.rand(N, A.shape[0], 2)
# print(A.shape)
# print(A[:, 0].shape)
# i = 1
# # while i < N:
#     # plt.scatter(A[i, :, 0], A[i, :, 1], c=[(1/(i+1), 1/(i+1), 1/(i+1)), 1/(i+1)])
#     plt.plot(A[:i+1, :, 0], A[:i+1, :, 1], c=(1/(i+1), 1/(i+1), 1/(i+1), 1/(i+1)))
#     plt.draw()
#     plt.xlim((0, 1))
#     plt.ylim((0, 1))
#     plt.pause(1)
#     c = vec_b(A[i-1, :, 0], A[i-1, :, 1])
#     A[i, :, 0] = c[0]
#     A[i, :, 1] = c[1]
#     # print(A.shape)
#     i = i + 1

# plt.pause(10)