import os
from ultralytics import YOLO
import csv
from tqdm import tqdm

# Load the YOLO model
model = YOLO('../estagio/runs/classify/train2/weights/best.pt')

def process_image_and_save_results(image_path):
    # Split the image path to get different components
    parts = image_path.split("/")[-1].split("-")
    
    # Get the real class name from the image path
    nome_classe_real = image_path.split("/")[-2]
    
    # Predict using the YOLO model
    pred = model.predict(image_path)
    
    # Process the predictions
    results = []
    for detection in pred:
        top = detection.probs
        class_dict = detection.names
        posicao = top.top5[0]
        
        # Check if the position exists in the dictionary
        if posicao in class_dict:
            classe_posicao = class_dict[posicao]
        else:
            classe_posicao = None
        
        # Append the results for this image to the list
        results.append({
            'image_path': image_path,
            'classe': nome_classe_real,
        })
    
    return results

# Folder containing the subfolders with images
root_folder = '../estagio/yoloclassification/dataset/test'

# Get the total number of image files for the progress bar
total_images = sum(len(files) for _, _, files in os.walk(root_folder) if files)

# Process each image in subfolders and store the results in a list
all_results = []
with tqdm(total=total_images, desc="Processing Images", unit="image") as pbar:
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            # Process only image files with specific extensions like .jpg, .png, etc.
            if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.gif', '.bmp')):
                image_path = os.path.join(foldername, filename)
                image_results = process_image_and_save_results(image_path)
                all_results.extend(image_results)
            
            # Update the progress bar
            pbar.update(1)

# Save the results to a CSV file
output_csv_path = 'output_results.csv'


""" import cv2 # importar o opencv -> para instalar rode pip install opencv-python
import mediapipe as mp # para instalar rode pip install mediapipe

 webcam = cv2.VideoCapture(0) # para conectar o python com a nossa webcam.

reconhecimento_rosto = mp.solutions.face_detection # ativando a solução de reconhecimento de rosto
desenho = mp.solutions.drawing_utils # ativando a solução de desenho
reconhecedor_rosto = reconhecimento_rosto.FaceDetection() # criando o item que consegue ler uma imagem e reconhecer os rostos ali dentro

while webcam.isOpened():
    validacao, frame = webcam.read() # lê a imagem da webcam
    if not validacao:
        break
    imagem = frame
    lista_rostos = reconhecedor_rosto.process(imagem) # usa o reconhecedor para criar uma lista com os rostos reconhecidos
    
    if lista_rostos.detections: # caso algum rosto tenha sido reconhecido
        for rosto in lista_rostos.detections: # para cada rosto que foi reconhecido
            desenho.draw_detection(imagem, rosto) # desenha o rosto na imagem
    
    cv2.imshow("Rostos na sua webcam", imagem) # mostra a imagem da webcam para a gente
    if cv2.waitKey(5) == 27: # ESC # garante que o código vai ser pausado ao apertar ESC (código 27) e que o código vai esperar 5 milisegundos a cada leitura da webcam
        break
webcam.release() # encerra a conexão com a webcam 
cv2.destroyAllWindows() # fecha a janela que mostra o que a webcam está vendo """

with open(output_csv_path, 'w', newline='') as csvfile:
    fieldnames = ['image_path','classe']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for result in all_results:
        writer.writerow(result)
