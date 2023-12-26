import cv2
import numpy as np
import matplotlib.pyplot as plt

def laplacian_blur(gri_goruntu):

    laplacian = cv2.Laplacian(gri_goruntu, cv2.CV_64F)


    laplacian = np.abs(laplacian)


    laplacian = cv2.normalize(laplacian, None, 0, 255, cv2.NORM_MINMAX)

    return laplacian.astype(np.uint8)


gri_goruntu = cv2.imread("../manzara.jpg", cv2.IMREAD_GRAYSCALE)


if gri_goruntu is None:
    print("Görüntü yüklenemedi. Dosya yolu doğru mu?")
else:

    blurlu_goruntu = laplacian_blur(gri_goruntu)


    plt.subplot(2, 1, 1)
    plt.imshow(gri_goruntu, cmap='gray')
    plt.title('Orjinal Görüntü')

    plt.subplot(2, 1, 2)
    plt.imshow(blurlu_goruntu, cmap='gray')
    plt.title('Laplacian ile Blurlaştırılmış Görüntü')

    plt.show()