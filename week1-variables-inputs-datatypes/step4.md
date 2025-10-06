# Étape 4 : Défi Pratique - Tout Assembler!

## IMPORTANT: Réactiver votre environnement virtuel

Dernière étape! Activons l'environnement une dernière fois.

### Commande 1 : Aller dans votre dossier

`cd mon_projet_python`{{execute}}

### Commande 2 : Activer l'environnement

`source venv/bin/activate`{{execute}}

**VÉRIFICATION:**

Vous voyez `(venv)` ?
```
(venv) root@host:~/mon_projet_python#
```

Parfait! C'est parti pour le GRAND DÉFI! 💪

---

## Le Grand Défi : Système d'Inscription Étudiant

**Bravo d'être arrivé jusqu'ici!** Vous avez appris:
- ✅ Les variables
- ✅ Les types de données
- ✅ Les entrées utilisateur

**Maintenant:** On va TOUT utiliser ensemble dans un vrai programme!

---

## Qu'est-ce qu'on va créer?

Un **système d'inscription étudiant** qui:

1. **Demande** les informations d'un étudiant
2. **Calcule** des données automatiquement
3. **Affiche** un profil complet et joli

**C'est comme créer un mini logiciel de gestion!**

---

## Ce que votre programme DOIT faire

### PARTIE 1: Collecter les informations

Votre programme doit demander:

1. **Nom complet** de l'étudiant (String)
   - Exemple: "Sarah Martinez"

2. **Âge** de l'étudiant (Integer)
   - Exemple: 19

3. **Moyenne générale** / Note sur 20 (Float)
   - Exemple: 15.75

---

### PARTIE 2: Calculer automatiquement

Votre programme doit calculer:

1. **Année d'obtention du diplôme**
   - Formule: Année actuelle (2025) + 4 ans d'études
   - Exemple: 2025 + 4 = 2029

2. **BONUS (optionnel):** Âge au diplôme
   - Formule: Âge actuel + 4
   - Exemple: 19 + 4 = 23

---

### PARTIE 3: Afficher joliment

Votre programme doit afficher:

```
=== SYSTÈME D'INSCRIPTION ÉTUDIANT ===

[Questions et réponses]

=== PROFIL ÉTUDIANT ===
Nom: Sarah Martinez
Âge: 19 ans
Moyenne: 15.75 / 20
Diplôme prévu en: 2029

Bonne chance dans vos études, Sarah Martinez!
```

---

## STRATÉGIE: Comment aborder ce défi

**Conseil de prof:**

Ne faites PAS tout d'un coup! Construisez votre programme **BRIQUE PAR BRIQUE**.

**Étape 1:** Les entrées (input)
**Étape 2:** Les calculs
**Étape 3:** L'affichage

**Testez après chaque brique!**

---

## MÉTHODE 1: Défi Guidé (Pour débutants)

Je vais vous guider pas à pas. Suivez ces étapes:

### ÉTAPE 1.1 - Créer le fichier

`nano systeme_etudiant.py`{{execute}}

Nano s'ouvre.

---

### ÉTAPE 1.2 - Taper le TITRE du programme

**ACTION REQUISE:** Dans nano, tapez:

```python
# Système d'Inscription Étudiant
print("="*40)
print("SYSTÈME D'INSCRIPTION ÉTUDIANT")
print("="*40)
print()
```

**Explication:**
- `"="*40` = répète le symbole `=` 40 fois (pour faire une ligne)
- `print()` tout seul = ligne vide

**Vérifiez:** 5 lignes tapées.

---

### ÉTAPE 1.3 - Demander le nom complet

**ACTION REQUISE:** Continuez à taper (ligne 6):

```python
# Demander les informations
nom_complet = input("Entrez votre nom complet: ")
```

**Explication:**
- `input(...)` = demande à l'utilisateur
- Pas besoin de convertir, le nom est du TEXTE
- Stocké dans `nom_complet`

