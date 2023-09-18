import hashlib
import os
from datetime import datetime

def upload_to(instance, filename):
    # Pega a extensão do arquivo (por exemplo, .jpg, .png)
    ext = os.path.splitext(filename)[1]

    # Cria um nome baseado em um hash
    now = datetime.now()
    input_str = f"{filename}{now.strftime('%Y%m%d%H%M%S')}"
    hashed_filename = hashlib.sha256(input_str.encode('utf-8')).hexdigest()

    # Retorna o caminho para o arquivo
    return os.path.join(directory, f'{hashed_filename}{ext}')
