# Étape 1 : Les Variables et l'Assignation

## Qu'est-ce qu'une variable?

Une variable est comme une **boîte avec une étiquette** où vous pouvez ranger des informations. Imaginez que vous avez plusieurs boîtes dans votre chambre, chacune avec un nom dessus : "jouets", "livres", "vêtements". En programmation, c'est pareil!

---

## Créer votre première variable

### Syntaxe de base:
```python
nom_de_la_variable = valeur
```

### Exemple concret:
```python
mon_age = 25
mon_nom = "Julie"
```

---

## Les règles importantes pour nommer une variable:

1. Peut contenir des lettres, des chiffres et des tirets bas (_)
2. Doit commencer par une lettre (pas un chiffre)
3. Python fait la différence entre majuscules et minuscules (`Age` et `age` sont différents)
4. Utilisez des noms qui ont du sens! (`age_utilisateur` est mieux que `x`)

---

## EXERCICE 1 : Votre premier programme Python

Je vais vous guider pas à pas. Suivez exactement ces instructions:

### ÉTAPE 1.1 - Ouvrir l'éditeur

Cliquez sur ce bouton pour ouvrir l'éditeur de code:

`script.py`{{open}}

Un éditeur de texte va s'ouvrir à droite de votre écran.

---

### ÉTAPE 1.2 - Écrire votre premier code

Maintenant, **copiez exactement ce code** dans l'éditeur qui vient de s'ouvrir:

```python
# Ceci est un commentaire
# Python ne va pas exécuter cette ligne
# Les commentaires servent à expliquer ce que fait votre code

mon_code_pin = 1234

print(mon_code_pin)
```

**Que fait ce code?**
- La ligne qui commence par `#` est un commentaire (Python l'ignore)
- `mon_code_pin = 1234` crée une variable et met le nombre 1234 dedans
- `print(mon_code_pin)` affiche le contenu de la variable à l'écran

---

### ÉTAPE 1.3 - Exécuter votre code

Maintenant, cliquez sur ce bouton pour exécuter votre programme:

`python3 script.py`{{execute}}

**RÉSULTAT ATTENDU:**
Vous devriez voir le nombre `1234` s'afficher dans le terminal en bas!

Si vous voyez `1234`, BRAVO! Vous venez de créer votre première variable!

---

## EXERCICE 2 : À votre tour maintenant!

Je vais vous guider pour modifier votre code. Voici ce que vous allez faire:

### ÉTAPE 2.1 - Ajouter une deuxième variable

Dans votre éditeur `script.py`, **ajoutez ces 2 lignes** APRÈS la ligne `mon_code_pin = 1234`:

```python
mon_prenom = "VotrePrenom"
```

**IMPORTANT:** Remplacez `VotrePrenom` par votre vrai prénom, mais GARDEZ les guillemets!

Exemple:
```python
mon_prenom = "Julie"
```

---

### ÉTAPE 2.2 - Afficher votre prénom

Maintenant, **ajoutez cette ligne** tout à la fin de votre fichier:

```python
print(mon_prenom)
```

---

### ÉTAPE 2.3 - Votre code complet devrait ressembler à ça:

```python
# Ceci est un commentaire
# Python ne va pas exécuter cette ligne
# Les commentaires servent à expliquer ce que fait votre code

mon_code_pin = 1234
mon_prenom = "Julie"

print(mon_code_pin)
print(mon_prenom)
```

---

### ÉTAPE 2.4 - Exécuter à nouveau

Cliquez encore sur ce bouton:

`python3 script.py`{{execute}}

**RÉSULTAT ATTENDU:**
Vous devriez voir:
```
1234
Julie
```

---

## Comprendre la différence importante:

### Nombres (SANS guillemets):
```python
age = 25
```

### Texte (AVEC guillemets):
```python
prenom = "Julie"
```

**RÈGLE D'OR:** Si c'est du texte, il FAUT des guillemets `" "` ou `' '`

---

## Points clés à retenir:

1. Une variable stocke une information
2. `#` crée un commentaire
3. `=` met une valeur dans une variable
4. `print()` affiche quelque chose à l'écran
5. Le texte a besoin de guillemets, pas les nombres

---

**Conseil de pro:** Utilisez toujours des commentaires pour expliquer votre code. Dans 1 mois, vous aurez oublié ce que vous avez fait!

---

Quand vous êtes prêt, cliquez sur "Continuer" pour apprendre les types de données!
