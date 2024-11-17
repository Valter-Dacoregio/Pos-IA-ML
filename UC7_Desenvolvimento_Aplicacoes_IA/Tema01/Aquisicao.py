import cv2;
import matplotlib.pyplot as plt;
import numpy as np;

imagem = cv2.imread("imagem.jpg")
imagem2 = cv2.imread("imagem2.png")

imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2BGR)
imagem2 = cv2.cvtColor(imagem2, cv2.COLOR_RGB2BGR)

plt.imshow(imagem)
#plt.imshow(imagem2)

plt.clf()

plt.hist(imagem.ravel())
#plt.hist(imagem2.ravel())

plt.clf()

# Se for uma imagem RGB, você pode transformar em escala de cinza
imagem_gray = np.mean(imagem, axis=2)
plt.hist(imagem_gray.ravel(), bins=256, range=(0, 256), color='gray')

imgRavel = imagem.ravel()

plt.clf()

imagem_preto_branco = cv2.imread("imagem.jpg", 0)
plt.imshow(imagem_preto_branco)

plt.clf()

plt.hist(imagem_preto_branco)

plt.clf()

equ = cv2.equalizeHist(imagem_preto_branco)
plt.imshow(equ)

plt.clf()

equRavel = equ.ravel()
plt.hist(equRavel)