---

### ÉTAPE 1.4 - Demander l'âge

**ACTION REQUISE:** Ligne suivante:

```python
age = int(input("Entrez votre âge: "))
```

**ATTENTION:** On utilise `int()` pour convertir en nombre!

**Pourquoi?** Pour pouvoir calculer l'âge au diplôme plus tard!

---

### ÉTAPE 1.5 - Demander la moyenne

**ACTION REQUISE:** Ligne suivante:

```python
moyenne = float(input("Entrez votre moyenne sur 20: "))
```

**ATTENTION:** On utilise `float()` car une moyenne peut avoir des décimales (15.75, 12.5, etc.)

---

### ÉTAPE 1.6 - Calculer l'année de diplôme

**ACTION REQUISE:** Après une ligne vide, tapez:

```python
# Calculer l'année de diplôme
annee_actuelle = 2025
annee_diplome = annee_actuelle + 4
```

**Explication:**
- On stocke 2025 dans une variable (facile à modifier plus tard)
- On calcule: 2025 + 4 = 2029
- Le résultat va dans `annee_diplome`

---

### ÉTAPE 1.7 - Afficher le profil

**ACTION REQUISE:** Après une ligne vide, tapez:

```python
# Afficher le profil étudiant
print()
print("="*40)
print("PROFIL ÉTUDIANT")
print("="*40)
print(f"Nom: {nom_complet}")
print(f"Âge: {age} ans")
print(f"Moyenne: {moyenne} / 20")
print(f"Diplôme prévu en: {annee_diplome}")
print("="*40)
print()
print(f"Bonne chance dans vos études, {nom_complet}!")
```

**Explication:**
- Les f-strings `f"..."` permettent d'insérer des variables
- `{nom_complet}` sera remplacé par le nom tapé
- C'est beau et professionnel!

---

### ÉTAPE 1.8 - Vérifier votre code complet

Votre fichier `systeme_etudiant.py` devrait ressembler à ça:

```python
# Système d'Inscription Étudiant
print("="*40)
print("SYSTÈME D'INSCRIPTION ÉTUDIANT")
print("="*40)
print()

# Demander les informations
nom_complet = input("Entrez votre nom complet: ")
age = int(input("Entrez votre âge: "))
moyenne = float(input("Entrez votre moyenne sur 20: "))

# Calculer l'année de diplôme
annee_actuelle = 2025
annee_diplome = annee_actuelle + 4

# Afficher le profil étudiant
print()
print("="*40)
print("PROFIL ÉTUDIANT")
print("="*40)
print(f"Nom: {nom_complet}")
print(f"Âge: {age} ans")
print(f"Moyenne: {moyenne} / 20")
print(f"Diplôme prévu en: {annee_diplome}")
print("="*40)
print()
print(f"Bonne chance dans vos études, {nom_complet}!")
```

**Vérifiez ligne par ligne!** Si quelque chose manque, ajoutez-le.

---

### ÉTAPE 1.9 - Sauvegarder et quitter

1. `Ctrl + O` puis `Entrée` → Sauvegarder
2. Vous voyez: `[ Wrote X lines ]`
3. `Ctrl + X` → Quitter

---

### ÉTAPE 1.10 - LE MOMENT DE VÉRITÉ!

**EXÉCUTEZ VOTRE PROGRAMME:**

`python3 systeme_etudiant.py`{{execute}}

**UTILISATION:**

Quand le programme demande, tapez:

```
Entrez votre nom complet: Sarah Martinez
Entrez votre âge: 19
Entrez votre moyenne sur 20: 15.75
```

**RÉSULTAT ATTENDU:**

```
========================================
SYSTÈME D'INSCRIPTION ÉTUDIANT
========================================

Entrez votre nom complet: Sarah Martinez
Entrez votre âge: 19
Entrez votre moyenne sur 20: 15.75

========================================
PROFIL ÉTUDIANT
========================================
Nom: Sarah Martinez
Âge: 19 ans
Moyenne: 15.75 / 20
Diplôme prévu en: 2029
========================================

Bonne chance dans vos études, Sarah Martinez!
```

