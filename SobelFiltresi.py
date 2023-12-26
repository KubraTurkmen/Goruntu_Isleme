import cv2
import numpy as np
import matplotlib.pyplot as plt

def sobel_filtre(gri_goruntu):

    grad_x = cv2.Sobel(gri_goruntu, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gri_goruntu, cv2.CV_64F, 0, 1, ksize=3)


    kenar_buyuklugu = np.sqrt(grad_x**2 + grad_y**2)
    kenar_acisi = np.arctan2(grad_y, grad_x)

    return kenar_buyuklugu, kenar_acisi


gri_goruntu = cv2.imread("../manzara.jpg", cv2.IMREAD_GRAYSCALE)


if gri_goruntu is None:
    print("Görüntü yüklenemedi. Dosya yolu doğru mu?")
else:

    kenar_buyuklugu, kenar_acisi = sobel_filtre(gri_goruntu)


    plt.subplot(2, 2, 1)
    plt.imshow(gri_goruntu, cmap='gray')
    plt.title('Orjinal Görüntü')

    plt.subplot(2, 2, 2)
    plt.imshow(kenar_buyuklugu, cmap='gray')
    plt.title('Kenar Büyüklüğü')

    plt.subplot(2, 2, 3)
    plt.imshow(kenar_acisi, cmap='gray')
    plt.title('Kenar Açısı')

    plt.show()
