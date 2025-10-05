# Étape 2 : Les Types de Données en Python

## IMPORTANT: Réactiver votre environnement virtuel

À chaque nouvelle étape, on réactive l'environnement virtuel. C'est comme rallumer la lumière quand on change de pièce!

### Commande 1 : Aller dans votre dossier

`cd mon_projet_python`{{execute}}

### Commande 2 : Activer l'environnement

`source venv/bin/activate`{{execute}}

**VÉRIFICATION OBLIGATOIRE:**

Vous DEVEZ voir `(venv)` au début de votre ligne:

```
(venv) root@host:~/mon_projet_python#
```

Parfait? On continue!

---

## Qu'est-ce qu'un type de données?

**Imaginez votre chambre avec différentes boîtes:**

- Une boîte **ROUGE** pour les vêtements (seulement des vêtements)
- Une boîte **BLEUE** pour les livres (seulement des livres)
- Une boîte **VERTE** pour les jouets (seulement des jouets)

**En programmation, c'est pareil!**

Python a différents **types** de boîtes (variables) pour différents **types** de données:

- Une boîte pour le **TEXTE** (votre nom, une phrase)
- Une boîte pour les **NOMBRES ENTIERS** (1, 2, 3, 100...)
- Une boîte pour les **NOMBRES DÉCIMAUX** (3.14, 19.99, 1.75)
- Une boîte pour **VRAI ou FAUX** (oui/non, activé/désactivé)

**Pourquoi c'est important?**

Parce qu'on ne peut pas faire les mêmes choses avec du texte et des nombres!
- Avec des nombres: on peut calculer (5 + 3 = 8)
- Avec du texte: on ne peut PAS calculer ("Bonjour" + "Au revoir" ≠ un calcul mathématique)

---

## Les 4 types de données essentiels

### TYPE 1: String (str) - Le Texte

**C'est quoi?** Du texte, des mots, des phrases.

**Comment le reconnaître?** Il y a TOUJOURS des guillemets autour: `"..."` ou `'...'`

**Exemples:**
```python
prenom = "Marie"
ville = "Paris"
message = "Bonjour le monde!"
email = 'contact@exemple.fr'
```

**RÈGLE D'OR:** Si c'est du texte → Mettez des guillemets!

---

### TYPE 2: Integer (int) - Les Nombres Entiers

**C'est quoi?** Des nombres SANS virgule, SANS point décimal.

**Comment le reconnaître?** Juste des chiffres, PAS de guillemets, PAS de point.

**Exemples:**
```python
age = 25
annee = 2025
nombre_etudiants = 30
temperature = -5
```

**RÈGLE D'OR:** Si c'est un nombre entier → Pas de guillemets, pas de point!

---

### TYPE 3: Float - Les Nombres Décimaux

**C'est quoi?** Des nombres AVEC un point décimal (la virgule en Python, c'est un POINT!)

**Comment le reconnaître?** Des chiffres avec un `.` (point) au milieu.

**Exemples:**
```python
prix = 19.99
taille = 1.75
temperature = 36.6
pi = 3.14
```

**ATTENTION:** En Python, on écrit `1.75` (avec un POINT), PAS `1,75` (avec une virgule)!

**RÈGLE D'OR:** Si c'est un nombre décimal → Utilisez un POINT, pas une virgule!

---

### TYPE 4: Boolean (bool) - Vrai ou Faux

**C'est quoi?** Une réponse à une question oui/non, vrai/faux, activé/désactivé.

**Comment le reconnaître?** Seulement deux valeurs possibles: `True` ou `False`

**Exemples:**
```python
est_etudiant = True
a_termine = False
est_majeur = True
aime_python = True
```

**ATTENTION AUX MAJUSCULES:**
- ✅ CORRECT: `True` (T majuscule)
- ❌ FAUX: `true` (tout en minuscules)
- ✅ CORRECT: `False` (F majuscule)
- ❌ FAUX: `false` (tout en minuscules)

**RÈGLE D'OR:** Boolean = True ou False (avec la première lettre en MAJUSCULE!)

---

## Récapitulatif visuel

```python
# STRING (texte) - AVEC guillemets
nom = "Julie"

# INTEGER (nombre entier) - SANS guillemets, SANS point
age = 25

# FLOAT (nombre décimal) - AVEC un point
taille = 1.75

# BOOLEAN (vrai/faux) - True ou False
est_etudiant = True
```

