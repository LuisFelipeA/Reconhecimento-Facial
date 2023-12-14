# Importando as bibliotecas necessárias
import cv2
import os
import shutil
import mediapipe as mp
import time

folderPath = "../Reconhecimento-Facial/FotosTiradas"

pathState = os.path.exists(folderPath)
if (not pathState):
    os.mkdir(folderPath)
else:
    shutil.rmtree(folderPath)
    os.mkdir(folderPath)
    
# Inicializando a captura da webcam
webcam = cv2.VideoCapture(0)

# Inicializando os módulos do MediaPipe para reconhecimento de rosto
reconhecimento_rosto = mp.solutions.face_detection
desenho = mp.solutions.drawing_utils
reconhecedor_rosto = reconhecimento_rosto.FaceDetection()
start_time = time.time()



# Loop principal para processar cada quadro da webcam
while webcam.isOpened():
    # Lendo um quadro da webcam
    validacao, frame = webcam.read()

    # Verificando se o quadro foi lido corretamente
    if not validacao:
        break

    # Criando uma cópia do quadro para desenhar sobre ele
    imagem = frame

    # Processando a detecção de rosto no quadro
    lista_rostos = reconhecedor_rosto.process(imagem)

    # Verificando se foram detectados rostos
    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            # Obtendo as coordenadas do retângulo delimitador do rosto
            x = int(rosto.location_data.relative_bounding_box.xmin * frame.shape[1])
            y = int(rosto.location_data.relative_bounding_box.ymin * frame.shape[0])
            w = int(rosto.location_data.relative_bounding_box.width * frame.shape[1])
            h = int(rosto.location_data.relative_bounding_box.height * frame.shape[0])

            # Aplicando um fator de escala ao retângulo
            scale_factor = 1.5
            x = int(x - w * (scale_factor - 1) / 2)
            y = int(y - h * (scale_factor - 1) / 2)
            w = int(w * scale_factor)
            h = int(h * scale_factor)

            # Desenhando o retângulo ao redor do rosto e salvando a imagem
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
           
            cv2.imwrite(f'{folderPath}'+f'/rosto_{int(time.time())}.jpg', frame[y:y + h, x:x + w])
            print(f'Imagem capturada: rosto_{int(time.time())}.jpg')
            start_time = time.time()

    # Exibindo o quadro com os rostos detectados
    cv2.imshow("Rostos na sua webcam", imagem)

    # Verificando se a tecla 'Esc' foi pressionada para encerrar o programa
    if cv2.waitKey(20) == 27:
        break

# Liberando os recursos da webcam
webcam.release()

# Fechando todas as janelas
cv2.destroyAllWindows()
