import os
from ultralytics import YOLO
import csv
from tqdm import tqdm

# Carrega o modelo YOLO a partir do arquivo de pesos
# model = YOLO("C:\\Users\\felip\\source\\repos\\Reconhecimento Facial\\runs\\classify\\train2\\weights\\best.pt")
model = YOLO("..\\Reconhecimento Facial\\runs\\classify\\train2\\weights\\best.pt")

# Função para processar uma imagem e salvar os resultados
def process_image_and_save_results(image_path):
    # Extrai o nome real da classe da estrutura de pastas
    print(f"Caminho da Imagem: {image_path}")
    nome_classe_real = image_path.split("\\")[-2]  # Supondo que o nome da classe esteja na segunda pasta de trás para frente
    print(f"Nome da Classe: {nome_classe_real}")

    # Faz a previsão usando o modelo YOLO
    pred = model.predict(image_path)
    
    # Processa as previsões
    results = []
    for detection in pred:
        top = detection.probs
        class_dict = detection.names
        posicao = top.top5[0]
        
        # Verifica se a posição existe no dicionário
        if posicao in class_dict:
            classe_posicao = class_dict[posicao]
        else:
            classe_posicao = None
        
        # Adiciona os resultados para esta imagem à lista
        # results.append({
        #     'classe': nome_classe_real,
        # })
        results.append({
            'classe': classe_posicao,
        })

        print(f"Nome da Classe Real: {nome_classe_real}")
        print(f"Posição: {posicao}, Classe na Posição: {classe_posicao}")

    
    return results

# Pasta que contém as subpastas com imagens
# root_folder = "C:\\Users\\felip\\source\\repos\\Reconhecimento Facial\\FotosTiradas"
root_folder = "..\\Reconhecimento Facial\\FotosTiradas"

# Obtém o número total de arquivos de imagem para a barra de progresso
total_images = sum(len(files) for _, _, files in os.walk(root_folder) if files)

# Processa cada imagem nas subpastas e armazena os resultados em uma lista
all_results = []
with tqdm(total=total_images, desc="Processing Images", unit="image") as pbar:
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            # Processa apenas arquivos de imagem com extensões específicas, como .jpg, .png, etc.
            if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.gif', '.bmp')):
                image_path = os.path.join(foldername, filename)
                
                image_results = process_image_and_save_results(image_path)
                all_results.extend(image_results)
            
            # Atualiza a barra de progresso
            pbar.update(1)

# Salva os resultados em um arquivo CSV
output_csv_path = 'output_results.csv'
with open(output_csv_path, 'w', newline='') as csvfile:
    fieldnames = ['classe']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for result in all_results:
        writer.writerow(result)
