import cv2
import numpy as np
import matplotlib.pyplot as plt


def contraharmonic_mean_filtre(gri_goruntu, kernel_boyutu, Q):

    kenar_boyutu = kernel_boyutu // 2


    sonuc_goruntu = np.zeros_like(gri_goruntu, dtype=np.float32)

    for i in range(kenar_boyutu, gri_goruntu.shape[0] - kenar_boyutu):
        for j in range(kenar_boyutu, gri_goruntu.shape[1] - kenar_boyutu):

            kernel_bolgesi = gri_goruntu[i - kenar_boyutu:i + kenar_boyutu + 1, j - kenar_boyutu:j + kenar_boyutu + 1]


            pay = np.sum(np.power(kernel_bolgesi, Q + 1))
            payda = np.sum(np.power(kernel_bolgesi, Q))

            if payda != 0:
                sonuc_goruntu[i, j] = pay / payda

    return sonuc_goruntu.astype(np.uint8)



gri_goruntu = cv2.imread("../manzara.jpg", cv2.IMREAD_GRAYSCALE)


if gri_goruntu is None:
    print("Görüntü yüklenemedi. Dosya yolu doğru mu?")
else:

    kernel_boyutu = 3
    Q = 1.5
    filtrelenmis_goruntu = contraharmonic_mean_filtre(gri_goruntu, kernel_boyutu, Q)


    plt.subplot(2, 1, 1)
    plt.imshow(gri_goruntu, cmap='gray')
    plt.title('Orjinal Görüntü')

    plt.subplot(2, 1, 2)
    plt.imshow(filtrelenmis_goruntu, cmap='gray')
    plt.title(f'Kontraharmonik Ortalama (Kernel Boyutu={kernel_boyutu}, Q={Q})')

    plt.show()