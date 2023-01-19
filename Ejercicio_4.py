#Ejercicio 4

import re
from typing import Dict, List, Tuple

def do_math(numeros: str) -> int: #encontar las letras y los números
    def extract_letter(numero: str) -> Tuple[str, int]:
        letra = re.search(r"[a-zA-Z]", numero).group()
        numero = int(re.sub(r"[a-zA-Z]", "", numero))
        return letra, numero

    numeros_dict = {}
    for number in numeros.split():
        letra, numero = extract_letter(numero)
        if letra in numeros_dict:
            numeros_dict[letra].append(numero)
        else:
            numeros_dict[letra] = [numero]

        
