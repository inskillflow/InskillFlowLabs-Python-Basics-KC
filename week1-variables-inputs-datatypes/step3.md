# Étape 3 : Les Entrées Utilisateur

## IMPORTANT: Réactiver votre environnement virtuel

Nouvelle étape = on réactive l'environnement virtuel!

### Commande 1 : Aller dans votre dossier

`cd mon_projet_python`{{execute}}

### Commande 2 : Activer l'environnement

`source venv/bin/activate`{{execute}}

**VÉRIFICATION:**

Vous voyez `(venv)` ?
```
(venv) root@host:~/mon_projet_python#
```

Parfait! On y va!

---

## Rendre vos programmes INTERACTIFS!

**Jusqu'à maintenant, vos programmes étaient comme ça:**

```python
prenom = "Julie"  # Vous tapez le nom DANS le code
print(prenom)
```

**Problème:** Si vous voulez changer de prénom, il faut MODIFIER le code et RÉEXÉCUTER le programme!

**Solution:** Demander à l'utilisateur de taper son prénom QUAND le programme s'exécute!

**C'est ça, un programme interactif!** 🎮

---

## La fonction magique : input()

`input()` = demander quelque chose à l'utilisateur

**Analogie simple:**

Imaginez un guichet de banque:
- **L'employé vous demande:** "Quel est votre nom?"
- **Vous répondez:** "Julie Dupont"
- **L'employé note** votre réponse

En Python:
- **Le programme demande:** `input("Quel est votre nom? ")`
- **L'utilisateur tape:** Julie Dupont
- **Python stocke** la réponse dans une variable

---

## Syntaxe de base

```python
nom_variable = input("Votre question ici: ")
```

**Exemple concret:**

```python
prenom = input("Quel est votre prénom? ")
print("Bonjour", prenom)
```

**Ce qui se passe:**
1. Python affiche: "Quel est votre prénom? "
2. Le curseur clignote, attend que vous tapiez
3. Vous tapez votre prénom et appuyez sur `Entrée`
4. Python met votre réponse dans la variable `prenom`
5. Python affiche: "Bonjour Julie" (ou le prénom que vous avez tapé)

---

## ⚠️ RÈGLE SUPER IMPORTANTE

**`input()` retourne TOUJOURS du TEXTE (String)!**

Même si l'utilisateur tape un nombre, Python le voit comme du TEXTE!

```python
age = input("Votre âge: ")
# Si l'utilisateur tape: 25
# Python voit: "25" (TEXTE, pas le nombre 25)
```

**Pourquoi c'est important?**

Parce qu'on ne peut pas faire de calculs avec du texte!

```python
age = input("Votre âge: ")  # Utilisateur tape: 25
age_futur = age + 1  # ERREUR! On ne peut pas faire "25" + 1
```

**Solution:** On verra ça dans 2 minutes! 😉

---

## EXERCICE 1 : Votre premier programme interactif

Créons un programme qui demande votre prénom et vous salue!

### ÉTAPE 1.1 - Ouvrir nano

**EXÉCUTEZ:**

`nano interactif.py`{{execute}}

Nano s'ouvre avec un nouveau fichier vide.

---

### ÉTAPE 1.2 - Taper le code

**ACTION REQUISE:** Dans nano, tapez ce code:

```python
# Programme interactif simple
print("===== PROGRAMME DE SALUTATION =====")
print()

# Demander le prénom de l'utilisateur
prenom = input("Quel est votre prénom? ")

# Afficher un message personnalisé
print()
print("Bonjour,", prenom, "!")
print("Bienvenue dans le monde de Python!")
print("Ravi de vous rencontrer,", prenom, "!")
```

**Prenez votre temps!** Vérifiez bien chaque ligne.

---

### ÉTAPE 1.3 - Comprendre le code

**Ligne 5:** `prenom = input("Quel est votre prénom? ")`
- `input(...)` = demande à l'utilisateur
- La question entre guillemets = ce qui s'affiche
- La réponse est stockée dans `prenom`

**Lignes 9-11:** Affichent des messages avec le prénom
- `print("Bonjour,", prenom, "!")` = affiche "Bonjour, [le prénom tapé], !"

**Compris?** Super! Sauvegardons!

---

### ÉTAPE 1.4 - Sauvegarder et quitter

