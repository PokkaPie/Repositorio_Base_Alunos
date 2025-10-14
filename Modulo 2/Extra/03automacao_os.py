# Separar diretórios e arquivos

import os
caminho="/home/user/documentos/arquivo.txt"
print(os.path.dirname(caminho)) # /home/user/documentos
print(os.path.basename(caminho)) # arquivo.txt
