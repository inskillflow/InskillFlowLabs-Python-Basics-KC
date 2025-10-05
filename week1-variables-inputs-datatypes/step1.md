# Étape 1 : Les Variables et l'Assignation

## IMPORTANT: Activer votre environnement virtuel

Avant de commencer, activons l'environnement virtuel créé à l'Étape 0.

### Commande 1 : Aller dans votre dossier

`cd mon_projet_python`{{execute}}

### Commande 2 : Activer l'environnement

`source venv/bin/activate`{{execute}}

**VÉRIFICATION OBLIGATOIRE:**

Regardez le début de votre ligne de commande. Vous DEVEZ voir `(venv)` :

```
(venv) root@host:~/mon_projet_python#
```

Si vous ne voyez PAS `(venv)`, **STOP!** Refaites la Commande 2 ci-dessus.

---

## Qu'est-ce qu'une variable?

Imaginez une **boîte** avec une **étiquette** dessus.

**Exemple dans la vraie vie:**
- Vous avez une boîte avec l'étiquette "JOUETS" → Dedans: vos jouets
- Vous avez une boîte avec l'étiquette "LIVRES" → Dedans: vos livres
- Vous avez une boîte avec l'étiquette "PHOTOS" → Dedans: vos photos

**En programmation, c'est pareil!**
- Une variable avec le nom "age" → Dedans: votre âge (exemple: 25)
- Une variable avec le nom "prenom" → Dedans: votre prénom (exemple: "Julie")

La variable = la boîte avec une étiquette où on range une information

---

## Créer une variable : La syntaxe

Pour créer une variable en Python, on écrit:

```
nom_de_la_boite = ce_qu_on_met_dedans
```

**Exemples concrets:**

```python
age = 25
prenom = "Marie"
ville = "Paris"
```

**Traduction en français:**
- `age = 25` signifie: "Crée une boîte appelée 'age' et mets le nombre 25 dedans"
- `prenom = "Marie"` signifie: "Crée une boîte appelée 'prenom' et mets le texte 'Marie' dedans"

---

## Les règles pour nommer une variable

Comme quand vous choisissez un nom pour votre chien ou chat, il y a des règles:

**RÈGLE 1:** Le nom peut contenir des lettres, des chiffres et le tiret du bas `_`
- ✅ CORRECT: `mon_age`, `prenom2`, `ville_naissance`
- ❌ INCORRECT: `mon-age` (tiret normal interdit), `mon age` (espace interdit)

**RÈGLE 2:** Le nom DOIT commencer par une lettre (pas un chiffre)
- ✅ CORRECT: `age1`, `prenom2`
- ❌ INCORRECT: `1age`, `2prenom`

**RÈGLE 3:** Python fait la différence entre MAJUSCULES et minuscules
- `Age` et `age` sont DEUX variables différentes!
- `PRENOM`, `Prenom` et `prenom` sont TROIS variables différentes!

**RÈGLE 4:** Choisissez des noms qui ont du SENS
- ✅ CORRECT: `age_utilisateur` (on comprend tout de suite!)
- ❌ MAUVAIS: `x` ou `truc` (on ne comprend rien!)

---

## EXERCICE 1 : Votre tout premier programme Python

Je vais vous guider PAS À PAS, comme si vous étiez mon élève et que c'était votre premier jour.

### ÉTAPE 1.1 - Comprendre ce qu'on va faire

Nous allons:
1. Créer un fichier Python appelé `script.py`
2. Écrire du code dedans (une variable + un affichage)
3. Sauvegarder le fichier
4. Exécuter le programme pour voir le résultat

C'est tout! Simple, non? Allons-y!

---

### ÉTAPE 1.2 - Ouvrir l'éditeur nano

**QU'EST-CE QUE NANO?**

`nano` est un programme pour écrire du texte dans le terminal (comme Notepad sur Windows, mais dans le terminal).

**EXÉCUTEZ CETTE COMMANDE:**

`nano script.py`{{execute}}

