import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_denklestirme(gri_goruntu):

    histogram, sinir_degerleri = np.histogram(gri_goruntu.flatten(), 256, [0, 256])


    kumulatif_dagilim = histogram.cumsum()


    denk_goruntu = (kumulatif_dagilim[sinir_degerleri[gri_goruntu]] * 255.0 / kumulatif_dagilim[-1]).astype(np.uint8)


    denk_histogram, _ = np.histogram(denk_goruntu.flatten(), 256, [0, 256])

    return denk_goruntu, histogram, denk_histogram


gri_goruntu = cv2.imread("../manzara.jpg", cv2.IMREAD_GRAYSCALE)


denk_goruntu, histogram, denk_histogram = histogram_denklestirme(gri_goruntu)


plt.subplot(3, 1, 1)
plt.imshow(gri_goruntu, cmap='gray')
plt.title('Orjinal Görüntü')

plt.subplot(3, 1, 2)
plt.plot(histogram, color='black')
plt.title('Orjinal Histogram')

plt.subplot(3, 1, 3)
plt.imshow(denk_goruntu, cmap='gray')
plt.title('Histogram Denkleştirilmiş Görüntü')

plt.show()