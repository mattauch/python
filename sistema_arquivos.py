#sistema_arquivo:
#os.path.basename(arq) = apenas o arquivo
#os.path.dirname(arq) = apenas o caminho
#os.path.exists() = se o arquivo existe (False or True)
#os.path.getsize() = tamanho em bytes

import os.path #caminho do sistema operacional
import glob #dir ou desc

lista = sorted(glob.glob('c:\\windows\\*.exe'))

for arq in lista:
    print(os.path.basename(arq))
