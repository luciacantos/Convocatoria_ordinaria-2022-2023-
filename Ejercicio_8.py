# EJercicio 8

import re

def encontrar_monstruo(texto):
    monstruo = re.search(r"(tree fiddy|3.50|three fifty)", texto, re.IGNORECASE) #busca la palabra tree fiddy, 3.50 o three fifty
    # re.IGNORECASE es una bandera que permite que la expresión regular coincida con mayúsculas y minúsculas.
    
