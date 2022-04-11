import cv2

imaeg = cv2.imread("input.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(gray)
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)

# cv2.imshow("Inverted", invertedblur)

# Convert to sketch pencil style
sketch = cv2.divide(gray, invertedblur, scale = 256.0)

# Save the sketch
cv2.imwrite("output.jpg", sketch)
