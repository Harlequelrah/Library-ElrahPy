# Harlequelrah

Passionné par la programmation et le développement en Python, je crée une bibliothèque personnalisée pour renforcer mes compétences, améliorer ma productivité et partager mon expertise avec la communauté.

## Installation

- **Avec GitHub :**

  ```bash
  git clone https://github.com/Harlequelrah/Library-harlequelrah_py
  ```

- **Avec pip :**

  ```bash
  pip install harlequelrah_py
  ```

## Utilisation

Ce package contient plusieurs modules utiles pour divers calculs et manipulations de données. Voici un aperçu de leurs fonctionnalités.

### Module integer

#### 1. Sous Module `base_converter`

Le module `base_converter` contient des fonctions pour effectuer des conversions de base numérique.

- **`binary(x)`** : Convertit un nombre entier en une chaîne de caractères représentant sa valeur en binaire sans le préfixe `0b`.

  ```python
  from harlequelrah_py.base_converter import binary

  result = binary(10)  # Résultat : 1010
  ```

  - **Paramètre :**
    - `x` (int) : Le nombre entier à convertir en binaire.
  - **Retourne :**
    - `int` : La représentation binaire sans le préfixe `0b`.

- **`base_format(n, f)`** : Convertit un nombre entier `n` en fonction de la base spécifiée par `f`.

  ```python
  from harlequelrah_py.base_converter import base_format

  result_bin = base_format(10, "b")  # Résultat : "1010"
  result_hex = base_format(10, "h")  # Résultat : "a"
  result_dec = base_format(10, "d")  # Résultat : "10"
  ```

  - **Paramètres :**
    - `n` (int) : Le nombre entier à convertir.
    - `f` (str) : Le format de base à utiliser pour la conversion. Peut prendre les valeurs suivantes :
      - `"b"` : Convertit `n` en binaire.
      - `"h"` : Convertit `n` en hexadécimal.
      - `"d"` : Convertit `n` en décimal.

### 2. Sous Module `math_primes`

Le module `math_primes` contient des fonctions pour effectuer des opérations liées aux nombres premiers et aux diviseurs.

- **`prem(nbr)`** : Vérifie si un nombre est premier.

  ```python
  from harlequelrah_py.math_primes import prem

  result = prem(7)  # Résultat : True
  ```

  - **Paramètre :**
    - `nbr` (int) : Le nombre entier à vérifier.
  - **Retourne :**
    - `bool` : `True` si `nbr` est premier, sinon `False`.

- **`prd_fct(nbr)`** : Retourne un dictionnaire des facteurs premiers d'un nombre.

  ```python
  from harlequelrah_py.math_primes import prd_fct

  result = prd_fct(18)  # Résultat : {2: 1, 3: 2}
  ```

  - **Paramètre :**
    - `nbr` (int) : Le nombre entier à factoriser.
  - **Retourne :**
    - `dict` : Dictionnaire où les clés sont les facteurs premiers et les valeurs sont leurs puissances.

- **`nbr_div(nbr)`** : Calcule le nombre de diviseurs d'un nombre.

  ```python
  from harlequelrah_py.math_primes import nbr_div

  result = nbr_div(36)  # Résultat : 9
  ```

  - **Paramètre :**
    - `nbr` (int) : Le nombre entier à analyser.
  - **Retourne :**
    - `int` : Nombre total de diviseurs.

- **`list_div(nbr)`** : Retourne la liste des diviseurs d'un nombre.

  ```python
  from harlequelrah_py.math_primes import list_div

  result = list_div(36)  # Résultat : [1, 2, 3, 4, 6, 9, 12, 18, 36]
  ```

  - **Paramètre :**
    - `nbr` (int) : Le nombre entier dont on veut la liste des diviseurs.
  - **Retourne :**
    - `list` : Liste des diviseurs triée en ordre croissant.

### 3. Sous Module `math_utils`

Le module `math_utils` contient des fonctions utilitaires mathématiques.

