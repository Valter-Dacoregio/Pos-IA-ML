import cv2 as cv # Importação da OpenCV
from matplotlib import pyplot as plt # Importação do Plot
import os

# Muda para o diretório onde o arquivo .py e a imagem estão
os.chdir('/Users/valter/Documents/dev/Estudos/Pos-IA-ML/UC7_Desenvolvimento_Aplicacoes_IA/Tema03/Bloco01/1-Limiar/')
print(os.getcwd())  # Mostra o diretório de trabalho atual

plt.clf()

# img = cv.imread('/Users/valter/Documents/dev/Estudos/Pos-IA-ML/UC7_Desenvolvimento_Aplicacoes_IA/Tema03/Bloco01/1-Limiar/estrada.png', 0)  # './' indica o diretório atual

# Agora você pode carregar a imagem sem precisar do caminho absoluto
img = cv.imread('estrada.png', 0)
plt.imshow(img)
plt.show()


# Limiar Descricionario (média)
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

plt.imshow(th1)
plt.show()

# Limiar de OTSU
ret, th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# Cria imagem com limiar Gaussiano
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2) 
# Titulos para o plot

titles = [ '(a) Imagem Original em tons de cinza',

'(b)Limiar Global (v = 127)',

'(c) Limiar de Otsu',

'(d) Limiar Gaussiano']

images = [img, th1, th2, th3] # Define as imagens a serem plotadas

for i in range(4): # For para plotar todas as imagens
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i], fontsize=8)
    plt.xticks([]),plt.yticks([])
plt.show()


ret, faixas = cv.threshold(img,150,255,cv.THRESH_BINARY)
plt.imshow(faixas, 'gray')
plt.show()
