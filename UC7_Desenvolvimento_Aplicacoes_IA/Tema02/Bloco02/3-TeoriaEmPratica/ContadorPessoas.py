# import cv2

# # Carregar o classificador Haar Cascade pré-treinado para detecção de pessoas
# cascade_path = cv2.data.haarcascades + 'haarcascade_fullbody.xml'
# body_cascade = cv2.CascadeClassifier(cascade_path)

# # Carregar a imagem
# # image_path = 'cena3.png'
# # image_path = 'imagem.jpg'
# # image_path = 'imagem2.png'
# image_path = 'imagemTeste.jpg'
# # image_path = 'imagemTeste2.jpg'
# # image_path = 'imagemTeste3.jpeg'
# # image_path = 'imagemTeste4.jpeg'
# # image_path = 'imagemTeste4.png'




# image = cv2.imread(image_path)
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Detectar pessoas na imagem
# bodies = body_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

# # Contar e exibir o número de pessoas detectadas
# num_people = len(bodies)
# print(f"Número de pessoas detectadas: {num_people}")

# # Opcional: desenhar retângulos ao redor das pessoas detectadas
# for (x, y, w, h) in bodies:
#     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# # Mostrar a imagem com as detecções
# cv2.imshow('Detecção de Pessoas', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




import cv2


# Carregar a imagem
imagem = cv2.imread('/Users/valter/Documents/dev/Estudos/Pos-IA-ML/UC7_Desenvolvimento_Aplicacoes_IA/Tema02/Bloco02/3-TeoriaEmPratica/imagemTeste.jpg')

# Carregar o classificador Haar Cascade pré-treinado para detecção de corpos
cascata_corpo = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# Converter a imagem para escala de cinza, pois a detecção Haar Cascade funciona melhor em tons de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Detectar pessoas na imagem
corpos = cascata_corpo.detectMultiScale(imagem_cinza, scaleFactor=1.1, minNeighbors=5)

# Desenhar retângulos ao redor das pessoas detectadas
for (x, y, w, h) in corpos:
    cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Mostrar a imagem com as detecções
cv2.imshow('Detecção de Pessoas', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Exibir a quantidade de pessoas detectadas
print(f"Número de pessoas detectadas: {len(corpos)}")