**QU'EST-CE QUI SE PASSE?**

Votre écran change complètement! Vous voyez maintenant:
- Un écran bleu ou noir
- En haut: "GNU nano" et "File: script.py"
- En bas: Une liste de commandes avec des `^X`, `^O`, etc.
- Au milieu: Une zone vide (c'est là qu'on va taper!)

**IMPORTANT:** Le symbole `^` signifie la touche `Ctrl` de votre clavier.
- `^X` = `Ctrl + X`
- `^O` = `Ctrl + O`

**Vous êtes maintenant DANS nano!** Prêt à taper votre code!

---

### ÉTAPE 1.3 - Taper votre premier code Python

**ACTION REQUISE:** Vous allez maintenant TAPER du code.

**TAPEZ EXACTEMENT CE TEXTE** (ligne par ligne):

```python
# Ceci est un commentaire
# Python ne va pas exécuter cette ligne
# Les commentaires servent à expliquer ce que fait votre code

mon_code_pin = 1234

print(mon_code_pin)
```

**CONSEILS POUR TAPER:**
1. Tapez la première ligne: `# Ceci est un commentaire`
2. Appuyez sur `Entrée` pour aller à la ligne suivante
3. Tapez la deuxième ligne: `# Python ne va pas exécuter cette ligne`
4. Appuyez sur `Entrée`
5. Continuez comme ça pour chaque ligne

