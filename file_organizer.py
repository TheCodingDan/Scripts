import os
import shutil
import sys

if len(sys.argv) < 2:
    print("Diretório não fornecido.")
    exit()

pasta = sys.argv[1]

# Verificar se o diretório existe
if not os.path.isdir(pasta):
    print("Diretório inválido.")
    exit()

# Definir dicionário de tipos de arquivo e suas respectivas pastas de destino
tipos_arquivo = {
    '.txt': 'Arquivos de Texto',
    '.pgn': 'Arquivos de Xadrez',
    '.zip': 'Arquivos WinRar',
    '.7z': 'Arquivos WinRar',
    '.html': 'Links',
    '.webp': 'Links',
    '.rar': 'Arquivos Winrar',
    '.gz': 'Arquivos Winrar',
    '.css':'Arquivos CSS',
    '.pptx': 'Arquivos PowerPoint',
    '.gba': 'Jogos Emulador',
    '.nds': 'Jogos Emulador',
    '.ipynb': 'Arquivos em Python',
    '.pyw': 'Arquivos em Python',
    '.bat': 'Arquivos em Python',
    '.py': 'Arquivos em Pyhon',
    '.spec': 'Arquivos em Python',
    '.csv': 'Planilhas Excel',
    '.ove': 'Projetos Olive',
    '.ico': 'Icons',
    '.c': 'Arquivos em C',
    '.circ': 'Arquivos Logsim',
    '.msi': 'Instaladores',
    '.mp3':  'Videos',
    '.mp4': 'Videos',
    '.webm': 'Videos',
    '.aseprite': 'Sprites',
    '.ase': 'Sprites',
    '.exe': 'Executáveis',
    '.ods': 'Documentos Word',
    '.tif': 'Redação Enem',
    '.docx': 'Documentos Word',
    '.doc': 'Documentos Word',
    '.xlsx': 'Planilhas Excel',
    '.xls': 'Planilhas Excel',
    '.pdf': 'Arquivos PDF',
    '.jpg': 'Imagens',
    '.jpeg': 'Imagens',
    '.png': 'Imagens',
    '.gif': 'Imagens',
    '.rmskin': 'Skins Desktop',
    '.lnk': 'Atalhos',
    '.url': 'Atalhos',
}

# Percorrer os arquivos na pasta
for nome_arquivo in os.listdir(pasta):
    caminho_arquivo = os.path.join(pasta, nome_arquivo)
    if os.path.isfile(caminho_arquivo):
        extensao = os.path.splitext(nome_arquivo)[1].lower()

        if extensao in tipos_arquivo:
            pasta_destino = tipos_arquivo[extensao]
            pasta_destino_completa = os.path.join(r'C:\Users\Calili\Desktop\Arquivos', pasta_destino)  # Substitua pelo caminho correto da Área de Trabalho e pasta de destino

            # Verificar se a pasta de destino existe, caso contrário, criar
            os.makedirs(pasta_destino_completa, exist_ok=True)

            # Mover o arquivo para a pasta de destino
            shutil.move(caminho_arquivo, os.path.join(pasta_destino_completa, nome_arquivo))

            print(f'Arquivo {nome_arquivo} movido para a pasta {pasta_destino}')