**Facile à retenir:**
- Texte → Guillemets
- Nombre entier → Rien
- Nombre décimal → Point
- Vrai/Faux → True ou False

---

## EXERCICE 1 : Créer des variables de différents types

Maintenant, pratiquons! Nous allons créer un programme avec les 4 types de données.

### ÉTAPE 1.1 - Ouvrir nano pour créer un nouveau fichier

**EXÉCUTEZ:**

`nano types_donnees.py`{{execute}}

**Ce qui se passe:** Nano s'ouvre avec un nouveau fichier vide `types_donnees.py`

---

### ÉTAPE 1.2 - Taper le code complet

**ACTION REQUISE:** Dans nano, tapez TOUT ce code (prenez votre temps!):

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

**CONSEILS:**
- Tapez ligne par ligne
- Appuyez sur `Entrée` à chaque nouvelle ligne
- Vérifiez bien les guillemets pour le texte
- Vérifiez bien le point pour les décimaux (15.75)
- Vérifiez bien les majuscules pour True/False

**SI VOUS FAITES UNE ERREUR:**
- Utilisez les flèches pour revenir
- Utilisez `Backspace` pour effacer
- Retapez correctement

---

### ÉTAPE 1.3 - Comprendre ce code

Avant de continuer, comprenons ce qu'on a tapé:

**Lignes avec `#`:** Des commentaires pour expliquer

**Lignes 2-3:** Deux variables de type **String** (texte)
- `nom_etudiant` contient "Alex Dupont"
- `langue_preferee` contient "Python"

**Lignes 6-7:** Deux variables de type **Integer** (nombres entiers)
- `age_etudiant` contient 20
- `nombre_cours` contient 5

**Lignes 10-11:** Deux variables de type **Float** (décimaux)
- `moyenne` contient 15.75
- `prix_formation` contient 99.99

**Lignes 14-15:** Deux variables de type **Boolean** (vrai/faux)
- `est_inscrit` contient True
- `a_fini_cours` contient False

**Lignes 17-22:** Des `print()` pour afficher tout ça!

**Compris?** Super! Sauvegardons maintenant!

---

### ÉTAPE 1.4 - Sauvegarder le fichier

**ACTION REQUISE:**

**1.** Appuyez sur: `Ctrl + O`
**2.** Appuyez sur: `Entrée`
**3.** Vous voyez: `[ Wrote X lines ]`

Parfait! Le fichier est sauvegardé!

---

### ÉTAPE 1.5 - Quitter nano

**ACTION REQUISE:**

Appuyez sur: `Ctrl + X`

Vous revenez au terminal!

---

### ÉTAPE 1.6 - Exécuter le programme

**EXÉCUTEZ:**

`python3 types_donnees.py`{{execute}}

**RÉSULTAT ATTENDU:**

```
===== PROFIL ÉTUDIANT =====
Nom: Alex Dupont
Âge: 20 ans
Moyenne: 15.75 /20
Inscrit: True
```

**SI VOUS VOYEZ ÇA:** 🎉 Bravo! Vous avez créé des variables de 4 types différents!

---

## EXERCICE 2 : Vérifier les types avec type()

Python a une fonction magique: `type()` qui vous dit quel type de données c'est!

### ÉTAPE 2.1 - Rouvrir le fichier

**EXÉCUTEZ:**

`nano types_donnees.py`{{execute}}

Vous voyez votre code précédent dans nano.

---

### ÉTAPE 2.2 - Aller en bas du fichier

**ACTION REQUISE:**

1. Appuyez plusieurs fois sur la flèche `↓` (bas)
2. Arrêtez-vous APRÈS la dernière ligne (`print("Inscrit:", est_inscrit)`)
3. Appuyez sur `Entrée` DEUX fois (pour faire un espace)

---

### ÉTAPE 2.3 - Ajouter le code de vérification

**ACTION REQUISE:** Tapez ces lignes:

```python
# Vérifier les types
print()
print("===== VÉRIFICATION DES TYPES =====")
print("Type de 'nom_etudiant':", type(nom_etudiant))
print("Type de 'age_etudiant':", type(age_etudiant))
print("Type de 'moyenne':", type(moyenne))
print("Type de 'est_inscrit':", type(est_inscrit))
```

