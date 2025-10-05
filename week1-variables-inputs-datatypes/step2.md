# Étape 2 : Les Types de Données en Python

## Qu'est-ce qu'un type de données?

Imaginez que vous rangez des choses dans différentes boîtes:
- Une boîte pour les **mots** (votre nom, une phrase)
- Une boîte pour les **nombres entiers** (votre âge, 1, 2, 3...)
- Une boîte pour les **nombres décimaux** (votre taille: 1.75m, un prix: 19.99€)
- Une boîte pour **Vrai ou Faux** (es-tu étudiant? Oui/Non)

En Python, ces "boîtes" sont appelées des **types de données**.

---

## Les 4 types de données essentiels

### 1. String (str) - Le Texte

C'est pour stocker des mots, des phrases, du texte. **TOUJOURS avec des guillemets!**

```python
prenom = "Marie"
message = 'Bonjour le monde'
ville = "Paris"
```

Vous pouvez utiliser `"` ou `'` - les deux fonctionnent!

---

### 2. Integer (int) - Les Nombres Entiers

C'est pour les nombres SANS virgule. **SANS guillemets!**

```python
age = 25
annee = 2025
nombre_etudiants = 30
```

---

### 3. Float - Les Nombres Décimaux

C'est pour les nombres AVEC virgule (on utilise un **point**, pas une virgule!)

```python
prix = 19.99
taille = 1.75
temperature = 36.6
```

**ATTENTION:** En Python, on écrit `1.75` (avec un point), PAS `1,75` !

---

### 4. Boolean (bool) - Vrai ou Faux

C'est pour dire si quelque chose est VRAI ou FAUX. Attention aux majuscules!

```python
est_etudiant = True
a_termine = False
```

**IMPORTANT:** 
- `True` avec un T majuscule
- `False` avec un F majuscule

---

## EXERCICE 1 : Créer différents types de variables

### ÉTAPE 1 - Ouvrir un nouveau fichier

Cliquez ici pour créer un nouveau fichier:

`types_donnees.py`{{open}}

---

### ÉTAPE 2 - Copier ce code

Copiez TOUT ce code dans le fichier `types_donnees.py`:

```python
# Variables de type String (texte)
nom_etudiant = "Alex Dupont"
langue_preferee = "Python"

# Variables de type Integer (nombres entiers)
age_etudiant = 20
nombre_cours = 5

# Variables de type Float (nombres décimaux)
moyenne = 15.75
prix_formation = 99.99

# Variables de type Boolean (Vrai/Faux)
est_inscrit = True
a_fini_cours = False

# Afficher toutes les informations
print("===== PROFIL ÉTUDIANT =====")
print("Nom:", nom_etudiant)
print("Âge:", age_etudiant, "ans")
print("Moyenne:", moyenne, "/20")
print("Inscrit:", est_inscrit)
```

---

### ÉTAPE 3 - Exécuter le programme

Cliquez ici pour exécuter:

`python3 types_donnees.py`{{execute}}

**CE QUE VOUS DEVRIEZ VOIR:**
```
===== PROFIL ÉTUDIANT =====
Nom: Alex Dupont
Âge: 20 ans
Moyenne: 15.75 /20
Inscrit: True
```

---

## EXERCICE 2 : Vérifier les types

Python a une fonction magique pour vérifier le type d'une variable : `type()`

### ÉTAPE 1 - Ajouter du code de vérification

**Ajoutez ces lignes** à la fin de votre fichier `types_donnees.py`:

```python
# Vérifier les types
print("\n===== VÉRIFICATION DES TYPES =====")
print("Type de 'nom_etudiant':", type(nom_etudiant))
print("Type de 'age_etudiant':", type(age_etudiant))
print("Type de 'moyenne':", type(moyenne))
print("Type de 'est_inscrit':", type(est_inscrit))
```

---

### ÉTAPE 2 - Exécuter à nouveau

`python3 types_donnees.py`{{execute}}

**RÉSULTAT ATTENDU:**
```
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

**Explication:**
- `str` = String (texte)
- `int` = Integer (nombre entier)
- `float` = Float (nombre décimal)
- `bool` = Boolean (vrai/faux)

---

## EXERCICE 3 : À votre tour! Créez votre profil

Maintenant, vous allez créer vos propres variables. Suivez ces instructions:

### ÉTAPE 1 - Dans le fichier `types_donnees.py`, ajoutez VOTRE profil:

**Ajoutez ces lignes à la fin du fichier:**

```python
# MON PROFIL PERSONNEL
print("\n===== MON PROFIL =====")

# Créez vos propres variables ici:
mon_prenom = "VotrePrenom"           # Remplacez par votre prénom
mon_age = 20                          # Remplacez par votre âge
ma_taille = 1.70                      # Remplacez par votre taille en mètres
j_aime_programmer = True              # True si vous aimez, False sinon

# Afficher votre profil
print("Prénom:", mon_prenom)
print("Âge:", mon_age, "ans")
print("Taille:", ma_taille, "m")
print("J'aime programmer:", j_aime_programmer)
```

---

### ÉTAPE 2 - Personnalisez les valeurs

**Remplacez:**
- `"VotrePrenom"` par votre vrai prénom (gardez les guillemets!)
- `20` par votre âge (sans guillemets!)
- `1.70` par votre taille (sans guillemets, avec un point!)
- `True` ou `False` selon si vous aimez programmer

---

### ÉTAPE 3 - Exécutez

`python3 types_donnees.py`{{execute}}

---

## ATTENTION : Erreur courante!

### FAUX (avec guillemets, ce sera du texte):
```python
age = "25"           # C'est du TEXTE, pas un nombre!
```

### CORRECT (sans guillemets, c'est un nombre):
```python
age = 25             # C'est un NOMBRE, on peut faire des calculs!
```

**RÈGLE:** Si vous mettez des guillemets autour d'un nombre, Python va le considérer comme du TEXTE!

---

## Test rapide : Devinez le type!

**Question 1:** Quel est le type de `x = "123"` ?
<details>
<summary>Réponse</summary>
String (texte) - car il y a des guillemets!
</details>

**Question 2:** Quel est le type de `y = 123` ?
<details>
<summary>Réponse</summary>
Integer (nombre entier) - pas de guillemets!
</details>

**Question 3:** Quel est le type de `z = 12.3` ?
<details>
<summary>Réponse</summary>
Float (nombre décimal) - il y a un point!
</details>

---

## Points clés à retenir:

- **String** = Texte avec guillemets `"texte"`
- **Integer** = Nombre entier sans guillemets `25`
- **Float** = Nombre décimal avec point `25.5`
- **Boolean** = `True` ou `False` (attention aux majuscules!)
- `type()` vous dit le type d'une variable

---

Prêt pour les entrées utilisateur? Cliquez sur "Continuer"!
