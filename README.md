# Computor v1

## Description

**Computor v1** is a program that solves polynomial equations of degree 2 or lower. It is designed to reintroduce fundamental mathematical concepts essential for other projects. This program displays the reduced form of the equation, its degree, and its solutions (including discriminant analysis).

---

## Features

- Displays the **reduced form** of the equation.
- Indicates the **degree of the polynomial**.
- Solves equations of degree 1 and 2:
  - Identifies real or complex solutions.
  - Analyzes the discriminant for quadratic polynomials.

### Examples

```bash
$ ./computor "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly positive, the two solutions are:
0.905239
-0.475131

$ ./computor "5 * X^0 + 4 * X^1 = 4 * X^0"
Reduced form: 1 * X^0 + 4 * X^1 = 0
Polynomial degree: 1
The solution is:
-0.25

$ ./computor "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
Reduced form: 5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0
Polynomial degree: 3
The polynomial degree is strictly greater than 2, I can't solve.
```
