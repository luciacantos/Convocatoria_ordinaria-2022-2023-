# Ejercicio 2
def simplify(polynomial: str) -> str:
    from collections import Counter
    from itertools import groupby
    from operator import itemgetter


    monomials = polynomial.split("+")

    monomials.sort(key=lambda x: len(x), reverse=True)
    monomials_by_degree = groupby(monomials, key=lambda x: len(x))


    monomials_by_degree = {degree: sorted(list(monomials)) for degree, monomials in monomials_by_degree}

    monomials_by_variables = {}
    for degree, monomials in monomials_by_degree.items():
        for monomial in monomials:
            variables = "".join(sorted(list(set(monomial))))
            if variables not in monomials_by_variables:
                monomials_by_variables[variables] = []
            monomials_by_variables[variables].append(monomial)


    simplified_monomials = []
    for variables, monomials in monomials_by_variables.items():
        monomials_coefficients = Counter([m.replace("-", "") for m in monomials])
        for monomial, coefficient in monomials_coefficients.items():
            if coefficient > 0:
                simplified_monomials.append(f"{coefficient}{variables}")
            elif coefficient < 0:
                simplified_monomials.append(f"{coefficient}{variables}")


    simplified_monomials.sort()

    simplified_polynomial = "+".join(simplified_monomials)
    if simplified_polynomial[0] == "+":
        simplified_polynomial = simplified_polynomial[1:]
    return simplified_polynomial

if __name__ == "__main__":

    test_cases = [
        "3x-zx+2xy-x",
        "cb+cba",
        "2xy-yx",
        "-a+5ab+3a-c-2a",
        "-abc+3a+2ac",
        "xyz-xz",
        "a+ca-ab",
        "xzy+zby",
        "-y+x",
        "x-y"
    ]
    for polynomial in test_cases:
        simplified_polynomial = simplify(polynomial)
        print(f"{polynomial} -> {simplified_polynomial}")