**SI VOUS VOYEZ ÇA:** 🎉🎉🎉 **FÉLICITATIONS!!!** Vous avez créé un programme complet!

---

## MÉTHODE 2: Défi Autonome (Pour ceux qui veulent essayer seuls)

**Si vous voulez essayer VOUS-MÊME sans le guide:**

### Template de départ:

`nano systeme_etudiant.py`{{execute}}

Tapez ce template et complétez les `# TODO`:

```python
# Système d'Inscription Étudiant
print("="*40)
print("SYSTÈME D'INSCRIPTION ÉTUDIANT")
print("="*40)
print()

# TODO: Demander le nom complet (String)


# TODO: Demander l'âge (Integer - n'oubliez pas int()!)


# TODO: Demander la moyenne (Float - n'oubliez pas float()!)


# TODO: Calculer l'année de diplôme (2025 + 4)


# TODO: Afficher le profil avec print() ou f-strings


```

**Indices:**
- `input()` pour demander
- `int()` pour convertir en nombre entier
- `float()` pour convertir en décimal
- f-strings pour afficher: `print(f"Texte {variable}")`

---

## BONUS: Améliorations pour aller plus loin

Si vous avez terminé le défi de base, essayez ces améliorations!

### NIVEAU 1: Ajouter plus d'informations

Ajoutez ces champs:
- Numéro étudiant (Integer)
- Filière d'études (String)
- Email (String)
- Téléphone (String)

### NIVEAU 2: Plus de calculs

Calculez et affichez:
- Âge au moment du diplôme (âge + 4)
- Années restantes avant diplôme (4 - 0 = 4)
- Si la moyenne est >= 12 (mention: "Oui" ou "Non")

**Indice pour la mention:**
```python
if moyenne >= 12:
    print("Mention: Oui")
else:
    print("Mention: Non")
```

### NIVEAU 3: Rendre ça encore plus joli

Améliorations visuelles:
- Symboles spéciaux (★, ◆, →)
- Couleurs (avancé!)
- Espaces bien alignés
- Message personnalisé selon la moyenne

---

## Problèmes courants et solutions

### Problème 1: "invalid literal for int()"

**Cause:** Vous essayez de convertir du texte en nombre.

**Exemple d'erreur:**
```python
age = int(input("Âge: "))
# Utilisateur tape: "dix-neuf" au lieu de 19
```

**Solution:**
- Dites clairement: "Entrez votre âge EN CHIFFRES"
- Exemple: `int(input("Âge (en chiffres, ex: 19): "))`

---

### Problème 2: "unsupported operand type(s)"

**Cause:** Vous essayez de faire des calculs avec du texte.

**Exemple d'erreur:**
```python
age = input("Âge: ")  # Oubli de int()!
futur = age + 4       # ERREUR!
```

**Solution:**
- Vérifiez que vous avez `int()` ou `float()` autour de input()
- `age = int(input("Âge: "))`

---

### Problème 3: Les décimales s'affichent bizarrement

**Problème:**
```
Moyenne: 15.750000000001
```

**Solution:** Limitez à 2 décimales avec `.2f`

```python
print(f"Moyenne: {moyenne:.2f} / 20")
# Résultat: Moyenne: 15.75 / 20
```

---

### Problème 4: Nom de variable non défini

**Message d'erreur:**
```
NameError: name 'nom_complet' is not defined
```

**Cause:** Vous utilisez une variable avant de la créer!

**Solution:**
1. Vérifiez que vous avez bien tapé la ligne `nom_complet = input(...)`
2. Vérifiez l'orthographe (majuscules/minuscules!)
3. Assurez-vous que c'est AVANT le `print()`

---

