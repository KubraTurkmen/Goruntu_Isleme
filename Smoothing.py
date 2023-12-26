import cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussian_blur(gri_goruntu, kernel_boyut, sigma):

    blurlu_goruntu = cv2.GaussianBlur(gri_goruntu, (kernel_boyut, kernel_boyut), sigma)

    return blurlu_goruntu


gri_goruntu = cv2.imread("../manzara.jpg", cv2.IMREAD_GRAYSCALE)


if gri_goruntu is None:
    print("Görüntü yüklenemedi. Dosya yolu doğru mu?")
else:

    kernel_boyutu = 5
    sigma = 1
    blurlu_goruntu = gaussian_blur(gri_goruntu, kernel_boyutu, sigma)


    plt.subplot(2, 1, 1)
    plt.imshow(gri_goruntu, cmap='gray')
    plt.title('Orjinal Görüntü')

    plt.subplot(2, 1, 2)
    plt.imshow(blurlu_goruntu, cmap='gray')
    plt.title(f'Gaussian Blurring (Kernel Boyutu={kernel_boyutu}, Sigma={sigma})')

    plt.show()