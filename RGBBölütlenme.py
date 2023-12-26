import cv2
import numpy as np
import matplotlib.pyplot as plt

def rgb_bolutle(goruntu):

    kirmizi = goruntu[:, :, 2]
    yesil = goruntu[:, :, 1]
    mavi = goruntu[:, :, 0]

    return kirmizi, yesil, mavi


renkli_goruntu = cv2.imread("../manzara.jpg")


if renkli_goruntu is None:
    print("Görüntü yüklenemedi. Dosya yolu doğru mu?")
else:

    kirmizi, yesil, mavi = rgb_bolutle(renkli_goruntu)


    plt.subplot(2, 2, 1)
    plt.imshow(renkli_goruntu)
    plt.title('Orjinal Görüntü')

    plt.subplot(2, 2, 2)
    plt.imshow(kirmizi, cmap='gray')
    plt.title('Kırmızı Bileşen')

    plt.subplot(2, 2, 3)
    plt.imshow(yesil, cmap='gray')
    plt.title('Yeşil Bileşen')

    plt.subplot(2, 2, 4)
    plt.imshow(mavi, cmap='gray')
    plt.title('Mavi Bileşen')

    plt.show()