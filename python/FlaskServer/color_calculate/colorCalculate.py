# import the necessary packages
import numpy as np
import cv2
# Load the image
img_path = './resources/'
# image = cv2.imread(img_path + 'palette.png')
# image = cv2.imread(img_path + 'pokemon.png')
# image = cv2.imread(img_path + 'hulk.png')
scale_percent = 30 # percent of original size
image = cv2.imread(img_path + 'denden.jpg')
# scale_percent = 80 # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)

# Resize image
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
image_original = image
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Order: HSV 
boundaries = [
    # Red     
    ([0, 43, 46], [5, 255, 255]),
    ([6, 43, 46], [10, 255, 255]),
    ([11, 43, 46], [16, 255, 255]),
    # ([17, 43, 46], [22, 255, 255]),
    ([23, 43, 46], [28, 255, 255]),
    # ([29, 43, 46], [34, 255, 255]),
    # Green
    ([35, 43, 46], [40, 255, 255]),
    ([41, 43, 46], [46, 255, 255]),
    # ([47, 43, 46], [52, 255, 255]),
    # ([53, 0, 46], [58, 255, 255]),
    ([59, 23, 46], [64, 255, 255]),
    # Blue     
    ([100, 43, 46], [105, 255, 255]),
    # ([106, 43, 46], [111, 255, 255]),
    ([112, 43, 46], [117, 255, 255]),
    ([118, 43, 46], [123, 255, 255]),
    # Purple
    ([125, 43, 46], [130, 255, 255]),
    ([131, 43, 46], [135, 255, 255]),
    # ([136, 43, 46], [140, 255, 255]),
    ([141, 43, 46], [145, 255, 255]),
]
index = 0
rank = {}
# Loop over the boundaries
for (lower, upper) in boundaries:
    index += 1
    # Create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
    # Find the colors within the specified boundaries and apply the mask
    mask = cv2.inRange(image, lower, upper)
    #  Mask - Filter the specific color
    output = cv2.bitwise_and(image, image, mask = mask)
    # Check the most appear color
    count = (output > 1).sum()
    # Store the result in dict 
    rank[index] = count
    # Sort the result from large to small
    print(sorted(rank.items(), key=lambda item: item[1], reverse=True))
    # Change HSV to BGR(cv2 default)   
    output = cv2.cvtColor(output, cv2.COLOR_HSV2BGR)
    
    # Return three top colors

    # output1 = np.hstack([image, output])
    # plt.imshow(output1)
    # plt.show()
    # Change image positions
    # cv2.namedWindow('images')
    # cv2.moveWindow('images', 100, 100)
    # Show the images
    # cv2.imshow("images", np.hstack([image_original, output]))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # cv2.waitKey(1)