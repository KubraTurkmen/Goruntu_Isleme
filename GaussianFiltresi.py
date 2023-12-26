import cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussian_filtre(gri_goruntu, kernel_boyut, sigma):

    filtrelenmis_goruntu = cv2.GaussianBlur(gri_goruntu, (kernel_boyut, kernel_boyut), sigma)

    return filtrelenmis_goruntu


gri_goruntu = cv2.imread("../manzara.jpg", cv2.IMREAD_GRAYSCALE)


if gri_goruntu is None:
    print("Görüntü yüklenemedi. Dosya yolu doğru mu?")
else:

    kernel_boyutu = 5
    sigma = 0
    filtrelenmis_goruntu = gaussian_filtre(gri_goruntu, kernel_boyutu, sigma)


    plt.subplot(2, 1, 1)
    plt.imshow(gri_goruntu, cmap='gray')
    plt.title('Orjinal Görüntü')

    plt.subplot(2, 1, 2)
    plt.imshow(filtrelenmis_goruntu, cmap='gray')
    plt.title(f'Gaussian Filtre (Kernel Boyutu={kernel_boyutu}, Sigma={sigma})')

    plt.show()