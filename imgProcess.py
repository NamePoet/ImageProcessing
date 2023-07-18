import cv2
image = cv2.imread("pic.png")
image_Gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 将pic转换为灰度图像
t1, dst1 = cv2.threshold(image_Gray, 127, 255, cv2.THRESH_BINARY)
# 分别显示经过和未经过自适应阈值处理后的图像
cv2.imshow("Traditional", dst1)
# 自适应阈值的计算方法为cv2.ADAPTIVE_THRESH_GAUSSIAN_C
athdGAUS = cv2.adaptiveThreshold\	(image_Gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 5, 3)
cv2.imshow("Adaptive", athdGAUS)
cv2.waitKey()
cv2.destroyAllWindows()
