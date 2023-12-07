

import cv2 
import mediapipe as mp 
import time

webcam = cv2.VideoCapture(0)

reconhecimento_rosto = mp.solutions.face_detection 
desenho = mp.solutions.drawing_utils 
reconhecedor_rosto = reconhecimento_rosto.FaceDetection()
start_time = time.time()


while webcam.isOpened():
    validacao, frame = webcam.read() 
    if not validacao:
        break
    imagem = frame
    lista_rostos = reconhecedor_rosto.process(imagem)
    
    if lista_rostos.detections: 
        for rosto in lista_rostos.detections:
           # desenho.draw_detection(imagem, rosto)
            current_time = time.time()
            if current_time - start_time >= 1:
                x = int(rosto.location_data.relative_bounding_box.xmin * frame.shape[1])
                y = int(rosto.location_data.relative_bounding_box.ymin * frame.shape[0])
                w = int(rosto.location_data.relative_bounding_box.width * frame.shape[1])
                h = int(rosto.location_data.relative_bounding_box.height * frame.shape[0])

                scale_factor = 1.5
                x = int(x - w * (scale_factor - 1) / 2)
                y = int(y - h * (scale_factor - 1) / 2)
                w = int(w * scale_factor)
                h = int(h * scale_factor)

                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.imwrite(f'rosto_{int(current_time)}.jpg', frame[y:y+h, x:x+w])
                print(f'Imagem capturada: rosto_{int(current_time)}.jpg')
                start_time = current_time
 
    
    cv2.imshow("Rostos na sua webcam", imagem) 
    if cv2.waitKey(20) == 27: 
        break
webcam.release() 
cv2.destroyAllWindows() 
