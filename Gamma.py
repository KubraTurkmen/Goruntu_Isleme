import cv2
import numpy as np
import matplotlib.pyplot as plt

def gamma_duzeltme(gri_goruntu, gamma):

    duzeltilmis_goruntu = np.power(gri_goruntu / 255.0, gamma) * 255.0
    duzeltilmis_goruntu = np.uint8(duzeltilmis_goruntu)

    return duzeltilmis_goruntu


gri_goruntu = cv2.imread("../manzara.jpg", cv2.IMREAD_GRAYSCALE)


if gri_goruntu is None:
    print("Görüntü yüklenemedi. Dosya yolu doğru mu?")
else:

    gamma_degeri = 1.5
    duzeltilmis_goruntu = gamma_duzeltme(gri_goruntu, gamma_degeri)


    plt.subplot(2, 1, 1)
    plt.imshow(gri_goruntu, cmap='gray')
    plt.title('Orjinal Görüntü')

    plt.subplot(2, 1, 2)
    plt.imshow(duzeltilmis_goruntu, cmap='gray')
    plt.title(f'Gamma Düzeltme (Gamma={gamma_degeri})')

    plt.show()