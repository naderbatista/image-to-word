📄 Descrição do Repositório

📝 Descrição:
Este projeto utiliza OCR (Reconhecimento Óptico de Caracteres) para extrair texto de imagens e salvá-lo automaticamente no formato .docx. Ele processa múltiplas imagens de uma pasta e gera documentos organizados em outra pasta, mantendo o nome original da imagem para o arquivo .docx.

🌟 Principais Funcionalidades:
📂 Suporte a imagens nos formatos: .jpg, .jpeg e .png.

🔄 Processamento automatizado de várias imagens em sequência.
📝 Salvamento dos textos extraídos em arquivos .docx formatados.
⏳ Intervalo configurável entre o processamento de cada imagem.
💡 Estrutura clara e reutilizável para projetos de OCR e manipulação de texto.

⚙️ Tecnologias Utilizadas:
🐍 Python
🖼️ Pillow (PIL): Manipulação de imagens.
🔍 Pytesseract: OCR para extração de texto.
📄 python-docx: Criação de documentos .docx.

🚀 Como Usar:
📁 Coloque as imagens na pasta imagens.
▶️ Execute o script principal.
📝 O texto extraído será salvo na pasta resultado com o mesmo nome das imagens.
🛠️ Passo a Passo para Instalar os Requisitos:
Certifique-se de que o Python está instalado na sua máquina.

Você pode baixar e instalar o Python aqui.
Crie um ambiente virtual (opcional, mas recomendado):

bash
Copiar código
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
.\venv\Scripts\activate   # Para Windows
Instale os pacotes necessários usando o arquivo requirements.txt:

requirements:
pytesseract
Pillow
python-docx
Execute o comando para instalar os pacotes:
bash
Copiar código
pip install -r requirements.txt
Instale o Tesseract OCR:

Baixe o Tesseract para sua máquina:

Tesseract para Windows
Linux/Mac: Instale via terminal com:
bash
Copiar código
sudo apt update && sudo apt install tesseract-ocr
Configure o caminho do Tesseract no código Python:

Atualize o seguinte trecho no script para apontar para o local onde o Tesseract foi instalado:
python
Copiar código
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

🧪 Exemplo de Execução:
Coloque suas imagens na pasta imagens (ex.: imagem1.jpg, imagem2.png).

Execute o script no terminal:
bash
Copiar código
python script.py
Os documentos gerados serão salvos na pasta resultado.

📌 Notas Adicionais:
Certifique-se de que as imagens estão legíveis para que o OCR funcione corretamente.
Verifique o idioma da imagem (use 'eng' para inglês ou 'por' para português no código).
