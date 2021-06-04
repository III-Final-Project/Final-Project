# import the necessary packages
import numpy as np
import cv2
# load the image
img_path = './resources/'
# image = cv2.imread(img_path + 'palette.png')
# image = cv2.imread(img_path + 'pokemon.png')
# image = cv2.imread(img_path + 'hulk.png')
image = cv2.imread(img_path + 'denden.jpg')
scale_percent = 80 # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
image_original = image
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
# define the list of boundaries
# Order: GBR 
# boundaries = [
#     ([17, 15, 100], [50, 56, 200]),
#     ([86, 31, 4], [220, 88, 50]),
#     ([25, 146, 190], [62, 174, 250]),
# #     ([103, 86, 65], [145, 133, 128]),
#     ([204, 102, 255], [255, 255, 255]),
#     ([55, 48, 64], [255, 255, 212])
# ]
# Order: HSR
# boundaries = [
#     ([0, 46, 84], [22, 46, 84]),
#     ([23, 46, 84], [41, 46, 84]),
#     ([42, 46, 84], [64, 46, 84]),
#     ([65, 46, 84], [155, 46, 84]),
#     ([156, 46, 84], [250, 46, 84]),
# ]
# Order: RGB
# boundaries = [
#     ([0, 4, 67], [0, 35, 244]),
# ]
# Order: RGB -2
boundaries = [
    # Red     
    ([0, 43, 46], [5, 255, 255]),
    ([6, 43, 46], [10, 255, 255]),
    ([11, 43, 46], [16, 255, 255]),
#     ([17, 43, 46], [22, 255, 255]),
    ([23, 43, 46], [28, 255, 255]),
#     ([29, 43, 46], [34, 255, 255]),
    # Green
    ([35, 43, 46], [40, 255, 255]),
    ([41, 43, 46], [46, 255, 255]),
#     ([47, 43, 46], [52, 255, 255]),
#     ([53, 0, 46], [58, 255, 255]),
    ([59, 23, 46], [64, 255, 255]),
    # Blue     
    ([100, 43, 46], [105, 255, 255]),
#     ([106, 43, 46], [111, 255, 255]),
    ([112, 43, 46], [117, 255, 255]),
    ([118, 43, 46], [123, 255, 255]),
    # Purple
    ([125, 43, 46], [130, 255, 255]),
    ([131, 43, 46], [135, 255, 255]),
#     ([136, 43, 46], [140, 255, 255]),
    ([141, 43, 46], [145, 255, 255]),
]

# loop over the boundaries
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
    # find the colors within the specified boundaries and apply the mask
    mask = cv2.inRange(image, lower, upper)
    #  Mask   
    output = cv2.bitwise_and(image, image, mask = mask)
    # Change HSV to BGR(cv2 default)   
    output = cv2.cvtColor(output, cv2.COLOR_HSV2BGR)
#     output1 = np.hstack([image, output])
#     plt.imshow(output1)
#     plt.show()
    # show the images
    cv2.imshow("images", np.hstack([image_original, output]))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)