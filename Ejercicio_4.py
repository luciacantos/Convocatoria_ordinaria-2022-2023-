#Ejercicio 4

import re
from typing import Dict, List, Tuple

def do_math(numbers: str) -> int:
    def extract_letter(number: str) -> Tuple[str, int]:
        letter = re.search(r"[a-zA-Z]", number).group()
        number = int(re.sub(r"[a-zA-Z]", "", number))
        return letter, number

    numbers_dict = {}
    for number in numbers.split():
        letter, number = extract_letter(number)
        if letter in numbers_dict:
            numbers_dict[letter].append(number)
        else:
            numbers_dict[letter] = [number]

    sorted_numbers = [num for letter in sorted(numbers_dict) for num in numbers_dict[letter]]

    result = sorted_numbers[0]
    operations = "+-*/"
    operation_index = 0
    for i in range(1, len(sorted_numbers)):
        operation = operations[operation_index % 4]
        result = eval(f"{result} {operation} {sorted_numbers[i]}")
        operation_index += 1
    return round(result)

print("24z6 1x23 y369 89a 900b ->",do_math("24z6 1x23 y369 89a 900b"))
print("24z6 1z23 y369 89z 900b ->",do_math("24z6 1z23 y369 89z 900b"))
print("10a 90x 14b 78u 45a 7b 34y ->",do_math("10a 90x 14b 78u 45a 7b 34y"))