## Auto-évaluation

Avant de passer à la conclusion, vérifiez que vous pouvez:

- [ ] Demander des informations avec `input()`
- [ ] Convertir du texte en nombre avec `int()` et `float()`
- [ ] Stocker des données dans des variables
- [ ] Faire des calculs simples (+, -, *, /)
- [ ] Afficher avec `print()` et f-strings
- [ ] Créer un programme complet qui marche!

**Si vous pouvez faire tout ça: VOUS ÊTES UN PROGRAMMEUR!** 🎓

---

## Tester votre programme

**Un bon programmeur teste TOUJOURS son code!**

Exécutez votre programme plusieurs fois avec différentes valeurs:

**Test 1: Valeurs normales**
```
Nom: Julie Dubois
Âge: 20
Moyenne: 14.5
```

**Test 2: Très jeune**
```
Nom: Marc Petit
Âge: 17
Moyenne: 16.0
```

**Test 3: Excellente moyenne**
```
Nom: Fatima El Mansouri
Âge: 22
Moyenne: 18.75
```

**Test 4: Faible moyenne**
```
Nom: Pierre Martin
Âge: 21
Moyenne: 8.5
```

**Chaque test devrait fonctionner sans erreur!**

---

## Conseil de professeur expérimenté

**Quand vous créez un programme, suivez toujours cette méthode:**

### 1. PLANIFIER (sur papier!)
- Qu'est-ce que mon programme doit faire?
- De quelles informations ai-je besoin?
- Quels calculs dois-je faire?
- Comment afficher le résultat?

### 2. CODER (pas à pas)
- Commencez par le titre
- Ajoutez une entrée, testez
- Ajoutez une autre entrée, testez
- Ajoutez les calculs, testez
- Ajoutez l'affichage, testez

### 3. TESTER (avec différentes valeurs)
- Valeurs normales
- Valeurs extrêmes
- Valeurs bizarres

### 4. AMÉLIORER (si temps)
- Rendre plus joli
- Ajouter des fonctionnalités
- Optimiser le code

**Cette méthode marche pour TOUS les programmes, même les plus complexes!**

---

## Variante du défi

**Si vous voulez un défi différent**, essayez celui-ci:

### DÉFI ALTERNATIF: Calculateur de Budget Étudiant

Créez un programme qui:

1. **Demande:**
   - Nom de l'étudiant
   - Argent de poche mensuel (Float)
   - Loyer mensuel (Float)
   - Budget nourriture mensuel (Float)

2. **Calcule:**
   - Total des dépenses (loyer + nourriture)
   - Argent restant (argent de poche - dépenses)
   - Budget annuel (montant mensuel × 12)

3. **Affiche:**
   - Résumé du budget
   - Si c'est positif (il reste de l'argent) ou négatif

---

## Aide si vous êtes bloqué

### Indice 1: Structure générale

```python
# 1. Titre
# 2. Inputs (3-4 variables)
# 3. Calculs (1-2 variables)
# 4. Affichage avec f-strings
```

### Indice 2: Pour les inputs

```python
variable_texte = input("Question: ")
variable_nombre = int(input("Question: "))
variable_decimal = float(input("Question: "))
```

### Indice 3: Pour les f-strings

```python
print(f"Texte fixe {variable} autre texte {autre_variable}")
```

---

## Solution complète (N'OUBLIEZ PAS D'ESSAYER D'ABORD!)

<details>
<summary>⚠️ Cliquez ICI seulement si vous êtes vraiment bloqué</summary>