1. `Ctrl + O` puis `Entrée` → Sauvegarder
2. `Ctrl + X` → Quitter

---

### ÉTAPE 1.5 - Exécuter le programme

**EXÉCUTEZ:**

`python3 interactif.py`{{execute}}

**CE QUI SE PASSE:**

1. Vous voyez: `===== PROGRAMME DE SALUTATION =====`
2. Puis: `Quel est votre prénom?`
3. Le curseur clignote et ATTEND!

**ACTION REQUISE:**

**Tapez votre prénom** (exemple: Julie) puis appuyez sur `Entrée`

**RÉSULTAT ATTENDU:**

```
===== PROGRAMME DE SALUTATION =====

Quel est votre prénom? Julie

Bonjour, Julie !
Bienvenue dans le monde de Python!
Ravi de vous rencontrer, Julie !
```

**SI VOUS VOYEZ ÇA:** 🎉 Bravo! Votre premier programme interactif fonctionne!

**Testez encore!** Relancez `python3 interactif.py` et tapez un AUTRE prénom!

---

## Obtenir des NOMBRES de l'utilisateur

**Grand problème:** `input()` retourne toujours du TEXTE!

**Exemple du problème:**

```python
age = input("Votre âge: ")  # Utilisateur tape: 25
# Python voit: age = "25" (TEXTE)

age_futur = age + 10  # ERREUR! "25" + 10 ne marche pas!
```

**Solution:** CONVERTIR le texte en nombre!

---

## Les fonctions de conversion

Python a des fonctions pour transformer un type en un autre:

**1. `int()` = Convertit en Integer (nombre entier)**

```python
texte = "25"
nombre = int(texte)
# nombre vaut maintenant 25 (le nombre, pas le texte)
```

**2. `float()` = Convertit en Float (nombre décimal)**

```python
texte = "19.99"
nombre = float(texte)
# nombre vaut maintenant 19.99 (le nombre, pas le texte)
```

---

## Comment utiliser input() avec des nombres

**MÉTHODE:** Convertir IMMÉDIATEMENT après input()

**Pour un nombre entier:**

```python
age = int(input("Votre âge: "))
```

**Décomposons:**
1. `input("Votre âge: ")` → Demande à l'utilisateur, retourne du texte
2. `int(...)` → Convertit ce texte en nombre entier
3. `age = ...` → Stocke le nombre dans la variable

**Pour un nombre décimal:**

```python
taille = float(input("Votre taille en mètres: "))
```

---

## EXERCICE 2 : Calculer l'année de naissance

Créons un programme qui calcule votre année de naissance!

### ÉTAPE 2.1 - Rouvrir le fichier

**EXÉCUTEZ:**

`nano interactif.py`{{execute}}

---

### ÉTAPE 2.2 - Aller en bas

**ACTION REQUISE:**

1. Flèches `↓` pour aller tout en bas du fichier
2. Appuyez sur `Entrée` TROIS fois (pour bien séparer)

---

### ÉTAPE 2.3 - Ajouter le nouveau code

**ACTION REQUISE:** Tapez ces lignes:

```python
# Calculateur d'année de naissance
print()
print("===== CALCULATEUR D'ANNÉE DE NAISSANCE =====")

# Demander l'âge (et CONVERTIR en nombre!)
age = int(input("Quel âge avez-vous? "))

# Calculer l'année de naissance
annee_actuelle = 2025
annee_naissance = annee_actuelle - age

# Afficher le résultat
print("Vous êtes né(e) en", annee_naissance, "environ.")
```

**ATTENTION:** Regardez bien la ligne `age = int(input(...))` !
- On ENTOURE `input()` avec `int()`
- Comme ça, `age` devient un NOMBRE, pas du texte
- On peut faire des calculs avec!

---

### ÉTAPE 2.4 - Sauvegarder et quitter

1. `Ctrl + O` puis `Entrée`
2. `Ctrl + X`

---

### ÉTAPE 2.5 - Exécuter

**EXÉCUTEZ:**

`python3 interactif.py`{{execute}}

**UTILISATION:**

1. Tapez votre prénom quand demandé
2. Plus bas, tapez votre âge (exemple: 25)
3. Regardez le résultat!

**EXEMPLE:**

```
Quel âge avez-vous? 25
Vous êtes né(e) en 2000 environ.
```

