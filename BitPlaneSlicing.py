import cv2
import numpy as np
import matplotlib.pyplot as plt

def bit_plane_slicing(image):

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    rows, cols = gray_image.shape


    bit_planes = [np.zeros((rows, cols), dtype=np.uint8) for _ in range(8)]


    for i in range(8):
        bit_planes[i] = np.bitwise_and(gray_image, 2 ** i)
        bit_planes[i] = bit_planes[i] * 255  # 0 ve 255 arasında değerler elde etmek için

    return bit_planes


image_path = "../resim.jpg"
image = cv2.imread(image_path)


bit_planes = bit_plane_slicing(image)


plt.figure(figsize=(10, 6))
plt.subplot(3, 3, 1), plt.imshow(image, cmap='gray'), plt.title('Original Image')

for i in range(8):
    plt.subplot(3, 3, i + 2), plt.imshow(bit_planes[i], cmap='gray'), plt.title(f'Bit {i + 1}')

plt.tight_layout()
plt.show()