# 2021.11.28 cv2dector.py
# Created by Jack Cobra
# Python 3.9.9
# requirements: opencv-pyhton, numpy
import cv2
import numpy
import math

def edgedect(grayImage, MinThred, MaxThred):
    # Canny Edge Detecting
    cannyImage = cv2.Canny(grayImage, MinThred, MaxThred, 3)
    contours, hierarchy = cv2.findContours(cannyImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Draw the Edge
    processedImg = cv2.drawContours(cannyImage, contours, -1, (255, 0, 0), 3)
    # Calculate the Contour Length
    for index in range(0, int(numpy.size(contours))-1):
        contourLength = cv2.arcLength(contours[index], True)
        print(contourLength)
    cv2.imshow("Processed Image",processedImg)

if __name__ == "__main__":
    srcImage = cv2.imread("Picture1.png") # 此处修改成图片名字
    cv2.namedWindow("[Source Image]", 0)
    cv2.imshow("[Source Image]", srcImage)

    # Turn the srcImg into the grayImg
    grayImage = cv2.cvtColor(srcImage, cv2.COLOR_BGR2GRAY)
    # Filter the Gaussian Blur
    grayImage = cv2.GaussianBlur(grayImage, (3, 3), 0, 0)
    cv2.imshow("[Filtered Image]", grayImage)
    
    # Adjust the Canny Threshold
    canny_nMinThred = 128
    canny_nMaxThred = 255
    edgedect(grayImage, canny_nMinThred, canny_nMaxThred)

    cv2.waitKey(0)

