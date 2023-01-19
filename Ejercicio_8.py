# EJercicio 8

import re

def encontrar_monstruo(texto):
    monstruo = re.search(r"(tree fiddy|3.50|three fifty)", texto, re.IGNORECASE) #busca la palabra tree fiddy, 3.50 o three fifty
    # re.IGNORECASE es una bandera que permite que la expresión regular coincida con mayúsculas y minúsculas.
    if monstruo: #si encuentra la palabra devuelve el monstruo y cual de las expresiones ha encontrado
        return "Monstruo detectado: " + monstruo.group()
    else:
        return "No es el monstruo."

if __name__ == "__main__":
    texto1 = "Siempre va a tratarse de Tree Fiddy'"
    print("-",texto1,"->",encontrar_monstruo(texto1))
    texto2 = "No soy quien crees, solosoy un músico."
    print("-",texto2,"->",encontrar_monstruo(texto2))
    texto3 = "No soy un monstruo, no mido 3.50."
    print("-",texto3,"->",encontrar_monstruo(texto3))