**SI ÇA MARCHE:** 🎉 Excellent! Vous savez maintenant convertir en nombre!

---

## ⚠️ ERREUR COURANTE: Oublier de convertir

**PROBLÈME:**

```python
age = input("Âge: ")  # age = "25" (TEXTE)
futur = age + 1       # ERREUR! "25" + 1 impossible!
```

**MESSAGE D'ERREUR:**
```
TypeError: can only concatenate str (not "int") to str
```

**TRADUCTION:** "Erreur: tu essaies d'ajouter un nombre à du texte!"

**SOLUTION:**

```python
age = int(input("Âge: "))  # age = 25 (NOMBRE)
futur = age + 1             # 25 + 1 = 26 ✓ Ça marche!
```

**RÈGLE D'OR:** Si vous voulez faire des calculs, utilisez `int()` ou `float()`!

---

## ⚠️ ERREUR COURANTE: L'utilisateur tape du texte au lieu d'un nombre

**PROBLÈME:**

```python
age = int(input("Âge: "))
# Si l'utilisateur tape: "vingt" au lieu de 20
# Python ne peut pas convertir "vingt" en nombre!
```

**MESSAGE D'ERREUR:**
```
ValueError: invalid literal for int()
```

**TRADUCTION:** "Erreur: je ne peux pas transformer 'vingt' en nombre!"

**SOLUTION:** Dites CLAIREMENT à l'utilisateur qu'il doit taper un NOMBRE!

```python
age = int(input("Votre âge (tapez un NOMBRE): "))
```

Ou encore mieux:

```python
age = int(input("Votre âge en chiffres (exemple: 25): "))
```

---

## EXERCICE 3 : Calculatrice simple

Créons une petite calculatrice qui additionne deux nombres!

### ÉTAPE 3.1 - Rouvrir le fichier

`nano interactif.py`{{execute}}

---

### ÉTAPE 3.2 - Aller en bas et ajouter

**ACTION REQUISE:** Allez en bas, 3x `Entrée`, puis tapez:

```python
# Calculatrice simple
print()
print("===== CALCULATRICE SIMPLE =====")

# Demander deux nombres
print("Je vais additionner deux nombres pour vous!")
nombre1 = float(input("Premier nombre: "))
nombre2 = float(input("Deuxième nombre: "))

# Calculer la somme
somme = nombre1 + nombre2

# Afficher le résultat
print()
print(nombre1, "+", nombre2, "=", somme)
```

**REMARQUES:**
- On utilise `float()` pour accepter aussi les décimaux (19.5, 3.14, etc.)
- La variable `somme` contient le résultat du calcul
- On affiche tout joli à la fin!

---

### ÉTAPE 3.3 - Sauvegarder, quitter, exécuter

1. `Ctrl + O` puis `Entrée`
2. `Ctrl + X`
3. `python3 interactif.py`{{execute}}

**UTILISATION:**

```
===== CALCULATRICE SIMPLE =====
Je vais additionner deux nombres pour vous!
Premier nombre: 5.5
Deuxième nombre: 3.2

5.5 + 3.2 = 8.7
```

**SI ÇA MARCHE:** 🎉 Génial! Vous avez créé une calculatrice!

---

## Technique avancée : Les f-strings

Il existe une manière MODERNE et ÉLÉGANTE d'afficher des variables: les **f-strings**.

**Ancienne méthode:**

```python
nom = "Julie"
age = 25
print("Je m'appelle", nom, "et j'ai", age, "ans")
```

**Nouvelle méthode (f-string):**

```python
nom = "Julie"
age = 25
print(f"Je m'appelle {nom} et j'ai {age} ans")
```

**Comment ça marche?**

1. Mettez un `f` AVANT les guillemets: `f"..."`
2. Mettez les variables entre accolades `{}`  : `{nom}`, `{age}`
3. Python remplace automatiquement!

**Résultat:** Exactement le même, mais le code est plus joli!

---

## EXERCICE 4 : Carte d'identité interactive avec f-strings

Créons un programme qui crée votre carte d'identité!

### ÉTAPE 4.1 - Créer un nouveau fichier

`nano carte_identite.py`{{execute}}

---

### ÉTAPE 4.2 - Taper le programme complet

**ACTION REQUISE:** Tapez TOUT ce code (prenez votre temps!):

