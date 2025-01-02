Descrição do Repositório

Descrição: Este projeto utiliza OCR (Reconhecimento Óptico de Caracteres) para extrair texto de imagens e salvá-lo automaticamente no formato .docx. Ele processa múltiplas imagens de uma pasta e gera documentos organizados em outra pasta, mantendo o nome original da imagem para o arquivo .docx.

Principais Funcionalidades:
Suporte a imagens nos formatos .jpg, .jpeg e .png.
Processamento automatizado de várias imagens em sequência.
Salvamento dos textos extraídos em arquivos .docx formatados.
Intervalo configurável entre o processamento de cada imagem.
Estrutura clara e reutilizável para projetos de OCR e manipulação de texto.


Tecnologias Utilizadas:
Python
Pillow (PIL): Manipulação de imagens.
Pytesseract: OCR para extração de texto.
python-docx: Criação de documentos .docx.



Como Usar:
Coloque as imagens na pasta imagens.
Execute o script principal.
O texto extraído será salvo na pasta resultado com o mesmo nome das imagens.
