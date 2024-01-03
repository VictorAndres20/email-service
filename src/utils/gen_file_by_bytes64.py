import base64
import os
from random import seed
from random import random


FOLDER_PDF = 'data'


def build_file(bytes_64: str, extension: str) -> str:
    seed(1)
    decrypted = base64.b64decode(bytes_64)
    file_name = str(random()) + "." + extension
    with open(os.path.join(FOLDER_PDF, file_name), 'wb') as f:
        f.write(decrypted)
    return file_name
