
import cv2
import numpy as np

image_path = r'image.png'
image = cv2.imread(image_path)

lower_color = np.array([150, 150, 150])
upper_color = np.array([200, 200, 200])

mask = cv2.inRange(image, lower_color, upper_color)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

min_radius = 3
max_radius = 6
dots_num = 0

for contour in contours:
    (x, y), radius = cv2.minEnclosingCircle(contour)
    if min_radius <= radius <= max_radius:
        area = cv2.contourArea(contour)
        if area > 0:
            perimeter = cv2.arcLength(contour, True)
            circularity = (4 * np.pi * area) / (perimeter ** 2)
            if circularity > 0.7:
                cv2.circle(image, (int(x), int(y)), int(radius), (0, 255, 0), 2)
                dots_num += 1


print('Total dots: ', dots_num)
cv2.imshow('Detected Dots', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
