import cv2 as cv
import matplotlib.pyplot as plt
import os

# Muda para o diretório onde o arquivo .py e a imagem estão
os.chdir('/Users/valter/Documents/dev/Estudos/Pos-IA-ML/UC7_Desenvolvimento_Aplicacoes_IA/Tema03/Bloco01/3-FeatureMatching')
print(os.getcwd())  # Mostra o diretório de trabalho atual

plt.clf()

img1 = cv.imread('ferrari1.png',cv.IMREAD_GRAYSCALE) # Carrega imagem 1
img2 = cv.imread('ferrari2.jpg',cv.IMREAD_GRAYSCALE) # Carrega imagem 2

# Cria o objeto contendo o algorítmo ORB
orb = cv.ORB_create()

# Encontrar os Keypoints e Descriptors utilizando ORB
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

# Feature Matching
matches = bf.match(des1,des2)

# Organiza os Matches pela distância (semelhança)
matches = sorted(matches, key = lambda x:x.distance)

# Desenha as 15 melhores matches e guarda em uma imagem só

img3 = cv.drawMatches(img1,kp1,img2,kp2,matches[:15],None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
plt.imshow(img3),plt.show()