**Explication:**
- `print()` tout seul = ligne vide (pour aérer)
- `type(nom_etudiant)` = demande à Python: "C'est quoi le type de cette variable?"

---

### ÉTAPE 2.4 - Sauvegarder et quitter

**ACTION REQUISE:**

1. `Ctrl + O` puis `Entrée` → Sauvegarder
2. `Ctrl + X` → Quitter

---

### ÉTAPE 2.5 - Exécuter le programme modifié

**EXÉCUTEZ:**

`python3 types_donnees.py`{{execute}}

**RÉSULTAT ATTENDU:**

```
===== PROFIL ÉTUDIANT =====
Nom: Alex Dupont
Âge: 20 ans
Moyenne: 15.75 /20
Inscrit: True

===== VÉRIFICATION DES TYPES =====
Type de 'nom_etudiant': <class 'str'>
Type de 'age_etudiant': <class 'int'>
Type de 'moyenne': <class 'float'>
Type de 'est_inscrit': <class 'bool'>
```

**Traduction:**
- `<class 'str'>` = String (texte)
- `<class 'int'>` = Integer (nombre entier)
- `<class 'float'>` = Float (nombre décimal)
- `<class 'bool'>` = Boolean (vrai/faux)

**Bravo!** Vous savez maintenant vérifier les types!

---

## EXERCICE 3 : Créez VOTRE profil personnel

À votre tour! Vous allez créer vos propres variables avec VOS informations.

### ÉTAPE 3.1 - Rouvrir le fichier

**EXÉCUTEZ:**

`nano types_donnees.py`{{execute}}

---

### ÉTAPE 3.2 - Aller en bas du fichier

**ACTION REQUISE:**

1. Flèches `↓` pour aller tout en bas
2. Appuyez sur `Entrée` TROIS fois (pour bien séparer)

---

### ÉTAPE 3.3 - Taper VOTRE code personnel

**ACTION REQUISE:** Tapez ce code, mais REMPLACEZ les valeurs par VOS informations:

```python
# MON PROFIL PERSONNEL
print()
print("===== MON PROFIL =====")

# Créez vos propres variables ici:
mon_prenom = "VotrePrenom"
mon_age = 20
ma_taille = 1.70
j_aime_programmer = True

# Afficher votre profil
print("Prénom:", mon_prenom)
print("Âge:", mon_age, "ans")
print("Taille:", ma_taille, "m")
print("J'aime programmer:", j_aime_programmer)
```

**MAINTENANT, MODIFIEZ:**

**Ligne `mon_prenom = "VotrePrenom"`:**
- Remplacez `VotrePrenom` par votre VRAI prénom
- **GARDEZ les guillemets!**
- Exemple: `mon_prenom = "Ahmed"` ou `mon_prenom = "Sophie"`

**Ligne `mon_age = 20`:**
- Remplacez `20` par votre âge réel
- **PAS de guillemets!**
- Exemple: `mon_age = 25` ou `mon_age = 18`

**Ligne `ma_taille = 1.70`:**
- Remplacez `1.70` par votre taille en mètres
- **Utilisez un POINT!**
- Exemple: `ma_taille = 1.75` ou `ma_taille = 1.82`

**Ligne `j_aime_programmer = True`:**
- Mettez `True` si vous aimez programmer
- Mettez `False` si vous n'aimez pas (c'est OK!)
- **Attention à la majuscule!**

---

### ÉTAPE 3.4 - Sauvegarder et quitter

1. `Ctrl + O` puis `Entrée`
2. `Ctrl + X`

---

### ÉTAPE 3.5 - Exécuter et voir VOTRE profil

**EXÉCUTEZ:**

`python3 types_donnees.py`{{execute}}

**VOUS DEVEZ VOIR:**

Tout le résultat précédent + votre profil personnel à la fin!

**Exemple:**
```
===== MON PROFIL =====
Prénom: Ahmed
Âge: 22 ans
Taille: 1.78 m
J'aime programmer: True
```

**SI VOUS VOYEZ VOTRE PROFIL:** 🎉 Excellent! Vous maîtrisez les types de données!

---

## ⚠️ ATTENTION: Erreur courante numéro 1

**PIÈGE:** Les guillemets transforment TOUT en texte!

```python
# FAUX - Ceci est du TEXTE, pas un nombre!
age = "25"

# CORRECT - Ceci est un NOMBRE
age = 25
```

