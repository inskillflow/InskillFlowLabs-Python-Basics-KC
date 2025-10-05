# Étape 4 : Défi Pratique

## IMPORTANT: Réactiver votre environnement virtuel

Avant le défi final, assurons-nous que l'environnement virtuel est actif!

### Commande 1 : Aller dans votre dossier de projet

`cd mon_projet_python`{{execute}}

---

### Commande 2 : Activer l'environnement virtuel

`source venv/bin/activate`{{execute}}

**VÉRIFICATION:**
Vous devez voir `(venv)` au début de votre ligne!

---

## C'est l'heure de tout assembler!

Vous avez appris les variables, les types de données et les entrées utilisateur. Maintenant, construisons quelque chose de réel!

---

## DÉFI : Système d'Information Étudiant

Créez un programme qui collecte et affiche les informations d'un étudiant.

### Ce que votre programme doit faire:

**1. Demander:**
- Le nom complet de l'étudiant (string)
- L'âge de l'étudiant (integer)
- La moyenne générale / GPA (float, de 0.0 à 20.0)

**2. Calculer:**
- L'année d'obtention du diplôme (année actuelle 2025 + 4 ans)

**3. Afficher:**
- Un résumé bien formaté de toutes les informations

---

## Template de départ

### ÉTAPE 1 - Créer votre fichier de défi

`systeme_etudiant.py`{{open}}

---

### ÉTAPE 2 - Copier ce template

Copiez ce code de départ dans `systeme_etudiant.py`:

```python
# Système d'Information Étudiant
print("=== SYSTÈME D'INSCRIPTION ÉTUDIANT ===\n")

# TODO: Demander le nom complet
# Exemple: nom_complet = input("...")


# TODO: Demander l'âge (n'oubliez pas de convertir en integer!)
# Exemple: age = int(input("..."))


# TODO: Demander la moyenne (convertir en float!)
# Exemple: moyenne = float(input("..."))


# TODO: Calculer l'année de diplôme (2025 + 4)
# Exemple: annee_diplome = ...


# Afficher les informations
print("\n=== PROFIL ÉTUDIANT ===")
# TODO: Afficher le nom

# TODO: Afficher l'âge

# TODO: Afficher la moyenne

# TODO: Afficher l'année de diplôme

# TODO: Message de fin personnalisé
```

---

### ÉTAPE 3 - Complétez le code

Remplacez chaque `# TODO:` par le code approprié.

**INDICES:**
- Pour demander une information: `input("Votre question: ")`
- Pour convertir en nombre: `int(...)` ou `float(...)`
- Pour afficher: `print("Texte:", variable)`
- Pour calculer: `resultat = 2025 + 4`

---

## Exemple de sortie attendue

Votre programme devrait ressembler à ça:

```
=== SYSTÈME D'INSCRIPTION ÉTUDIANT ===

Entrez votre nom complet: Sarah Martinez
Entrez votre âge: 19
Entrez votre moyenne (0.0-20.0): 15.75

=== PROFIL ÉTUDIANT ===
Nom: Sarah Martinez
Âge: 19 ans
Moyenne: 15.75 / 20
Diplôme prévu en: 2029

Bonne chance dans vos études, Sarah Martinez!
```

---

## Testez votre programme

Une fois que vous avez complété le code:

`python3 systeme_etudiant.py`{{execute}}

Testez avec différentes valeurs pour vous assurer que ça marche!

---

## Défis bonus

Si vous terminez rapidement, essayez ces améliorations:

### Niveau 1: Ajouter plus de champs
- Numéro étudiant
- Filière d'études
- Adresse email

### Niveau 2: Rendre ça joli
- Ajouter des lignes de séparation (========)
- Utiliser des f-strings
- Ajouter des emojis (optionnel)

### Niveau 3: Calculs supplémentaires
- Calculer les années restantes jusqu'au diplôme
- Vérifier si la moyenne est supérieure à 12 (mention)
- Calculer l'âge au diplôme

---

## Exemple de solution (N'OUBLIEZ PAS D'ESSAYER D'ABORD!)

<details>
<summary>Cliquez ici pour voir UNE solution possible</summary>

```python
# Système d'Information Étudiant
print("=== SYSTÈME D'INSCRIPTION ÉTUDIANT ===\n")

# Demander les informations
nom_complet = input("Entrez votre nom complet: ")
age = int(input("Entrez votre âge: "))
moyenne = float(input("Entrez votre moyenne (0.0-20.0): "))

# Calculer l'année de diplôme
annee_actuelle = 2025
annee_diplome = annee_actuelle + 4

# Afficher les informations
print("\n=== PROFIL ÉTUDIANT ===")
print(f"Nom: {nom_complet}")
print(f"Âge: {age} ans")
print(f"Moyenne: {moyenne} / 20")
print(f"Diplôme prévu en: {annee_diplome}")
print(f"\nBonne chance dans vos études, {nom_complet}!")
```

</details>

---

## Problèmes courants et solutions

**Problème:** "invalid literal for int()"  
**Solution:** Vous essayez de convertir du texte en nombre. Assurez-vous d'utiliser `int(input(...))` correctement.

**Problème:** Les nombres ont trop de décimales  
**Solution:** Utilisez `round(nombre, 2)` pour arrondir à 2 décimales.

**Problème:** Vous voulez formater la moyenne à 2 décimales?  
**Solution:** Utilisez `print(f"Moyenne: {moyenne:.2f}")`

---

## Besoin d'aide?

Voici la structure de base:

```python
# 1. Obtenir les entrées (utilisez input() et convertissez les types)
# 2. Faire les calculs (annee_diplome = 2025 + 4)
# 3. Afficher le résultat formaté (utilisez print() ou f-strings)
```

Prenez votre temps et expérimentez! Faire des erreurs fait partie de l'apprentissage.

---

## Auto-évaluation

Avant de passer à l'étape suivante, vérifiez que vous pouvez:

- [ ] Demander des informations à l'utilisateur avec `input()`
- [ ] Convertir du texte en nombres avec `int()` et `float()`
- [ ] Stocker des données dans des variables
- [ ] Faire des calculs simples
- [ ] Afficher des résultats formatés avec `print()`
- [ ] Comprendre les différents types de données

---

Quand vous êtes prêt (ou si vous êtes bloqué), cliquez sur "Continuer" pour voir la solution complète et le résumé!
