import cv2import matplotlib.pyplot as pltimport numpy as npplt.clf()imagem = cv2.imread("imagem.jpg")imagem2 = cv2.imread("imagem2.png")imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2BGR)imagem2 = cv2.cvtColor(imagem2, cv2.COLOR_RGB2BGR)plt.imshow(imagem)plt.show()plt.imshow(imagem2)plt.show()def embacar(img, tamanho):    blurImg = cv2.blur(img, (tamanho, tamanho))    return blurImgdef plotarImagem(imagem):    plt.imshow(imagem)    plt.show()plotarImagem(embacar(imagem, 11))aguca = np.array([    [-1,-1,-1],    [1,0,-1],    [1,1,0]])detect = np.array([    [0,-1,-1],    [1,0,-1],    [1,1,0]])sol = np.array([    [0.272,0.534,0.131],    [0.349,0.686,0.168],    [0.393,0.769,0.189]])def filtro_conv(imagem, kernel):    return cv2.filter2D(imagem, -1, kernel)plotarImagem(filtro_conv(imagem, aguca))plotarImagem(filtro_conv(imagem2, aguca))plotarImagem(filtro_conv(imagem, detect))plotarImagem(filtro_conv(imagem2, detect))plotarImagem(filtro_conv(imagem, sol))plotarImagem(filtro_conv(imagem2, sol))