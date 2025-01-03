# Computor v1

## Description

**Computor v1** est un programme qui résout des équations polynomiales de degré 2 ou inférieur. Il est conçu pour réintroduire les concepts mathématiques de base essentiels à d'autres projets. Ce programme affiche la forme réduite de l'équation, son degré, et ses solutions (y compris l'analyse du discriminant).

---

## Fonctionnalités

- Affiche la **forme réduite** de l'équation.
- Indique le **degré du polynôme**.
- Résout des équations de degré 1 et 2 :
  - Identifie les solutions réelles ou complexes.
  - Analyse le discriminant pour les polynômes quadratiques.

### Exemples

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