- **`fibonacci(n)`** : Génère la séquence de Fibonacci jusqu'à une limite donnée.

  ```python
  from harlequelrah_py.math_utils import fibonacci

  result = fibonacci(10)  # Résultat : [0, 1, 1, 2, 3, 5, 8]
  ```

  - **Paramètre :**
    - `n` (int) : La limite supérieure pour générer la séquence de Fibonacci.
  - **Retourne :**
    - `list` : Liste contenant la séquence de Fibonacci jusqu'à `n`.

- **`fct(n)`** : Calcule le factoriel d'un nombre.

  ```python
  from harlequelrah_py.math_utils import fct

  result = fct(5)  # Résultat : 120
  ```

  - **Paramètre :**
    - `n` (int) : Le nombre entier pour lequel on veut calculer le factoriel.
  - **Retourne :**
    - `int` : Le factoriel de `n`.

### Module date

### 1. Sous-module `clock`

Le sous-module `clock` contient des fonctions pour la gestion des dates et des heures.

- **is_bisectile(year)** : Renvoie `True` si c'est une année bissextile et `False` sinon.

  ```python
  from harlequelrah_py.date.clock import is_bisectile

  result = is_bisectile(2020)  # Résultat : True
  ```

  - **Paramètre :**
    - year (int) : L année pour laquelle on veut vérifier si elle est bisectile
  -**Retourne:**
    - bool : True si l'année est bissextile, sinon False.

- **interval(birthday_year, birthday_month, birthday_day, type=None) :** Renvoie un intervalle de temps d'une date à aujourd'hui.

```python
from harlequelrah_py.date.clock import interval

result_years = interval(1990, 5, 15, "year")  # Résultat : (nombre d'années depuis 1990-05-15)
result_months = interval(1990, 5, 15, "month")  # Résultat : (nombre de mois depuis 1990-05-15)
result_days = interval(1990, 5, 15, "day")  # Résultat : (nombre de jours depuis 1990-05-15)
```

  - **Paramètres :**
    - birthday_year (int) : L'année de naissance.
    - birthday_month (int) : Le mois de naissance.
    - birthday_day (int) : Le jour de naissance.
    - type (str, optionnel) : Le type d'intervalle à renvoyer. Peut prendre les valeurs suivantes :
      - "year" ou "y" : Renvoie l'intervalle en années.
      - "month" ou "m" : Renvoie l'intervalle en mois.
      - "day" ou "d" : Renvoie l'intervalle en jours.
  - **Retourne :**
    - int ou None : Le nombre d'années, de mois ou de jours selon le type spécifié, ou None si le type n'est pas reconnu.

# Module files

## Sous-module myfiles

Le sous-module `myfiles` contient des fonctions pour gérer les opérations sur les fichiers.

- **recopie(ficher_source, ficher_destination, debit)** : Recopie le contenu d'un fichier source vers un fichier de destination en plusieurs blocs.

  ```python
  from harlequelrah_py.files.myfiles import recopie

  recopie("source.txt", "destination.txt", 1024)  # Copie le contenu de source.txt à destination.txt
  ```

  - **Paramètres :**
    - ficher_source (str) : Le chemin du fichier source à recopier.
    - ficher_destination (str) : Le chemin du fichier de destination.
    - debit (int) : Le nombre de caractère à recopier à chaque fois.
  - **Retourne :**
    - None : La fonction ne retourne rien.

  - **filereset(file) : Efface le contenu d'un fichier.**

  ```python
  from harlequelrah_py.files.myfiles import filereset
   filereset("file.txt")  # Efface le contenu de file.txt
  ```

  - **Paramètre :**
    - file (str) : Le chemin du fichier dont le contenu doit être effacé.
  - **Retourne :**
    - None : La fonction ne retourne rien.

  - **rline(file, line) : Lit une ligne spécifique d'un fichier (le premier indice est 1).**

  ```python
  from harlequelrah_py.files.myfiles import rline
  rline("file.txt", 3)  # Lit la 3ème ligne de file.txt
  ```

  - **Paramètre :**
    - file (str) : Le chemin du fichier à lire.
    - line (int) : Le numéro de la ligne à lire.
  - **Retourne :**
    - None : La fonction ne retourne rien.

  -**delfile(file, element) : Efface toutes les lignes d'un fichier commençant par un élément en particulier.**

  ```python
  from harlequelrah_py.files.myfiles import delfile
  delfile("file.txt", "#")  # Efface toutes les lignes de file.txt qui commencent par "#"
  ```

  - **Paramètre :**
    - file (str) : Le chemin du fichier à lire.
    - element (str) : L'élément par lequel les lignes à effacer commencent.
  - **Retourne :**
    -None : La fonction ne retourne rien.

