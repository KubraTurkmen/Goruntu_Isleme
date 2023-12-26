import cv2
import numpy as np
import matplotlib.pyplot as plt

def salt_and_pepper_gurultu_ekle(gri_goruntu, oran=0.02):

    gurultulu_goruntu = gri_goruntu.copy()
    salt_and_pepper = np.random.rand(*gri_goruntu.shape) < oran
    gurultulu_goruntu[salt_and_pepper] = 255
    gurultulu_goruntu[salt_and_pepper == False] = 0

    return gurultulu_goruntu


gri_goruntu = cv2.imread("../manzara.jpg", cv2.IMREAD_GRAYSCALE)


if gri_goruntu is None:
    print("Görüntü yüklenemedi. Dosya yolu doğru mu?")
else:

    oran = 0.02
    gurultulu_goruntu = salt_and_pepper_gurultu_ekle(gri_goruntu, oran)


    plt.subplot(2, 1, 1)
    plt.imshow(gri_goruntu, cmap='gray')
    plt.title('Orjinal Görüntü')

    plt.subplot(2, 1, 2)
    plt.imshow(gurultulu_goruntu, cmap='gray')
    plt.title(f'Tuz-Biber Gürültüsü (Oran={oran})')

    plt.show()