```python
# Système d'Inscription Étudiant
print("="*40)
print("SYSTÈME D'INSCRIPTION ÉTUDIANT")
print("="*40)
print()

# Demander les informations
nom_complet = input("Entrez votre nom complet: ")
age = int(input("Entrez votre âge: "))
moyenne = float(input("Entrez votre moyenne sur 20: "))

# Calculer l'année de diplôme
annee_actuelle = 2025
annee_diplome = annee_actuelle + 4

# Afficher le profil étudiant
print()
print("="*40)
print("PROFIL ÉTUDIANT")
print("="*40)
print(f"Nom: {nom_complet}")
print(f"Âge: {age} ans")
print(f"Moyenne: {moyenne:.2f} / 20")
print(f"Diplôme prévu en: {annee_diplome}")
print("="*40)
print()
print(f"Bonne chance dans vos études, {nom_complet}!")
```

**Note:** `.2f` dans `{moyenne:.2f}` limite l'affichage à 2 décimales.

</details>

---

## Amélioration BONUS: Version avec calcul d'âge au diplôme

<details>
<summary>Solution avec bonus</summary>

```python
# Système d'Inscription Étudiant
print("="*40)
print("SYSTÈME D'INSCRIPTION ÉTUDIANT")
print("="*40)
print()

# Demander les informations
nom_complet = input("Entrez votre nom complet: ")
age = int(input("Entrez votre âge: "))
moyenne = float(input("Entrez votre moyenne sur 20: "))

# Calculer l'année de diplôme ET l'âge au diplôme
annee_actuelle = 2025
annee_diplome = annee_actuelle + 4
age_diplome = age + 4

# Afficher le profil étudiant
print()
print("="*40)
print("PROFIL ÉTUDIANT")
print("="*40)
print(f"Nom: {nom_complet}")
print(f"Âge actuel: {age} ans")
print(f"Moyenne: {moyenne:.2f} / 20")
print(f"Diplôme prévu en: {annee_diplome}")
print(f"Âge au diplôme: {age_diplome} ans")
print("="*40)
print()
print(f"Bonne chance dans vos études, {nom_complet}!")
print(f"Dans 4 ans, vous aurez {age_diplome} ans et un diplôme!")
```

</details>

---

## Exercices supplémentaires (Si vous avez le temps)

### Exercice 1: Convertisseur de devises

Créez `convertisseur.py` qui:
- Demande un montant en euros
- Le convertit en dollars (1€ = 1.10$)
- Affiche le résultat

**Exemple:**
```
Montant en euros: 100
100.00€ = 110.00$
```

---

### Exercice 2: Calculateur IMC (Indice de Masse Corporelle)

Créez `imc.py` qui:
- Demande le poids en kg
- Demande la taille en mètres
- Calcule l'IMC: `poids / (taille * taille)`
- Affiche le résultat

**Exemple:**
```
Poids (kg): 70
Taille (m): 1.75
Votre IMC: 22.86
```

---

### Exercice 3: Calculateur de moyenne

Créez `moyenne.py` qui:
- Demande 3 notes
- Calcule la moyenne
- Affiche si c'est réussi (>= 10)

**Exemple:**
```
Note 1: 12
Note 2: 15
Note 3: 14
Moyenne: 13.67
Résultat: RÉUSSI!
```

---

## Points clés de ce défi

**Ce que vous avez appris:**

1. **Organiser un programme complet**
   - Titre → Inputs → Calculs → Affichage

2. **Combiner plusieurs concepts**
   - Variables + types + input() + calculs + affichage

3. **Rendre un programme joli**
   - Lignes de séparation
   - Messages personnalisés
   - Formatage propre

4. **Débugger** (corriger les erreurs)
   - Lire les messages d'erreur
   - Identifier le problème
   - Corriger et retester

**BRAVO!** Vous êtes maintenant capable de créer des programmes Python complets et fonctionnels!

---

## Prêt pour la conclusion?

Vous venez de terminer le PLUS GROS défi de la Semaine 1!

**Dans la conclusion, vous allez voir:**
- Résumé complet de tout ce que vous avez appris
- Solutions détaillées
- Exercices supplémentaires pour pratiquer
- Aperçu de la Semaine 2

**Cliquez sur "Continuer" pour voir la conclusion!** 🎓