**Comment savoir?**
- `"25"` avec guillemets = texte (String)
- `25` sans guillemets = nombre (Integer)

**Test rapide:**
```python
age_texte = "25"
age_nombre = 25

print(type(age_texte))    # <class 'str'> ← TEXTE!
print(type(age_nombre))   # <class 'int'> ← NOMBRE!
```

**Règle:** Si vous voulez faire des calculs, N'UTILISEZ PAS de guillemets!

---

## ⚠️ ATTENTION: Erreur courante numéro 2

**PIÈGE:** En Python, les décimaux utilisent un POINT, pas une virgule!

```python
# FAUX - Python ne comprend pas la virgule
prix = 19,99  # ERREUR!

# CORRECT - Utilisez un point
prix = 19.99  # BON!
```

**Pourquoi?**

Parce qu'en anglais (langue de Python), on écrit "19.99" pas "19,99"!

**Règle:** Pour les décimaux, TOUJOURS un point `.` jamais une virgule `,`

---

## ⚠️ ATTENTION: Erreur courante numéro 3

**PIÈGE:** Les majuscules comptent pour True et False!

```python
# FAUX
reponse = true   # Python ne reconnaît pas "true"
reponse = TRUE   # Python ne reconnaît pas "TRUE"

# CORRECT
reponse = True   # T majuscule, reste minuscule
reponse = False  # F majuscule, reste minuscule
```

**Règle:** Boolean = `True` ou `False` (première lettre en MAJUSCULE!)

---

## Mini-Quiz : Devinez le type!

**Question 1:** Quel est le type de `x = "123"` ?

<details>
<summary>Cliquez pour voir la réponse</summary>

**Réponse:** String (texte)

**Pourquoi?** Il y a des guillemets! Même si c'est des chiffres, les guillemets en font du TEXTE.
</details>

---

**Question 2:** Quel est le type de `y = 123` ?

<details>
<summary>Cliquez pour voir la réponse</summary>

**Réponse:** Integer (nombre entier)

**Pourquoi?** Pas de guillemets, pas de point décimal = nombre entier!
</details>

---

**Question 3:** Quel est le type de `z = 12.3` ?

<details>
<summary>Cliquez pour voir la réponse</summary>

**Réponse:** Float (nombre décimal)

**Pourquoi?** Il y a un point décimal!
</details>

---

**Question 4:** Quel est le type de `a = True` ?

<details>
<summary>Cliquez pour voir la réponse</summary>

**Réponse:** Boolean (vrai/faux)

**Pourquoi?** C'est le mot spécial `True`!
</details>

---

## Récapitulatif : Les 4 types essentiels

| Type | Exemple | Avec quoi? | Pour quoi? |
|------|---------|------------|------------|
| **String** | `"Marie"` | Guillemets | Texte, mots, phrases |
| **Integer** | `25` | Rien | Nombres entiers |
| **Float** | `19.99` | Point | Nombres décimaux |
| **Boolean** | `True` | Majuscule | Vrai ou Faux |

**Aide-mémoire:**
```python
# Les 4 types en un coup d'œil
texte = "Bonjour"      # String
entier = 42            # Integer
decimal = 3.14         # Float
vrai_faux = True       # Boolean
```

---

## Conseil de professeur expérimenté

**Choisissez toujours le BON type pour vos données!**

**Exemples:**

✅ **BON:**
```python
age = 25              # Integer (on ne fait pas d'opérations avec des décimales sur l'âge)
prix = 19.99          # Float (un prix a souvent des centimes)
```

❌ **MAUVAIS:**
```python
age = 25.0            # Float inutile (l'âge est toujours entier)
nombre_enfants = 2.5  # Float impossible (on ne peut pas avoir 2.5 enfants!)
```

**Règle d'or:** Réfléchissez à ce que représente votre donnée dans la vraie vie!

---

## Prêt pour la suite?

Vous savez maintenant:
- ✅ Les 4 types de données essentiels
- ✅ Comment créer chaque type
- ✅ Comment vérifier le type avec `type()`
- ✅ Les erreurs courantes à éviter

**Bravo!** Vous progressez super bien!

**Prochaine étape:** Apprendre à obtenir des informations de l'utilisateur avec `input()`!

Cliquez sur "Continuer" →
