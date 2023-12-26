import cv2
import numpy as np
import matplotlib.pyplot as plt

def ortalama_filtre(gri_goruntu, kernel_boyut):

    sonuc_goruntu = np.zeros_like(gri_goruntu)


    kenar_boyutu = kernel_boyut // 2


    for i in range(kenar_boyutu, gri_goruntu.shape[0] - kenar_boyutu):
        for j in range(kenar_boyutu, gri_goruntu.shape[1] - kenar_boyutu):

            kernel_bolgesi = gri_goruntu[i - kenar_boyutu:i + kenar_boyutu + 1, j - kenar_boyutu:j + kenar_boyutu + 1]


            sonuc_goruntu[i, j] = np.mean(kernel_bolgesi)

    return sonuc_goruntu


gri_goruntu = cv2.imread("../manzaras.jpg", cv2.IMREAD_GRAYSCALE)


if gri_goruntu is None:
    print("Görüntü yüklenemedi. Dosya yolu doğru mu?")
else:

    kernel_boyutu = 3
    filtrelenmis_goruntu = ortalama_filtre(gri_goruntu, kernel_boyutu)


    plt.subplot(2, 1, 1)
    plt.imshow(gri_goruntu, cmap='gray')
    plt.title('Orjinal Görüntü')

    plt.subplot(2, 1, 2)
    plt.imshow(filtrelenmis_goruntu, cmap='gray')
    plt.title(f'Ortalama Filtre (Kernel Boyutu={kernel_boyutu})')

    plt.show()