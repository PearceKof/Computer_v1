import re
import sys
from fractions import Fraction

def parse_equation(equation):
    terms = {}

    leftSide, rightSide = equation.split('=')

    print(f"left = {leftSide} rigth= {rightSide}")
    pattern = r'([-+]?)\s*([\d.]+)\s*\*\s*X\^([0-9]+)'

    def add_term(match, side):
        
        coefficient = Fraction(match.group(1) + match.group(2)) * (1 if side == "left" else -1)
        exponent = int(match.group(3))
        print(f"the match is {match}, exponant {exponent} and coefficient {coefficient}")
        terms[exponent] = terms.get(exponent, 0) + coefficient

    for match in re.finditer(pattern, leftSide):
        add_term(match, "left")

    for match in re.finditer(pattern, rightSide):
        add_term(match, "right")
    
    print(f"terms: {terms}")
    return terms

def reduced_form(terms):
    """Generate the reduced form of the polynomial."""
    if not terms:
        return "0 = 0"

    result = 0
    sorted_terms = sorted(terms.items(), key=lambda x: x[0])
    result = " + ".join(f"{float(c) if c.denominator != 1 else c.numerator} * X^{e}" for e, c in sorted_terms if c != 0)
    result = result.replace("+ -", "- ")
    if (result):
        return result + " = 0"
    return "0 = 0"

def get_polynomial_degree(terms):
    if not terms:
        return 0
    return max((e for e, c in terms.items() if c != 0), default=0)

def solve_equation(terms):
    degree = get_polynomial_degree(terms)

    print(f"degree= {degree}")
    if degree > 2:
        return "The polynomial degree is strictly greater than 2, I can't solve."
    
    if degree == 0:
        if 0 in terms and terms[0] == 0:
            return "Each real number is a solution."
        return "No solution."
    
    if degree == 1:
        a = terms.get(1,0)
        b = terms.get(0,0)

        aExp = terms.get(2,1)
        bExp = terms.get(1,1)

        if (a == 0 and b == 0) or (aExp == 0 and bExp == 0):
            return "Each real number is a solution."
        
        if a == 0:
            return "No solution."
        
        print(f"a= {a} et b= {b}")
        return (f"The solution is:\n{float(-b / a)}")
    
    if degree == 2:
        a = terms.get(2,0)
        b = terms.get(1,0)
        c = terms.get(0,0)

        aExp = terms.get(2,1)
        bExp = terms.get(1,1)
        cExp = terms.get(0,1)

        if (a == 0 and b == 0 and c == 0) or (aExp == 0 and bExp == 0 and cExp == 0):
            return "Each real number is a solution."

        if a == 0:
            return "No solution."
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            first_solution = (-b - discriminant ** 0.5) / (2 * a)
            second_solution =  (-b + discriminant ** 0.5) / (2 * a)
            return f"Discriminant is strictly positive, the two solutions are:\n{first_solution}\n{second_solution}"
        if discriminant == 0:
            return f"The solution is:\n{float(-b / (2*a))}"
        else:
            real_part = -b / (2 * a)
            imaginary_part = (-discriminant) ** 0.5 / (2 * a)
            return (f"Discriminant is strictly negative, the two complex solutions are:\n"
                    f"{real_part} + {imaginary_part}i\n"
                    f"{real_part} - {imaginary_part}i")



    

def main():
    if len(sys.argv) != 2:
        print("Usage: ./Computer_v1 \"equation here\"")
    
    equation = sys.argv[1]
    try:
        terms = parse_equation(equation)
        reduced = reduced_form(terms)
        
        print(f"Reduced form: {reduced}")
        print(f"Polynomial degree: {get_polynomial_degree(terms)}")

        solution = solve_equation(terms)
        print(solution)

    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()