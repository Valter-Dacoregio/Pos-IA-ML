import cv2 as cv
from matplotlib import pyplot as plt
import os

# Muda para o diretório onde o arquivo .py e a imagem estão
os.chdir('/Users/valter/Documents/dev/Estudos/Pos-IA-ML/UC7_Desenvolvimento_Aplicacoes_IA/Tema03/Bloco01/4-FeatureExtraction')
print(os.getcwd())  # Mostra o diretório de trabalho atual

# img = cv.imread('ferrari.png',0)
# img = cv.imread('guitar.png',0)
# img = cv.imread('merca.jpg',0)
# img = cv.imread('moto.jpg',0)
img = cv.imread('tapete.jpg',0)

img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
plt.imshow(img)
plt.show()

# Initiate ORB detector
orb = cv.ORB_create()

# find the keypoints with ORB
kp = orb.detect(img,None)


# compute the descriptors with ORB
kp, des = orb.compute(img, kp)


# draw only keypoints location,not size and orientation
img2 = cv.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)
plt.imshow(img2), plt.show()