```python
# Carte d'identité interactive
print("="*40)
print("CRÉATION DE CARTE D'IDENTITÉ")
print("="*40)
print()

# Demander toutes les informations
prenom = input("Votre prénom: ")
nom = input("Votre nom: ")
age = int(input("Votre âge: "))
ville = input("Votre ville: ")
pays = input("Votre pays: ")

# Afficher la carte d'identité
print()
print("="*40)
print("         CARTE D'IDENTITÉ")
print("="*40)
print(f"Prénom:  {prenom}")
print(f"Nom:     {nom}")
print(f"Âge:     {age} ans")
print(f"Ville:   {ville}")
print(f"Pays:    {pays}")
print("="*40)
print()
print(f"Merci {prenom} {nom}!")
print("Votre carte d'identité est créée.")
```

**ASTUCES DANS CE CODE:**
- `"="*40` = répète le symbole `=` 40 fois (pour faire joli!)
- Les f-strings rendent l'affichage super propre
- On mélange texte et input()

---

### ÉTAPE 4.3 - Sauvegarder, quitter, exécuter

1. `Ctrl + O` puis `Entrée`
2. `Ctrl + X`
3. `python3 carte_identite.py`{{execute}}

**EXEMPLE D'UTILISATION:**

```
========================================
CRÉATION DE CARTE D'IDENTITÉ
========================================

Votre prénom: Ahmed
Votre nom: Benali
Votre âge: 22
Votre ville: Casablanca
Votre pays: Maroc

========================================
         CARTE D'IDENTITÉ
========================================
Prénom:  Ahmed
Nom:     Benali
Âge:     22 ans
Ville:   Casablanca
Pays:    Maroc
========================================

Merci Ahmed Benali!
Votre carte d'identité est créée.
```

**C'EST BEAU, NON?** 🎨

---

## Récapitulatif : input() en 5 points

**1. Pour du TEXTE (pas de conversion):**
```python
prenom = input("Votre prénom: ")
```

**2. Pour un nombre ENTIER (conversion avec int):**
```python
age = int(input("Votre âge: "))
```

**3. Pour un nombre DÉCIMAL (conversion avec float):**
```python
taille = float(input("Votre taille: "))
```

**4. Dites TOUJOURS à l'utilisateur ce que vous attendez:**
```python
age = int(input("Votre âge en chiffres: "))  # ✓ Clair!
age = int(input("Age: "))                     # ✗ Pas assez clair
```

**5. Les f-strings rendent l'affichage plus joli:**
```python
print(f"Bonjour {prenom}, vous avez {age} ans!")
```

---

## Tableau récapitulatif

| Ce que vous voulez | Commande | Exemple |
|-------------------|----------|---------|
| Texte simple | `input(...)` | `nom = input("Nom: ")` |
| Nombre entier | `int(input(...))` | `age = int(input("Age: "))` |
| Nombre décimal | `float(input(...))` | `prix = float(input("Prix: "))` |
| Afficher joliment | f-string | `print(f"Bonjour {nom}!")` |

---

## Conseil de professeur expérimenté

**Testez TOUJOURS votre programme avec différentes entrées!**

Quand vous créez un programme interactif, essayez:
- Des valeurs normales (âge: 25)
- Des valeurs limites (âge: 0, âge: 120)
- Des valeurs négatives (âge: -5)
- Du texte quand vous attendez un nombre

**Pourquoi?** Pour voir où votre programme peut "casser" et le rendre plus robuste!

**Exemple:**
```python
age = int(input("Âge: "))
# Essayez: 25 ✓
# Essayez: 200 (marche, mais bizarre!)
# Essayez: "vingt" (ça plante!)
```

Plus tard, vous apprendrez à gérer ces erreurs proprement!

---

## Prêt pour la suite?

Vous savez maintenant:
- ✅ Utiliser `input()` pour demander des informations
- ✅ Convertir du texte en nombre avec `int()` et `float()`
- ✅ Créer des programmes interactifs
- ✅ Utiliser les f-strings pour un affichage élégant
- ✅ Les erreurs courantes et comment les éviter

**BRAVO!** Vos programmes peuvent maintenant communiquer avec l'utilisateur!

**Prochaine étape:** Un GRAND défi pratique où vous allez utiliser TOUT ce que vous avez appris!

Cliquez sur "Continuer" → Le défi vous attend! 💪
