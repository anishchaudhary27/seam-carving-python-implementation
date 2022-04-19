import cv2
import numpy as np


def compute_min_cost_dir(img):
    height, width, _ = img.shape

    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blurred = img_grey

    x_kernel = np.array([[-0.125, 0., 0.125],
                         [-0.25, 0., 0.25],
                         [-0.125, 0., 0.125]])
    y_kernel = np.array([[-0.125, 0., -0.125],
                         [-0.25, 0., 0.25],
                         [0.125, 0., 0.125]])
    x_grad = cv2.filter2D(img_blurred, ddepth=-1, kernel=x_kernel)
    y_grad = cv2.filter2D(img_blurred, ddepth=-1, kernel=y_kernel)

    xy_grad = np.sqrt(x_grad*x_grad + y_grad*y_grad)
    grad_data = np.asfarray(xy_grad)

    min_cost = [[0 for _ in range(width)] for _ in range(height)]
    min_dir = [[0 for _ in range(width)] for _ in range(height)]

    hmo = height - 1
    for i in range(width):
        min_cost[hmo][i] = grad_data[hmo][i]

    for i in range(hmo-1, -1, -1):
        if min_cost[i+1][0] <= min_cost[i+1][1]:
            min_cost[i][0] = grad_data[i][0] + min_cost[i+1][0]
            min_dir[i][0] = 0
        else:
            min_cost[i][0] = grad_data[i][0] + min_cost[i+1][1]
            min_dir[i][0] = 1

        for j in range(1, width-1):
            if min_cost[i+1][j] <= min_cost[i+1][j+1] \
                    and min_cost[i+1][j] <= min_cost[i+1][j-1]:
                min_cost[i][j] = grad_data[i][j] + min_cost[i+1][j]
                min_dir[i][j] = 0
            elif min_cost[i+1][j+1] <= min_cost[i+1][j-1]:
                min_cost[i][j] = grad_data[i][j] + min_cost[i+1][j+1]
                min_dir[i][j] = 1
            else:
                min_cost[i][j] = grad_data[i][j] + min_cost[i+1][j-1]
                min_dir[i][j] = -1

        if min_cost[i+1][width-1] <= min_cost[i+1][width-2]:
            min_cost[i][width-1] = grad_data[i][width-1] + \
                min_cost[i+1][width-1]
            min_dir[i][width-1] = 0
        else:
            min_cost[i][width-1] = grad_data[i][width-1] + \
                min_cost[i+1][width-2]
            min_dir[i][width-1] = -1

    return min_cost, min_dir


img_name = input("enter image name: ")
img = cv2.imread(img_name)
height, width, channels = img.shape
print("image width: ", width)
target = int(input("enter target image width: "))
print("processing...")
while width > target:
    width -= 1
    min_cost, min_dir = compute_min_cost_dir(img)
    new_img = np.zeros((height, width, channels), dtype=img.dtype)
    pos = 0
    min = 100000000
    for itr in range(width + 1):
        if min_cost[0][itr] < min:
            min = min_cost[0][itr]
            pos = itr

    for x in range(height):
        y = 0
        for j in range(width):
            if j == pos:
                y += 1
            new_img[x][j] = img[x][y]
            y += 1
        pos = pos + min_dir[x][pos]

    img = new_img

cv2.imwrite(img_name.split(".")[0] + "_result.jpg", img)
print("done! resized image saved as " + img_name.split(".")[0] + "_result.jpg")
