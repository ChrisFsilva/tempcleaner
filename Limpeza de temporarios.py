# Importar biblioteca de comandos do sistema operacional
import os

# Importar biblioteca de gerenciamento de arquivos
import shutil

# Importar biblioteca de coleta de informação do usuario
import getpass

# Pegar o nome do usuario que terá os temporarios eliminados
username = getpass.getuser()

# apelidar o caminho da pasta temporarios como 'caminho'
with os.scandir (f'C:/Users/{username}/AppData/Local/Temp') as caminho:
    # Para cada conteudo apelidar como 'documentos'
    for documentos in caminho:
        # Criar uma tela apresentando o nome de cada arquivo que será deletado 
        if documentos.is_file():
             print(f'Arquivos que foram deletados: {documentos.name}')

# Deletar os temporarios
shutil.rmtree(caminho)