**SI VOUS FAITES UNE FAUTE:**
- Utilisez les flèches `←` `→` `↑` `↓` pour bouger le curseur
- Utilisez `Backspace` (touche d'effacement) pour effacer
- Retapez correctement

**VÉRIFICATION:** Vous devez avoir tapé exactement 7 lignes dans nano.

---

### ÉTAPE 1.4 - Comprendre ce que fait ce code

Avant de sauvegarder, comprenons ce qu'on vient de taper:

**Ligne 1, 2, 3:** Commencent par `#`
- Ce sont des **commentaires**
- Python les IGNORE complètement
- Ils servent juste à expliquer le code aux humains (vous!)

**Ligne 4:** Vide
- Juste pour aérer le code, le rendre plus lisible

**Ligne 5:** `mon_code_pin = 1234`
- Crée une **variable** (une boîte) appelée `mon_code_pin`
- Met le nombre **1234** dans cette boîte
- C'est comme dire: "Souviens-toi que mon code PIN est 1234"

**Ligne 6:** Vide
- Encore pour aérer

**Ligne 7:** `print(mon_code_pin)`
- **Affiche** ce qu'il y a dans la boîte `mon_code_pin`
- `print` = "affiche à l'écran"
- Résultat attendu: `1234` va s'afficher

**Compris?** Parfait! Maintenant sauvegardons ce fichier!

---

### ÉTAPE 1.5 - Sauvegarder le fichier dans nano

**ACTION REQUISE:** Vous allez sauvegarder ce que vous avez tapé.

**ÉTAPE PAR ÉTAPE:**

**1. Appuyez sur votre clavier:** `Ctrl + O` (maintenez Ctrl, appuyez sur O)
   
   **Ce que vous voyez:** En bas de l'écran, vous voyez:
   ```
   File Name to Write: script.py
   ```
   
**2. Appuyez sur:** `Entrée` (touche Enter de votre clavier)
   
   **Ce que vous voyez:** Un message apparaît:
   ```
   [ Wrote 7 lines ]
   ```
   
   **Bravo!** Votre fichier est sauvegardé!

**AIDE-MÉMOIRE:**
- `Ctrl + O` = **O**pen/Write Out = Sauvegarder
- Vous verrez toujours ce raccourci en bas: `^O Write Out`

---

### ÉTAPE 1.6 - Quitter nano et retourner au terminal

**ACTION REQUISE:** Maintenant, sortons de nano.

**Appuyez sur votre clavier:** `Ctrl + X` (maintenez Ctrl, appuyez sur X)

**Ce qui se passe:** L'écran bleu/noir disparaît, vous revenez au terminal normal!

Vous voyez à nouveau:
```
(venv) root@host:~/mon_projet_python#
```

**Bravo!** Vous êtes sorti de nano!

**AIDE-MÉMOIRE:**
- `Ctrl + X` = e**X**it = Quitter
- Vous verrez toujours ce raccourci en bas: `^X Exit`

---

### ÉTAPE 1.7 - Exécuter votre programme Python

Maintenant le moment magique: voir votre programme fonctionner!

**EXÉCUTEZ CETTE COMMANDE:**

`python3 script.py`{{execute}}

**RÉSULTAT ATTENDU:**

Vous devez voir s'afficher:
```
1234
```

**SI VOUS VOYEZ 1234:**
🎉 **FÉLICITATIONS!** Vous venez de créer et exécuter votre tout premier programme Python!

**SI VOUS VOYEZ UNE ERREUR:**
- Il y a peut-être une faute de frappe dans votre code
- Relisez les ÉTAPES 1.2 à 1.6 et recommencez
- Vérifiez chaque ligne attentivement

---

## Explication : Que s'est-il passé?

Récapitulons ce que vous venez de faire:

1. **Ouvert nano** → Un éditeur pour taper du code
2. **Tapé du code Python** → Création d'une variable et affichage
3. **Sauvegardé** (Ctrl+O) → Le fichier `script.py` est créé sur le système
4. **Quitté nano** (Ctrl+X) → Retour au terminal
5. **Exécuté** (`python3 script.py`) → Python lit votre fichier et fait ce que vous avez demandé

**Résultat:** Le nombre 1234 s'affiche à l'écran!

---

## EXERCICE 2 : Modifier votre programme

Maintenant, vous allez **modifier** votre programme pour ajouter une deuxième variable.

### ÉTAPE 2.1 - Rouvrir le fichier dans nano

**EXÉCUTEZ CETTE COMMANDE:**

`nano script.py`{{execute}}

**Ce qui se passe:** Nano s'ouvre à nouveau, et vous voyez votre code d'avant! Il n'a pas disparu, il est sauvegardé!

---

### ÉTAPE 2.2 - Ajouter une nouvelle ligne de code

**ACTION REQUISE:** Vous allez ajouter UNE ligne.

**ÉTAPE PAR ÉTAPE:**

**1. Positionnez votre curseur:**
   - Utilisez la flèche `↓` (bas) pour descendre
   - Arrêtez-vous à la ligne `mon_code_pin = 1234`
   - Utilisez la flèche `→` (droite) pour aller à la FIN de cette ligne

**2. Créez une nouvelle ligne:**
   - Appuyez sur `Entrée`
   - Vous voyez le curseur passer à la ligne suivante

**3. Tapez cette nouvelle ligne:**
   ```python
   mon_prenom = "VotrePrenom"
   ```
   
   **MAIS ATTENTION:** Remplacez `VotrePrenom` par VOTRE vrai prénom!
   
   **Exemple si vous vous appelez Julie:**
   ```python
   mon_prenom = "Julie"
   ```
   
   **Exemple si vous vous appelez Ahmed:**
   ```python
   mon_prenom = "Ahmed"
   ```

**IMPORTANT:** **GARDEZ les guillemets `"` `"`** autour de votre prénom!
- Les guillemets disent à Python: "Ceci est du texte, pas un nombre"

---

### ÉTAPE 2.3 - Ajouter l'affichage du prénom

**ACTION REQUISE:** Ajoutons une ligne pour afficher votre prénom.

**ÉTAPE PAR ÉTAPE:**

**1. Allez en bas du fichier:**
   - Appuyez plusieurs fois sur la flèche `↓` (bas)
   - Arrêtez-vous APRÈS la ligne `print(mon_code_pin)`

**2. Créez une nouvelle ligne:**
   - Appuyez sur `Entrée`

**3. Tapez cette ligne:**
   ```python
   print(mon_prenom)
   ```
   
   **ATTENTION:** 
   - Pas de guillemets autour de `mon_prenom` ici!
   - C'est le **nom de la variable**, pas du texte

---

### ÉTAPE 2.4 - Vérifier votre code complet

Votre fichier devrait maintenant ressembler à ça:

```python
# Ceci est un commentaire
# Python ne va pas exécuter cette ligne
# Les commentaires servent à expliquer ce que fait votre code

mon_code_pin = 1234
mon_prenom = "Julie"

print(mon_code_pin)
print(mon_prenom)
```

(Avec VOTRE prénom à la place de Julie!)

**Vérifiez ligne par ligne!** Si ce n'est pas exactement ça, corrigez avec les flèches et Backspace.

---

### ÉTAPE 2.5 - Sauvegarder vos modifications

**ACTION REQUISE:** Sauvegardons le fichier modifié.

**RAPPELEZ-VOUS:**
1. `Ctrl + O` puis `Entrée` → Sauvegarder
2. Message: `[ Wrote X lines ]` → C'est bon!

**Faites-le maintenant!**

---

### ÉTAPE 2.6 - Quitter nano

**ACTION REQUISE:** Sortons de nano.

`Ctrl + X` → Quitter

Vous revenez au terminal.

---

### ÉTAPE 2.7 - Exécuter votre programme modifié

**EXÉCUTEZ:**

`python3 script.py`{{execute}}

**RÉSULTAT ATTENDU:**

Vous devez voir:
```
1234
Julie
```

(Avec votre prénom à vous!)

**SI VOUS VOYEZ ÇA:**
🎉 **SUPER!** Vous savez maintenant:
- Créer des variables
- Afficher leur contenu
- Modifier un programme Python

---

## Points importants à retenir

**1. Une variable, c'est comme une boîte avec une étiquette**
   - L'étiquette = le nom (exemple: `age`)
   - Ce qu'il y a dedans = la valeur (exemple: `25`)

**2. Pour créer une variable:**
   ```python
   nom_variable = valeur
   ```

**3. Différence texte / nombre:**
   - **Nombre** (pas de guillemets): `age = 25`
   - **Texte** (AVEC guillemets): `prenom = "Julie"`

**4. Les commentaires commencent par `#`**
   - Python les ignore
   - Ils servent à expliquer le code

**5. `print()` affiche quelque chose à l'écran**
   ```python
   print(mon_age)  # Affiche le contenu de la variable
   ```

**6. Nano, les 2 commandes essentielles:**
   - `Ctrl + O` puis `Entrée` = Sauvegarder
   - `Ctrl + X` = Quitter

---

## Conseil de professeur expérimenté

**Lisez toujours vos commentaires à voix haute!**

Dans 1 semaine, 1 mois, 1 an, quand vous relirez votre code, vous aurez oublié ce qu'il fait. Les commentaires sont comme des petites notes que vous laissez à votre futur vous.

**Bon réflexe:**
```python
# Stocker l'âge de l'utilisateur
age = 25

# Afficher l'âge
print(age)
```

**Mauvais réflexe:**
```python
age = 25
print(age)
```

Le premier est plus long à taper, mais 100x plus facile à comprendre plus tard!

---

## Prêt pour la suite?

Vous savez maintenant:
- ✅ Créer des variables
- ✅ Utiliser nano (ouvrir, taper, sauvegarder, quitter)
- ✅ Exécuter un programme Python
- ✅ Modifier un programme existant

**Bravo!** Cliquez sur "Continuer" pour apprendre les **types de données**!

---

## Aide-mémoire rapide

```bash
# Ouvrir/créer un fichier
nano nomfichier.py

# Dans nano:
# - Taper normalement
# - Entrée = nouvelle ligne
# - Flèches = se déplacer
# - Backspace = effacer
# - Ctrl+O puis Entrée = Sauvegarder
# - Ctrl+X = Quitter

# Exécuter un programme Python
python3 nomfichier.py
```

Gardez cet aide-mémoire sous les yeux!
