# DiabetesFlask
Usando Flask para servir modelo de Machine Learning treinado sobre dados de pacientes com e sem diabetes.

![Screenshot](https://raw.githubusercontent.com/altinodantas/diabetesflask/main/static/assets/screenshot.jpg)

## Como usar

Baixar o repositório e executar python main.py via linha de comando. Em seguinda, acessar o endereço http://localhost:8001/ no navegador. 
Caso seja necessário, mudar a porta na última linha do arquivo main.py.

Para realizar um novo treinamento do modelo, basta executar o arquivo ml/train.py.


## Dependências
- Sklearn
- Flask
  - flask_bootstrap
  - flask_wtf
- Pandas
- joblib
