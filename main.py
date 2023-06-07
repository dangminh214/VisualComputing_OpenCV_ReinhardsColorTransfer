# import numpy as np ## optional
import cv2
import numpy as np
print("OpenCV-Version: " + cv2.__version__)

#Load Images
original_img = cv2.imread("figures/yoshi.png")
copy_img = cv2.imread("figures/yoshi.png")

height, width, color_channel = original_img.shape

float_image = original_img.astype(np.float32) / 255.0;

print("Data Type: ", float_image.dtype)

print("Height: ", height);
print("Width: ", width);
print("Color Channel: ", color_channel);

startpoint_X = 500
startpoint_Y = 500

endpoint_X = 510
endpoint_Y = 510

startpoint = (startpoint_X, startpoint_Y)
endpoint = (endpoint_X, endpoint_Y)

color = (0,0,255)

#draw a red rectangle 10x10 px in the middle of the image
red_rectangle = cv2.rectangle(copy_img, startpoint, endpoint, color, -1);

for row in range(0, height, 5):
    # Set pixels in the row to black
    copy_img[row,] = (0, 0, 0)

#save to local disk
cv2.imwrite('Modified Image With Red Rectangle and Black Row.jpg', copy_img)

#load the mask
mask_img = cv2.imread("figures/mask.png")

#convert to HSV
hsv_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2HSV)

mask_height, mask_width, _ = mask_img.shape;

for y in range(mask_height):
    for x in range(mask_width):
       b,g,r = mask_img[y,x]
       if (b,g,r) == (255,255,255):

            white_pixel_location = (y,x)

            hue_of_this_pixel = mask_img[y, x, 0]
            hue_of_this_pixel = hue_of_this_pixel + 160

            hsv_img[white_pixel_location] = hue_of_this_pixel


# Convert the modified Yoshi image back to BGR color space
modified_yoshi = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)

modified_yoshi = cv2.resize(modified_yoshi, (500, 646))
original_img = cv2.resize(original_img, (500, 646))
copy_img = cv2.resize(copy_img, (500, 646))

cv2.imshow("hsv_img", modified_yoshi)
cv2.imshow("original_img", original_img)
cv2.imshow("copy_img", copy_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

