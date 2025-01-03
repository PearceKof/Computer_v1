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

## Examples

```bash
$ ./computor "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
Polynomial degree: 2
Discriminant is strictly positive, the two solutions are:
0.905239
-0.475131
```
```bash
$ ./computor "5 * X^0 + 4 * X^1 = 4 * X^0"
Reduced form: 1 * X^0 + 4 * X^1 = 0
Polynomial degree: 1
The solution is:
-0.25
```
```bash
$ ./computor "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
Reduced form: 5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0
Polynomial degree: 3
The polynomial degree is strictly greater than 2, I can't solve.
```

## Requirements

  - Python 3.x: Required to run the program.
  - A compatible Linux, macOS, or Windows system with Python installed.

## How to run it

### Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>

```
Or directly download the computor.py file.

### Make the script executable:

```bash
chmod +x computor.py
(Optional) Install Python:
```

### (Optional) Install Python:

If Python is not installed on your system, follow the instructions on the official website:
https://www.python.org/downloads/

## Usage

To execute the program, run it with an equation as an argument:

```bash
./computor.py "your equation here"
```

### Example

```bash
./computor.py "3 * X^2 - 4 * X^1 + 1 * X^0 = 0"
```

## How It Works

### Equation Parsing:

- Splits the terms on the left and right sides of the =.
- Computes the coefficients for each degree.

### Reduced Form:

- Reorganizes and displays the equation in a simplified form.

  
### Degree Calculation:

- Detects the highest degree with a non-zero coefficient.
  
### Solving:

Solves based on the degree:
- Degree 0: No solutions or infinite solutions.
- Degree 1: Unique solution.
- Degree 2: Solutions based on the discriminant.

###  Limitations
- Does not solve equations of degree higher than 2.
- Terms must follow a strict format (a * X^p).
