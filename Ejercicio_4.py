#Ejercicio 4

import re
from typing import Dict, List, Tuple

def do_math(numeros: str) -> int:
    def extract_letter(numero: str) -> Tuple[str, int]:
        letra = re.search(r"[a-zA-Z]", numero).group()
        numero = int(re.sub(r"[a-zA-Z]", "", numero))
        return letra, numero

