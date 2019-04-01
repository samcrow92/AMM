import cv2


def grayscale():
    path = "C:\\Users\\mari\\Desktop\\AMM\\AMM\\Main\\app\\ProcessedImages\\1.png"
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("C:\\Users\\mari\\Desktop\\AMM\\AMM\\Main\\app\\ProcessedImages\\2.jpg",gray)


