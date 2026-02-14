---
layout: default
---

# Documentation

Ce package contient plusieurs modules utiles pour divers calculs et manipulations de données. Voici un aperçu de leurs fonctionnalités.

**Lien** : [Github](https://github.com/Harlequelrah/Library-ElrahPy/)

## I- Module intkit

### 1. Sous Module `math_primes`

Le module `math_primes` contient des fonctions pour effectuer des opérations liées aux nombres premiers et aux diviseurs.

- `is_prime` : Vérifie si un nombre est premier.

  - **paramètres** :

    - `number` (**int**) : Le nombre entier à vérifier.

  - **sortie** :

    - `bool` : `True` si `number` est premier, sinon `False`.

  - **exemple** :

  ```python
  from elrahpy.intkit.math_primes import is_prime

  result = is_prime(7)  # Résultat : True
  ```

- `factor_products` : Retourne un dictionnaire des facteurs premiers d'un nombre.

  - **paramètres** :

    - `number` (**int**) : Le nombre entier à factoriser.

  - **sortie** :

    - `dict` : Dictionnaire où les clés sont les facteurs premiers et les valeurs sont leurs puissances.

  - **exemple** :

  ```python
  from elrahpy.intkit.math_primes import factor_products

  result = factor_products(18)  # Résultat : {2: 1, 3: 2}
  ```

- `count_dividers` : compte le nombre de diviseurs d'un nombre.

  - **paramètres** :

    - `number` (**int**) : Un entier.

  - **Retourne :**

    - `int` : Nombre total de diviseurs.

  - **exemple** :

  ```python
  from elrahpy.intkit.math_primes import count_dividers

  result = count_dividers(18)  # Résultat : 6
  ```

- `list_dividers` : Retourne la liste des diviseurs d'un nombre.

  - **paramètres** :

    - `number` (**int**) : Le nombre entier dont on veut la liste des diviseurs.

  - **sortie** :

    - `list` : Liste des diviseurs triés en ordre croissant.

  - **exemple** :

  ```python
  from elrahpy.intkit.math_primes import list_dividers

  result = list_dividers(18)  # Résultat : [1, 2, 3, 6, 9, 18]
  ```

### 2. Sous Module `math_utils`

Le module `math_utils` contient des fonctions utilitaires mathématiques.

- **`fibonacci`** : Génère la séquence de Fibonacci jusqu'à une limite donnée.

  - **paramètres :**

    - `n` (**int**) : La limite supérieure pour générer la séquence de Fibonacci.

  - **sortie** :

    - `list[int]` : Liste contenant la séquence de Fibonacci jusqu'à `n`.

  - **exemple** :

  ```python
  from elrahpy.intkit.math_utils import fibonacci

  result = fibonacci(10)  # Résultat : [0, 1, 1, 2, 3, 5, 8]
  ```

## II- Module utils

### 1. Sous-module `datekit`

Le sous-module `datekit` contient des fonctions utiles pour les dates.

- `is_bisectile` : Renvoie `True` si c'est une année bissextile et `False` sinon.

  - **paramètre :**

    - year ( **int** ) : L'année pour laquelle on veut vérifier si elle est bisectile .

  - **sortie :**

    - **bool** : True si l'année est bissextile, sinon False.

  - **exemple** :

  ```python
  from elrahpy.utils.datekit import is_bisectile

  result = is_bisectile(2020)  # Résultat : True
  ```

- `get_interval` : Renvoie un entier ou un tuple d'entier d' intervalle de temps d'une date de début à une date de fin.

  - **paramètres :**

    - `start_date` ( **int** ) : La date de début.

    - `end_date` ( **int** ) : La date de fin (aujourdhui par défaut).

    - `interval_type` (str, optionnel) : Le type d'intervalle à renvoyer. Peut prendre les valeurs suivantes :
      - "year" | "y" : Renvoie l'intervalle en années.
      - "month" | "m" : Renvoie l'intervalle en mois.
      - "day" | "d" : Renvoie l'intervalle en jours.

  - **sortie :**

    - `int` ou `(day,month,year)` : Le nombre d'années, de mois ou de jours selon le type spécifié ou un tuple des trois .

  - **exemple :**

```python
from elrahpy.utils.datekit import get_interval
from datetime import datetime
# Date du jour : 10/10/25
result_years = get_interval(start_date=datetime(2025,1,1), "year")
# Résultat : 0
result_months = get_interval(start_date=datetime(2025,1,1), "month")
# Résultat : 9
result_days = get_interval(start_date=datetime(2025,1,1), "day")
# Résultat : 282
result_days = get_interval(start_date=datetime(2025,1,1),end_date=datetime(2025,10,10))
# Résultat : (0,9,282)
```

### 2. Sous Module `fileskit`

Le sous-module `fileskit` contient des fonctions pour gérer les opérations sur les fichiers.

- `rewrite_content` : Recopie le contenu d'un fichier source vers un fichier de destination en plusieurs blocs.

  - **paramètres :**

    - `ficher_source` (**str**) : Le chemin du fichier source à recopier.

    - `ficher_destination` (**str**) : Le chemin du fichier de destination.

  - **sortie :**

    - `None` : La fonction ne retourne rien.

  - **exemple** :

```python
  from elrahpy.utils.fileskit import rewrite_content

  rewrite_content("source.txt", "destination.txt")  # Copie le contenu de source.txt à destination.txt
```

- `reset_file(file)` : Efface le contenu d'un fichier.

  - **Paramètre :**

    - `file` (**str**) : Le chemin du fichier dont le contenu doit être effacé.

  - **Retourne :**

    - `None` : La fonction ne retourne rien.

  - **exemple** :

```python
from elrahpy.utils.fileskit import reset_file
 reset_file("file.txt")  # Efface le contenu de file.txt
```

- `read_line` : Lit une ligne spécifique d'un fichier.

  - **paramètre :**

    - `file` (str) : Le chemin du fichier à lire.

    - `line` (int) : Le numéro de la ligne à lire.

  - **sortie :**

    - `None` : La fonction ne retourne rien.

  - **exemple** :

  ```python
  from elrahpy.fileskit.filestools import  read_line
  read_line"file.txt", 3)  # Lit la 3ème ligne de file.txt
  ```

- `replace_line` : Remplace le contenu d'une ligne à une position précise.

  - **paramètres**:

    - `file` (**str**) : Le chemin du fichier à lire.

    - `line` (**int**) : Le numéro de la ligne à remplacer.

    - `line_content` (**str**) : Le nouveau contenu de la ligne.

  - **sortie :**

    - `None` : La fonction ne retourne rien.

  - **exemple** :

```python
from elrahpy.utils.fileskit import replace_line
replace_line("file.txt", 1, "Nouvelle ligne 1")  # Remplace la 1ère ligne de file.txt par "Nouvelle ligne 1"
```

- `insert_line `: Insère une ligne à une position précise.

  - **paramètres :**

    - `file` (**str**) : Le chemin du fichier à lire.

    - `line` (**int**) : Le numéro de la ligne à insèrer.

    - `line_content` (**str**) : Le nouveau contenu de la ligne.

  - **sortie :**

    - `None` : La fonction ne retourne rien.

  - **exemple** :

```python
from elrahpy.utils.fileskit import insert_line
insert_line("file.txt", 2, "Ligne insérée")  # Insère "Ligne insérée" à la 2ème position de file.txt
```

- `delete_line `: Supprime une ligne à une position précise.

  - **paramètres :**

    - `file` (**str**) : Le chemin du fichier à lire.

    - `line` (**int**) : Le numéro de la ligne à supprimer.

  - **sortie :**

    - `None` : La fonction ne retourne rien.

  - **exemple** :

```python
from elrahpy.utils.fileskit import delete_line
delete_line("file.txt", 2)
# Suppression de la ligne à la 2ème position de file.txt
```

- `delete_line_startswith `: Supprime les lignes commençant par un marqueur.

  - **paramètres :**

    - `file` (**str**) : Le chemin du fichier à lire.

    - `marker` (**str**) : Le marqueur.

  - **sortie :**

    - `None` : La fonction ne retourne rien.

  - **exemple** :

```python
from elrahpy.utils.fileskit import delete_line_startswith
delete_line_startswith(file="file.txt",marker="@")
# Suppression des lignes de file.txt commençant par @
```

## III- Module `turtlekit`

### 1. Sous-module `geometric_shape`

Le sous-module `geometric_shape` permet de dessiner des formes géométrique

- `figure` : Tracer une forme géométrique avec des couleurs différentes.

  - **paramètres** :

    - `nbr_figure` : **int** - Nombre de figures à tracer

    - `rayon` : **int** - Rayon de chaque figure

    - `nbr_cote` : **int|None** - Nombre de côtés (None pour un cercle)

    - `position` : **list[Tuple[int, int]]** - Liste des positions de chaque figure

    - `couleur` : **list[str]** - Liste des couleurs pour chaque figure

    - `orientation` : **int** - Orientation initiale des figures

  - **sortie** : `None`

  - **exemple** :

```python
from elrahpy.turtlekit.geometric_shape import figure

figure(
    nbr_figure=3,
    rayon=50,
    nbr_cote=4,
    position=[(0, 0), (100, 100), (200, 0)],
    couleur=["red", "blue", "green"],
    orientation=0
)
```

- `rectangle` : Dessiner un rectangle.

  - **paramètres** :

    - `L` : **int** - Longueur du rectangle

    - `l` : **int** - Largeur du rectangle

    - `inside_color` : **str** - Couleur de remplissage

    - `line_color` : **str** - Couleur du contour

  - **Retour** : **None**

  - **exemple** :

```python
from elrahpy.turtlekit.geometric_shape import rectangle

rectangle(
    L=100,
    l=50,
    inside_color="yellow",
    line_color="black"
)
```

### 2. Sous-module `particular_shape`

Le sous-module `particular_shape` permet de dessiner des formes particulières

- `heart` : Dessiner un coeur

  - **paramètres** :

    - `inside_color` : `str` - Couleur de remplissage du cœur

    - `line_color` : `str` - Couleur du contour

    - `background_color` : `str` - Couleur de fond

  - **sortie** : `None`

  - **exemple** :

```python
from elrahpy.turtlekit.particular_shape import heart

heart(
    inside_color="red",
    line_color="black",
    background_color="pink"
)
```

## IV- Module `strkit`

### 1. Sous-Module `charscraft`

Le sous-module `charscraft` permet de faire des opérations spécifiques sur les chaines de caractère

- `is_vowel` : verifie si le caractère est une voyelle et en renvoie un boolean

  - **paramètres** :

    - `vowel` (**str**) : le caractère à verifier.

  - **sortie** :

    - `boolean` : `True` si **vowel** est une voyelle et `False` sinon.

    - **exemple** :

```python
   from elrahpy.strkit.charscraft import is_vowel
   is_vowel('a') # Renvoie True
   is_vowel('b') # Renvoie False
```

- `count_vowels` : Renvoie le nombre de voyelles dans une sequence.

  - **paramètres** :

    - `seq` (**str|list|tuple**) : La chaîne de caractères à analyser.

  - **sortie** :

    - `int` : Le nombre de voyelles présentes dans y.

  - **exemple** :

```python
from elrahpy.strkit.charscraft  import count_vowels
count_vowels("exemple") # Renvoie 3
```

- `check_char_case` : Détecte si un caractère est en minuscule, en majuscule, ou aucun des deux.

  - **paramètre** :

    - `char` (**str**) : Le caractère à verifier.

  - **sortie** :

    - `int` : `-1` si `char` est entre minuscule , `1` si char est en majuscule et `0` sinon aucun des deux.

  - **exemple** :

```python
from elrahpy.strkit.charscraft import check_char_case
check_char_case('a') # Renvoie -1
check_char_case('A') # Renvoie 1
check_char_case('1') # Renvoie 0
```

- `generate_uuid_code` : Génère un code uuid.

  - **paramètre** :

    - `prefix` (**str**) : Un préfix .

    - `length` (**int**) : La longueur du code .

  - **sortie** :

    - `str` : Le code uuid

  - **exemple** :

```python
from elrahpy.strkit.charscraft import generate_uuid_code
generate_uuid_code(prefix='MX',length=5) # retourne MX-F9
```

- `ispalindrome` : Vérifie si une chaîne de caractère est un palindrome.

  - **paramètres** :

    - `word` (**str**) : La chaîne de caractère à verifier.

  - **sortie** :

  - `boolean` : `True` si `word` est un palindrome, `False` sinon.

  - **exemple** :

```python
from elrahpy.strkit.charscraft import ispalindrome
ispalindrome("radar") # Renvoie True
ispalindrome("hello") # Renvoie False
```

### 2. Sous-Module `sequencescraft`

Le sous-module `sequencescraft` permet de faire des opérations spécifiques sur les chaines de caractère et sequences.

- `get_all_indexes` : Renvoie une liste contenant les indices de toutes les occurrences d’un élément dans une chaîne de caractères ou une liste.

  - **paramètres** :

    - `seq` (**sequence**) : La chaîne de caractères ou la liste ou la sequence dans laquelle chercher.

    - `element` : L' élément à rechercher .

  - **sortie** :

    - `list[int]` : Une liste d’indices où element apparaît dans le sequence.

  - **exemple** :

```python
from elrahpy.strkit.sequencescraft import get_all_indexes
get_all_indexes("banana", "a") # Renvoie [1, 3, 5]
```

- `remove_all_occurrences` : Supprime toutes les occurrences d’un élément donné dans sequence.

  - **paramètres** :

    - `seq` : La liste ou chaîne à modifier.

    - `element` : L' élément à rechercher .

  - **Retourne** :

  - `list` : La liste ou chaîne de caractères sans les occurrences de element.

  - **exemple** :

```python
  from elrahpy.strkit.sequencescraft remove_all_occurrences
  remove_all_occurrences([1, 2, 3, 2, 4], 2) # Renvoie [1, 3, 4]
```

- `count_letters` : renvoie le nombre d' occurence de chaque lettre dans la chaine .

  - **paramètres** :

    - `txt` (**str**) : La chaîne à analyser.

    - `sensitive`(**bool**) : **True** pour tenir compte de la casse et **False** pour uniformiser la casse

  - **sortie** :

  - `dict[str,int]` : Un dictionnaire avec chaque element et son nombre d’occurrences, ou un entier représentant le nombre d’occurrences de x.

  - **exemple** :

```python
from elrahpy.strkit.sequencescraft import
    count_letters

count_letters("Sirops",sensitive=True)
# Retourne {"S": 1, "i": 1, "o": 1, "p": 1, "r": 1, "s": 1}

count_letters("Sirops",sensitive=False)
# Retourne {"i": 1, "o": 1, "p": 1, "r": 1, "s": 2}

```

- `separate_case` : compte et separe les lettres en fonction de leur casse

  - **paramètres** :

    - `text` : La chaine de caractère .

  - **sortie** :

    - `dict[str,dict]`

  - **exemple** :

```python
from elrahpy.strkit.sequencescraft import separate_case
txt="Hello"
separate_case(txt=txt)
# retourne {
        "lowercase": {"e": 1, "l": 2, "o": 1},
        "uppercase": {"H": 1},
    }

```

## V- Module `cryptokit`

Le sous-module `cryptokit` permet de faire des opérations spécifiques sur le codage par cryptographie.

### 1. Sous-Module `cesar`

Ce sous module contient des utilitaires pour la cryptographie avec la méthode cesar.Ils ne sont valides que les élements de `string.printable`.

- `crypt_cesar` : Encode ou décode un mot en utilisant le chiffrement de César avec une clé de décalage spécifiée.

  - **paramètres** :

    - word ( **str** ) : Le mot à coder ou décoder.

    - operation ( **int** ) : 1 pour coder, -1 pour décoder.

    - k ( **int**) : La clé de décalage pour le chiffrement (par défaut 3).

  - **sortie** :

    - **str** : Le mot codé ou décodé selon le chiffrement de César.

  - **exemple** :

```python
from elrahpy.cryptokit.cesar import crypt_cesar
crypt_cesar("Bonjour", operation=1, k=3) # Encode le mot et renvoie Erqmrxu
crypt_cesar("Erqmrxu", operation=-1, k=3) # Decode le mot et renvoie Bonjour
```

- `verify_cesar` : Vérifie la correspondance entre un mot en texte claire et un mot crypté.

  - **paramètres** :

    - word ( **str** ) : Le mot en claire.

    - crypted_word ( **str** ) : Le mot en crypté.

    - k ( **int**) : La clé de décalage pour le chiffrement .

  - **sortie** :

    - `bool` : Un booléen .

  - **exemple** :

```python
from elrahpy.cryptokit.cesar import verify_cesar
verify_cesar(word="Bonjour",crypted_word="Erqmrxu",k=3)
# Renvoie True
```

- `search_cesar` : Décrypte un mot codé en utilisant le chiffrement de César et renvoie un dictionnaire des possibilités en fonction de chaque décalage possible.

  - **paramètres** :

    - word ( **str** ) : Le mot à déchiffrer.

  - **sortie** :

    - `dict` : Un dictionnaire où chaque clé est une possibilité de mot clair et la valeur correspond au décalage.

  - **exemple** :

```python
from elrahpy.cryptokit.cesar import search_cesar
search_cesar("Erqmrxu")
# Renvoie toutes les possibilités de décodage ex : {'Erqmrxu': 0, 'Dqplqwt': 1, 'Cpokpvs': 2, 'Bonjour': 3,...}
```

- `z_cesar` : Décrypte une phrase ou une chaîne codée en utilisant le chiffrement de César, en renvoyant un dictionnaire des décryptages possibles pour chaque mot de la chaîne.

  - **paramètres** :

    - chaine (**str**) : La chaîne de caractères codée à analyser .

  - **sortie** :

    - `dict` : Un dictionnaire où chaque clé est un décalage et chaque valeur est la chaîne possible pour ce décalage.

  - **exemple** :

```python
from elrahpy.cryptokit.cesar import z_cesar
z_cesar("Erqmrxu Phz") # Renvoie un dictionnaire des possibilités de mots clairs pour chaque mot de la chaîne ex :{0: 'Erqmrxu Phz', 1: 'Dqplqwt Ogy', 2: 'Cpokpvs Nfx', 3: 'Bonjour Mew'....}
```

## VI- Module `typeskit`

Ce module comporte des classes et types utilitaires .

### 1. Sous Module `landmark`

Ce sous module comporte les classes LandMark et Point

**`Point`**

- `__init__`:

  - **paramètres** :

    - x : **int** représente l'abscisse

    - y : **int** représente l'ordonnée

**`LandMark`** :

- `__init__` :

  - **paramètres** :

    - type_land_mark: **type** , default : Any

- marks: **dict[Point,type_land_mark]** , un dictionnaire de point et valeur.

- `get_point_value` : retourne la valeur au point du repère à partir d'un point .

  - **paramètres** :

    - point : **Point**

- `set_point_value` : change la valeur d'un point

  - **paramètres** :

    - point : **Point**

    - obj : **type_land_mark**

- `add_point` : ajoute un point et sa valeur

  - **paramètres** :

    - point : **Point**

    - obj : **type_land_mark**

- `is_valid_obj` : verifie si un objet est valide du type **type_land_mark**

  - **paramètres** :

    - obj : **type_land_mark**

  - **sortie** : **bool** -

- `exist_point` : verifie si un point existe

  - **paramètres** :

    - point : **Point**

  - **sortie** : **bool**

- `remove_point` : retire un point du repère

  - **paramètres** :

    - point : **Point**

- `list_marks` : liste les coordonnées et leurs valeurs

`ex` :

```python
my_land = LandMark()
my_land.add_point(Point(2,5),55)
my_land.list_marks()
my_land.set_point_value(Point(2,5),"mdr")
my_land.list_marks()
my_land.remove_point(Point(2,5))
my_land.list_marks()


new_land = LandMark(type_land_mark=int)
new_land.add_point(Point(1,2),2)
new_land.add_point(Point(2,3),3)
new_land.list_marks()
new_land.add_point(Point(1,2),"hi") # Provoque une erreur
```
