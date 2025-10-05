# Étape 3 : Les Entrées Utilisateur

## IMPORTANT: Réactiver votre environnement virtuel

Avant de commencer cette étape, réactivons l'environnement virtuel.

### Commande 1 : Aller dans votre dossier de projet

`cd mon_projet_python`{{execute}}

---

### Commande 2 : Activer l'environnement virtuel

`source venv/bin/activate`{{execute}}

**VÉRIFICATION:**
Vous devez voir `(venv)` au début de votre ligne!

```
(venv) root@host:~/mon_projet_python#
```

---

## Rendre les programmes interactifs!

Jusqu'à présent, nous avons créé des variables avec des valeurs fixes. Mais que faire si nous voulons obtenir des informations de l'utilisateur? C'est là qu'intervient `input()`!

---

## La fonction input()

La fonction `input()` vous permet de poser des questions aux utilisateurs:

```python
nom_variable = input("Votre question: ")
```

**Important:** `input()` retourne TOUJOURS du texte (string), même si l'utilisateur tape un nombre!

---

## EXERCICE 1 : Votre premier programme interactif

### ÉTAPE 1 - Créer un nouveau fichier

Cliquez ici pour créer le fichier:

`interactif.py`{{open}}

---

### ÉTAPE 2 - Copier ce code

Copiez ce code dans votre fichier `interactif.py`:

```python
# Demander le nom de l'utilisateur
prenom = input("Quel est votre prénom? ")

# Afficher un message personnalisé
print("Bonjour, " + prenom + "! Bienvenue dans Python!")
print("Ravi de vous rencontrer, " + prenom)
```

---

### ÉTAPE 3 - Exécuter le programme

`python3 interactif.py`{{execute}}

Tapez votre prénom quand on vous le demande et appuyez sur Entrée!

**RÉSULTAT ATTENDU:**
```
Quel est votre prénom? Julie
Bonjour, Julie! Bienvenue dans Python!
Ravi de vous rencontrer, Julie
```

---

## EXERCICE 2 : Obtenir des nombres de l'utilisateur

**ATTENTION:** `input()` retourne toujours du TEXTE. Si vous avez besoin d'un nombre, vous devez le convertir!

### Convertir les types de données

```python
# Convertir texte en nombre entier
age = int(input("Entrez votre âge: "))

# Convertir texte en nombre décimal
taille = float(input("Entrez votre taille en mètres: "))
```

---

### ÉTAPE 1 - Essayez ce code

Dans votre fichier `interactif.py`, **ajoutez ce code à la fin**:

```python
# Obtenir l'âge de l'utilisateur et calculer l'année de naissance
age = int(input("Quel âge avez-vous? "))
annee_actuelle = 2025
annee_naissance = annee_actuelle - age

print("Vous êtes né(e) en", annee_naissance, "environ")
```

---

### ÉTAPE 2 - Exécuter à nouveau

`python3 interactif.py`{{execute}}

**EXEMPLE D'UTILISATION:**
```
Quel âge avez-vous? 20
Vous êtes né(e) en 2005 environ
```

---

## ATTENTION: Erreurs courantes

### Erreur #1: Oublier de convertir

```python
# FAUX - On ne peut pas faire des maths avec du texte!
age = input("Âge: ")
age_futur = age + 1  # ERREUR!

# CORRECT - Convertir d'abord
age = int(input("Âge: "))
age_futur = age + 1  # Fonctionne! ✓
```

---

### Erreur #2: Convertir du texte en nombre

```python
# Ceci va planter si l'utilisateur tape "vingt"!
age = int(input("Âge: "))  # Utilisateur tape "vingt" = ERREUR
```

**Solution:** Toujours dire aux utilisateurs quel format vous attendez!

---

## EXERCICE 3 : Calculatrice personnelle

Créez un programme qui:
1. Demande deux nombres
2. Les convertit en nombres décimaux (float)
3. Les additionne
4. Affiche le résultat

### ÉTAPE 1 - Dans `interactif.py`, ajoutez:

```python
# Calculatrice simple
print("\n=== CALCULATRICE ===")
nombre1 = float(input("Entrez le premier nombre: "))
nombre2 = float(input("Entrez le deuxième nombre: "))
somme = nombre1 + nombre2

print("La somme est:", somme)
```

---

### ÉTAPE 2 - Testez

`python3 interactif.py`{{execute}}

**EXEMPLE:**
```
=== CALCULATRICE ===
Entrez le premier nombre: 5.5
Entrez le deuxième nombre: 3.2
La somme est: 8.7
```

---

## Plusieurs entrées à la suite

Vous pouvez obtenir plusieurs informations:

```python
prenom = input("Prénom: ")
age = input("Âge: ")
ville = input("Ville: ")

print(f"{prenom} a {age} ans et habite à {ville}")
```

**Astuce:** Le `f""` s'appelle une f-string - une façon moderne de formater du texte!

**Exemple:**
```python
nom = "Julie"
age = 25
print(f"Je m'appelle {nom} et j'ai {age} ans")
# Résultat: Je m'appelle Julie et j'ai 25 ans
```

---

## EXERCICE 4 : Profil complet

Créez un nouveau fichier qui demande:
- Prénom
- Âge (à convertir en int)
- Ville
- Hobby préféré

Puis affichez tout dans un message joli!

**Essayez par vous-même avant de regarder la solution ci-dessous!**

---

### Solution possible:

```python
print("=== CRÉATION DE PROFIL ===\n")

prenom = input("Votre prénom: ")
age = int(input("Votre âge: "))
ville = input("Votre ville: ")
hobby = input("Votre hobby préféré: ")

print("\n=== VOTRE PROFIL ===")
print(f"Prénom: {prenom}")
print(f"Âge: {age} ans")
print(f"Ville: {ville}")
print(f"Hobby: {hobby}")
print(f"\nMerci {prenom}! Profil créé avec succès!")
```

---

## Points clés à retenir

- `input()` obtient du texte des utilisateurs
- Retourne TOUJOURS une string (texte)
- Utilisez `int()` pour convertir en nombre entier
- Utilisez `float()` pour convertir en nombre décimal
- Dites toujours aux utilisateurs quel format vous attendez
- Les f-strings `f""` rendent le formatage facile

---

Prêt pour un vrai défi? Cliquez sur "Continuer" pour l'étape finale!
