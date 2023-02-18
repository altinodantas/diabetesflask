# DiabetesFlask
Usando Flask para servir modelo de Machine Learning treinado sobre dados de pacientes com e sem diabetes.

![Screenshot](https://raw.githubusercontent.com/altinodantas/diabetesflask/main/static/assets/screenshot.jpg)

## Como usar

Baixar o repositório, ativar o ambiente (env) e executar o arquivo `main.py` via linha de comando. Em seguinda, acessar o endereço http://localhost:8001 no navegador. Caso seja necessário, mudar a porta na última linha do arquivo main.py.

- Abrir terminal
- Clonar o repositório `git clone https://github.com/altinodantas/diabetesflask.git`
- Navegar até o diretório `diabetesflask`
- Ativar o ambiente `source env/bin/activate`
- Executar `python main.py`
- Acessar http://localhost:8001

Para realizar um novo treinamento do modelo, basta executar o arquivo `ml/train.py`.

## Dependências
- Sklearn
- Flask
  - flask_bootstrap
  - flask_wtf
- Pandas
- joblib
