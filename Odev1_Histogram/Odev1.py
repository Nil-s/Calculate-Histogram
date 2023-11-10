import cv2
import matplotlib.pyplot as plt


def calculate_histogram(image):

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    histogram = [0] * 256

    for row in gray_image:
        for pixel_value in row:
            histogram[pixel_value] += 1

    return histogram




img = cv2.imread('image/Dostoyevski.jpg')

hst = calculate_histogram(img)

plt.plot(hst, color='black')
plt.title('Gri Seviye Görüntü Histogramı')
plt.xlabel('Piksel Değeri')
plt.ylabel('Piksel Sayısı')
plt.show()
