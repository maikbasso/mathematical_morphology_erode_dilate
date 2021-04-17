
# @author Maik Basso <maik@maikbasso.com.br>

import numpy as np

def erode(image, kernel):

	# ref: https://homepages.inf.ed.ac.uk/rbf/HIPR2/erode.htm

	cloneImage = image.copy()

	for x in range(0, image.shape[1]):
		for y in range(0, image.shape[0]):

			count = 0
			for xi in range(x - (kernel.shape[1]//2), x + (kernel.shape[1]//2)+1):
				for yi in range(y - (kernel.shape[0]//2), y + (kernel.shape[0]//2)+1):
					if ((xi >= 0 and xi < image.shape[1]) and (yi >= 0 and yi < image.shape[0])) \
					and (image[yi][xi] != kernel[yi-y][xi-x]):
						count += 1

			if count == 0:
				cloneImage[y][x] = 1
			else:
				cloneImage[y][x] = 0

	return cloneImage

def dilate(image, kernel):

	# ref: https://homepages.inf.ed.ac.uk/rbf/HIPR2/dilate.htm

	cloneImage = image.copy()

	for x in range(0, image.shape[1]):
		for y in range(0, image.shape[0]):

			count = 0
			for xi in range(x - (kernel.shape[1]//2), x + (kernel.shape[1]//2)+1):
				for yi in range(y - (kernel.shape[0]//2), y + (kernel.shape[0]//2)+1):
					if ((xi >= 0 and xi < image.shape[1]) and (yi >= 0 and yi < image.shape[0])) \
					and (image[yi][xi] == kernel[yi-y][xi-x]):
						count += 1

			if count > 0:
				cloneImage[y][x] = 1
			else:
				cloneImage[y][x] = 0

	return cloneImage

image =  np.array([
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0],
	[0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
	[0,0,1,1,1,1,1,0,0,0,0,1,1,1,0,0],
	[0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0],
	[0,0,0,1,1,0,0,0,0,1,1,1,1,1,0,0],
	[0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0],
	[0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0],
	[0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0],
	[0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0],
	[0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0],
	[0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0],
	[0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
])

kernel = np.array([
	[1, 1, 1],
	[1, 1, 1],
	[1, 1, 1]
])

print("Original:\n", image)
print("kernel:\n", kernel)
print("Eroded:\n", erode(image, kernel))
print("Dilated:\n", dilate(image, kernel))