import cv2
import numpy as np
import matplotlib.pyplot as plt

def acma_kapama(gri_goruntu, acma_kernel, kapama_kernel):

    acma = cv2.morphologyEx(gri_goruntu, cv2.MORPH_OPEN, acma_kernel)


    kapama = cv2.morphologyEx(gri_goruntu, cv2.MORPH_CLOSE, kapama_kernel)

    return acma, kapama


gri_goruntu = cv2.imread("../manzara.jpg", cv2.IMREAD_GRAYSCALE)


if gri_goruntu is None:
    print("Görüntü yüklenemedi. Dosya yolu doğru mu?")
else:

    acma_kernel = np.ones((5, 5), np.uint8)
    kapama_kernel = np.ones((5, 5), np.uint8)


    acma, kapama = acma_kapama(gri_goruntu, acma_kernel, kapama_kernel)


    plt.subplot(3, 1, 1)
    plt.imshow(gri_goruntu, cmap='gray')
    plt.title('Orjinal Görüntü')

    plt.subplot(3, 1, 2)
    plt.imshow(acma, cmap='gray')
    plt.title('Açma İşlemi')

    plt.subplot(3, 1, 3)
    plt.imshow(kapama, cmap='gray')
    plt.title('Kapama İşlemi')

    plt.show()