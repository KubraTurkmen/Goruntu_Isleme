import cv2
import numpy as np
import matplotlib.pyplot as plt

def kontrast_genisletme(gri_goruntu, a=0, b=255):

    min_deger = np.min(gri_goruntu)
    max_deger = np.max(gri_goruntu)


    genisletilmis_goruntu = np.uint8((gri_goruntu - min_deger) / (max_deger - min_deger) * (b - a) + a)

    return genisletilmis_goruntu

gri_goruntu = cv2.imread("../manzara.jpg", cv2.IMREAD_GRAYSCALE)


if gri_goruntu is None:
    print("Görüntü yüklenemedi. Dosya yolu doğru mu?")
else:

    genisletilmis_goruntu = kontrast_genisletme(gri_goruntu, a=50, b=200)


    plt.subplot(2, 1, 1)
    plt.imshow(gri_goruntu, cmap='gray')
    plt.title('Orjinal Görüntü')

    plt.subplot(2, 1, 2)
    plt.imshow(genisletilmis_goruntu, cmap='gray')
    plt.title('Kontrast Genişletilmiş Görüntü')

    plt.show()