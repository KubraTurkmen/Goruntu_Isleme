import cv2
import numpy as np
import matplotlib.pyplot as plt

def laplacian_sharpen(gri_goruntu):

    laplacian = cv2.Laplacian(gri_goruntu, cv2.CV_64F)


    keskin_goruntu = gri_goruntu - laplacian


    keskin_goruntu = cv2.normalize(keskin_goruntu, None, 0, 255, cv2.NORM_MINMAX)

    return keskin_goruntu.astype(np.uint8)


gri_goruntu = cv2.imread("../manzara.jpg", cv2.IMREAD_GRAYSCALE)


if gri_goruntu is None:
    print("Görüntü yüklenemedi. Dosya yolu doğru mu?")
else:

    keskin_goruntu = laplacian_sharpen(gri_goruntu)


    plt.subplot(2, 1, 1)
    plt.imshow(gri_goruntu, cmap='gray')
    plt.title('Orjinal Görüntü')

    plt.subplot(2, 1, 2)
    plt.imshow(keskin_goruntu, cmap='gray')
    plt.title('Laplacian Sharpening')

    plt.show()