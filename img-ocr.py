import pytesseract
from PIL import Image
import os
import time
from docx import Document
from docx.shared import Pt

# Configurar o caminho do executável do Tesseract (caso seja necessário)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    """Extrai texto de uma imagem usando Tesseract OCR."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {image_path}")
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='eng')  # 'por' para português ou 'eng' para inglês
    return text

def save_text_to_doc(text, output_path):
    """Salva o texto extraído em um arquivo .docx."""
    doc = Document()
    
    # Adicionar o texto extraído com a formatação desejada
    para = doc.add_paragraph()
    run = para.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(10)
    
    # Salvar o documento
    doc.save(output_path)

def process_images_in_folder(input_folder, output_folder, interval=5):
    """
    Processa todas as imagens na pasta especificada.
    Cria um arquivo .docx para cada imagem com o mesmo nome da imagem.
    """
    if not os.path.exists(input_folder):
        raise FileNotFoundError(f"Pasta não encontrada: {input_folder}")
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Cria a pasta de saída se não existir
    
    # Listar todos os arquivos de imagem na pasta
    files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    if not files:
        print("Nenhuma imagem encontrada na pasta.")
        return

    for file in files:
        image_path = os.path.join(input_folder, file)
        doc_filename = os.path.splitext(file)[0] + ".docx"
        doc_output_path = os.path.join(output_folder, doc_filename)
        
        print(f"Lendo imagem: {file}")
        extracted_text = extract_text_from_image(image_path)
        
        print(f"Salvando texto extraído em: {doc_filename}")
        save_text_to_doc(extracted_text, doc_output_path)
        
        print(f"Processamento concluído para: {file}")
        print(f"Aguardando {interval} segundos antes de processar a próxima imagem...\n")
        time.sleep(interval)

def main():
    # Caminho da pasta de entrada (imagens) e saída (resultados)
    input_folder = r"C:\Users\NADER\Desktop\Arquivos\Projetos-Python\imagem-ocr\imagens"
    output_folder = r"C:\Users\NADER\Desktop\Arquivos\Projetos-Python\imagem-ocr\resultado"
    
    # Intervalo entre processamentos (em segundos)
    interval = 5  # Ajuste conforme necessário
    
    # Processar as imagens na pasta
    process_images_in_folder(input_folder, output_folder, interval)

if __name__ == "__main__":
    main()
