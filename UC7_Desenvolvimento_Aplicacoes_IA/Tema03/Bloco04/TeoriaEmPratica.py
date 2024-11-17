import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


def configuracoes():
    # Muda para o diretório onde o arquivo .py e a imagem estão
    os.chdir('/Users/valter/Documents/dev/Estudos/Pos-IA-ML/UC7_Desenvolvimento_Aplicacoes_IA/Tema03/Bloco04/')
    print(os.getcwd())  # Mostra o diretório de trabalho atual
    plt.clf()

PIXELS_BRANCOS_PADRAO = 97695
TOLERANCIA_PERCENTUAL = 10

configuracoes()

def contadorPixels(imageParam):
    if imageParam is None:
        print(f"Erro: Não foi possível carregar a imagem.")
    else:
        # Converter a imagem para escala de cinza
        gray_image = cv2.cvtColor(imageParam, cv2.COLOR_BGR2GRAY)
    
        # Definir o valor limite para considerar o pixel como branco (255 é o valor do branco)
        white_pixel_value = 255
    
        # Criar uma máscara que verifica se os pixels são brancos
        white_pixels_mask = (gray_image == white_pixel_value)
    
        # Contar o número de pixels brancos
        white_pixels_count = np.sum(white_pixels_mask)
    
        print(f"O número de pixels brancos na imagem é: {white_pixels_count}")
        
        return white_pixels_count


def lerImagem(image_path):
    image = cv2.imread(image_path)
    return image

def mostrarImagem(image):
    plt.imshow(image)
    plt.show()


def invadiu(qtdPixelsBrancos):
    qtdEsperada = PIXELS_BRANCOS_PADRAO * (1 - (TOLERANCIA_PERCENTUAL / 100))
    print("qtdEsperada: ", qtdEsperada)
    if(qtdPixelsBrancos < qtdEsperada):
        return True
    else:
        return False


def processar(image_path):
    image = lerImagem(image_path)
    mostrarImagem(image)
    pixelsBrancos = contadorPixels(image)
    print("**************")
    print("Nome Imagem...: ", image_path)
    print("Pixels Brancos: ", pixelsBrancos)
    print("Invadiu.......: ", invadiu(pixelsBrancos))
    print("**************")




nomesImagens = [
    'imagem1.jpg', # SEM INVASÃO
    'imagem2.jpg', # SEM INVASÃO
    'imagem3.jpg', # COM INVASÃO
    'imagem4.jpg', # COM INVASÃO
]

nomeImagemTeste = nomesImagens[0]
processar(nomeImagemTeste)

nomeImagemTeste = nomesImagens[1]
processar(nomeImagemTeste)

nomeImagemTeste = nomesImagens[2]
processar(nomeImagemTeste)

nomeImagemTeste = nomesImagens[3]
processar(nomeImagemTeste)






