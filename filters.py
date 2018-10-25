import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('striping.bmp',0)

img_float32 = np.fft.fft2(img)
fshift = np.fft.fftshift(img_float32)

#show the furier  image transform
furier_tr = 20*np.log(np.abs(fshift))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(furier_tr, cmap = 'gray')
plt.title('furier transform'), plt.xticks([]), plt.yticks([])
plt.show()



for x in range(350,430):
    for y in range(580,660):
       print(furier_tr[x,y])
       fshift[y, x]=1


for x in range(880,960):
    for y in range (660,740):
           print(furier_tr[x,y])
           fshift[y, x]=1





f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

cv2.imwrite('output.png',img_back)
furier_tr2 = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(furier_tr2, cmap = 'gray')
plt.title('modified furier'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('output'), plt.xticks([]), plt.yticks([])

plt.show()