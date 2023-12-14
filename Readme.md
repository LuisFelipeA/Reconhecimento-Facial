# Reconhecimento Facial

### Como clonar o projeto?

- git clone https://github.com/LuisFelipeA/Reconhecimento-Facial

Após clonar abra a pasta que foi gerada

### Dependencias
Para que a aplicação possa funcionar instale primeiro as dependências do projeto, basta abrir a sua CLI no diretório gerado ao clonar o projeto utilizando os seguintes comandos:

- pip install ultralytics
- pip install opencv-python
- pip install mediapipe

***OBS***: Não recomendamos o uso da última versão do python **(3.12.1)**, pois tivemos alguns problemas para instalar as dependencias. Pode ser usada a versão **(3.10.12)** ou **(3.11.5)**. Pode funcionar em outras versões também.

### Como rodar a aplicação?

O repositorio já está treinado, então você pode rodar o arquivo `ReconhecimentoFacial.py` que abrirá sua **webcam** e vai tirar algumas fotos sua. Com as fotos tirada agora voce pode rodar o arquivo `evaluation.py` que vai comparar as fotos com o nosso modelo. Quando terminar de rodar vai ser criado um arquivo chamado `output_results.csv`, nele estão os resultados, caso seu rosto não seja reconhecido ele vai estar como desconhecido.

**Exemplo do resultado de um dos testes**
![Alt text](../Reconhecimento-Facial/doc/img_readme1.jpeg)

Aqui apenas uma foto que mandei para comparar foi reconhecida

### Como treinar um novo modelo?

Para treinar um novo modelo você precisa criar uma pasta chamada **DataSet** dentro de **yoloclassification** passando as imagens que você quer treinar. Temos um arquivo **Dataset.txt** com dois liks de imagens para adiantar se preferir.

Agora você pode rodar  o arquivo `yoloclassificador.py` que irá treinar seu novo modelo. Após ser treinado será criada uma nova pasta chamada **train** se ela já existir vai ter uma numeração no nome (ex: `train3`), basta ir então até o arquivo `evaluation.py` e alterar o seguinte trecho do caminho para o diretório: 

![Alt text](../Reconhecimento-Facial/doc/img_readme2.jpeg)

No caso do nosso exemplo trocaríamos o `/train2` por `/train3`