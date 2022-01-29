import os
import numpy as np
import matplotlib.pyplot as plt
import imageio

# import cv2 as cv

# img = cv.imread('pokeball.png', 0)
# A = np.array(img)
# m, n = A.shape

# print(A.shape)
points = []
m = 100
n = 100
for i in np.linspace(0,1,m):
     for j in np.linspace(0,1,n):
         points.append((i, j))
points = np.array(points)
print(points.shape)
plt.scatter(points[:,0],points[:,1])
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
N = 20 # iterations

coordinates_lists = [points]
for i in range(N):
    curr_points = coordinates_lists[i]
    c = vec_b(curr_points[:, 0], curr_points[:, 1])
    new_points = np.zeros(curr_points.shape)
    new_points[:, 0],  new_points[:, 1] = c[0], c[1]
    coordinates_lists.append(new_points)

coordinates_lists = np.array(coordinates_lists)
a, b, c = coordinates_lists.shape
# coordinates_lists = coordinates_lists.reshape((a, c, b),order='A')
temp = np.zeros((a, c, b))
for i in range(N):
    temp[i,0,:] = coordinates_lists[i,:,0]
    temp[i,1,:] = coordinates_lists[i,:,1]
coordinates_lists = np.array(temp)
plt.scatter(coordinates_lists[0, 0, :], coordinates_lists[0, 1, :])
# plt.show()

gif_name = 'movie' 
n_frames=N
bg_color='#95A4AD'
marker_color='#283F4E' 
marker_size = 25
print('building plots\n')
filenames = []
for index in np.arange(0, len(coordinates_lists)-1):
    # get current and next coordinates
    x = coordinates_lists[index][0]
    y = coordinates_lists[index][1]
    x1 = coordinates_lists[index+1][0]
    y1 = coordinates_lists[index+1][1]
    # Check if sizes match
    while len(x) < len(x1):
        diff = len(x1) - len(x)
        x = x + x[:diff]
        y = y + y[:diff]
    while len(x1) < len(x):
        diff = len(x) - len(x1)
        x1 = x1 + x1[:diff]
        y1 = y1 + y1[:diff]
    # calculate paths
    x_path = np.array(x1) - np.array(x)
    y_path = np.array(y1) - np.array(y)
    for i in np.arange(0, n_frames + 1):                
        # calculate current position
        x_temp = (x + (x_path / n_frames) * i)
        y_temp = (y + (y_path / n_frames) * i)
        # plot
        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw = dict(aspect="equal"))
        ax.set_facecolor(bg_color)
            
        plt.scatter(x_temp, y_temp, c=marker_color, s = marker_size)
        plt.xlim(-0.5,1.5)
        plt.ylim(-0.5,1.5)
        # remove spines
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        # grid
        ax.set_axisbelow(True)
        ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.7)
        ax.xaxis.grid(color='gray', linestyle='dashed', alpha=0.7)
        # build file name and append to list of file names
        filename = f'images/frame_{index}_{i}.png'
        filenames.append(filename)
        if (i == n_frames):
            for i in range(5):
                filenames.append(filename)
        # save img
        plt.savefig(filename, dpi=96, facecolor=bg_color)
        plt.close()
# Build GIF
print('creating gif\n')
with imageio.get_writer(f'{gif_name}.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
print('gif complete\n')
print('Removing Images\n')
# Remove files
for filename in set(filenames):
    os.remove(filename)
print('done')