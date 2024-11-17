# REFERÊNCIAS
https://pjreddie.com/darknet/yolo/

git clone https://github.com/pjreddie/darknet
cd darknet
make

wget https://pjreddie.com/media/files/yolov3.weights

./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg


# EXECUTA O MODELO PARA UMA IMAGEM ESPECÍFICA
./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
 sudo ./darknet detect cfg/yolov3.cfg yolov3.weights ../imagemTeste.jpg

# MOSTRA A IMAGEM COM AS MARCAÇÕES
open predictions.jpg