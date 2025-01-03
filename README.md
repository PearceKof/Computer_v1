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
```
### Prérequis
Python 3.x : nécessaire pour exécuter le programme.
Une distribution compatible Linux, macOS ou Windows avec Python installé.
### Installation
### Télécharger le script :

### Clonez le dépôt :
bash
Copier le code
git clone <repository-url>
cd <repository-directory>
Ou téléchargez directement le fichier computor.py.
Rendre le script exécutable :

bash
Copier le code
chmod +x computor.py
(Optionnel) Installer Python : Si Python n'est pas installé sur votre système, suivez les instructions sur le site officiel :
https://www.python.org/downloads/

Utilisation
Pour exécuter le programme, lancez-le avec une équation comme argument :

bash
Copier le code
./computor.py "équation ici"
Exemple
bash
Copier le code
./computor.py "3 * X^2 - 4 * X^1 + 1 * X^0 = 0"
Fonctionnement
Analyse de l'équation :

Sépare les termes à gauche et à droite du =.
Calcule les coefficients pour chaque degré.
Forme réduite :

Réorganise et affiche l'équation sous forme simplifiée.
Calcul du degré :

Détecte le degré maximal avec un coefficient non nul.
Résolution :

Résout selon le degré :
Degré 0 : aucune ou une infinité de solutions.
Degré 1 : solution unique.
Degré 2 : solutions basées sur le discriminant.
Limitations
Ne résout pas les équations de degré supérieur à 2.
Les termes doivent respecter un format strict (a * X^p).