- **repline(file, line, line_content) : Remplace le contenu d'une ligne à une position précise.**

```python
from harlequelrah_py.files.myfiles import repline
repline("file.txt", 1, "Nouvelle ligne 1")  # Remplace la 1ère ligne de file.txt par "Nouvelle ligne 1"
```

  - **Paramètre :**
    - file (str) : Le chemin du fichier à lire.
    - line (int) : Le numéro de la ligne à remplacer.
    - line_content (str) : Le nouveau contenu de la ligne.
  - **Retourne :**
    - None : La fonction ne retourne rien.

- **insline(file, line, line_content) : Insère une ligne à une position précise.**

```python
from harlequelrah_py.files.myfiles import insline
insline("file.txt", 2, "Ligne insérée")  # Insère "Ligne insérée" à la 2ème position de file.txt
```

  - **Paramètre :**
    - file (str) : Le chemin du fichier à lire.
    - line (int) : Le numéro de la ligne à inserer.
    - line_content (str) : Le nouveau contenu de la ligne.
  -**Retourne :**
    -None : La fonction ne retourne rien.

### Module `turtle`

#### Sous-module `geometric_shape`

1. **Tracer une forme géométrique avec des couleurs différentes**

   Fonction : `figure(nbr_figure, rayon, nbr_cote=None, position=[], couleur=[], orientation=0)`

   Exemple d'utilisation :

   ```python
   from geometric_shape import figure

   figure(
       nbr_figure=3,
       rayon=50,
       nbr_cote=4,
       position=[(0, 0), (100, 100), (200, 0)],
       couleur=["red", "blue", "green"],
       orientation=0
   )
   ```

   - **Paramètres** :
       - `nbr_figure` : `int` - Nombre de figures à tracer
       - `rayon` : `int` - Rayon de chaque figure
       - `nbr_cote` : `Optional[int]` - Nombre de côtés (None pour un cercle)
       - `position` : `List[Tuple[int, int]]` - Liste des positions de chaque figure
       - `couleur` : `List[str]` - Liste des couleurs pour chaque figure
       - `orientation` : `int` - Orientation initiale des figures
   - **Retour** : `None`

2. **Dessiner un rectangle**

   Fonction : `rectangle(L, l, inside_color="white", line_color="black")`

   Exemple d'utilisation :

   ```python
   from geometric_shape import rectangle

   rectangle(
       L=100,
       l=50,
       inside_color="yellow",
       line_color="black"
   )
   ```

   - **Paramètres** :
       - `L` : `int` - Longueur du rectangle
       - `l` : `int` - Largeur du rectangle
       - `inside_color` : `str` - Couleur de remplissage
       - `line_color` : `str` - Couleur du contour
   - **Retour** : `None`


#### Sous-module `particular_shape`

1. **Dessiner un cœur**

   Fonction : `heart(inside_color="white", line_color="black", background_color="white")`

   Exemple d'utilisation :

   ```python
   from particular_shape import heart

   heart(
       inside_color="red",
       line_color="black",
       background_color="pink"
   )
   ```

   - **Paramètres** :
       - `inside_color` : `str` - Couleur de remplissage du cœur
       - `line_color` : `str` - Couleur du contour
       - `background_color` : `str` - Couleur de fond
   - **Retour** : `None`


## Contact ou Support

Pour des questions ou du support, contactez-moi à maximeatsoudegbovi@gmail.com ou au (+228) 91 36 10 29.






