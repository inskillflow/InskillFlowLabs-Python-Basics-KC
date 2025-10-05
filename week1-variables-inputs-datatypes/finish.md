# Félicitations!

## IMPORTANT: Réactiver une dernière fois

### Commande : Activer l'environnement virtuel

`cd mon_projet_python && source venv/bin/activate`{{execute}}

**Vérifiez que vous voyez `(venv)`!**

---

## Vous avez terminé Python Semaine 1!

Vous venez de faire votre premier grand pas dans le monde de la programmation Python!

---

## Ce que vous avez appris

### Variables & Assignation
- Comment créer et nommer des variables
- Bonnes pratiques pour les noms de variables
- Utiliser les commentaires pour documenter le code

### Types de Données
- **String** (texte)
- **Integer** (nombres entiers)
- **Float** (nombres décimaux)
- **Boolean** (Vrai/Faux)
- Comment vérifier les types avec `type()`

### Entrées Utilisateur
- Obtenir des entrées avec `input()`
- Convertir des strings en nombres avec `int()` et `float()`
- Créer des programmes interactifs
- Utiliser les f-strings pour formater du texte

### Environnement Virtuel
- Créer un environnement virtuel Python
- Activer et désactiver l'environnement
- Comprendre pourquoi c'est important

---

## Solution complète du défi

Voici UNE façon de résoudre le défi de l'Étape 4:

```python
# Système d'Information Étudiant
print("=== SYSTÈME D'INSCRIPTION ÉTUDIANT ===\n")

# Obtenir les informations de l'étudiant
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
print(f"Moyenne: {moyenne:.2f} / 20")
print(f"Diplôme prévu en: {annee_diplome}")
print(f"\nBonne chance dans vos études, {nom_complet}!")
```

---

## Concepts clés à retenir

1. **Les variables sont des conteneurs** - Elles stockent des données pour une utilisation ultérieure
2. **Les types de données comptent** - Les strings et les nombres se comportent différemment
3. **input() retourne toujours des strings** - Convertissez toujours quand vous avez besoin de nombres
4. **Les commentaires sont essentiels** - Votre futur vous vous remerciera!
5. **L'environnement virtuel isole votre projet** - Bonne pratique professionnelle

---

## Exercices supplémentaires

Avant de passer à la Semaine 2, essayez ces exercices:

### Exercice 1: Convertisseur de Température

Créez un programme qui:
- Demande une température en Celsius
- La convertit en Fahrenheit: `F = (C * 9/5) + 32`
- Affiche les deux températures

**Exemple de sortie:**
```
Température en Celsius: 25
25°C = 77.0°F
```

---

### Exercice 2: Calculateur de Courses

Créez un programme qui:
- Demande le nom d'un article
- Demande le prix unitaire
- Demande la quantité
- Calcule le coût total
- Affiche un reçu

**Exemple de sortie:**
```
=== REÇU ===
Article: Pommes
Prix unitaire: 2.50€
Quantité: 5
Total: 12.50€
```

---

### Exercice 3: Calculateur d'Âge

Créez un programme qui:
- Demande l'année de naissance
- Calcule l'âge actuel (2025 - année de naissance)
- Calcule l'âge dans 10 ans
- Calcule l'âge en "années de chien" (âge × 7)

**Exemple de sortie:**
```
Année de naissance: 2000
Âge actuel: 25 ans
Âge dans 10 ans: 35 ans
Âge en années de chien: 175 ans
```

---

## Ressources supplémentaires

Pour aller plus loin:

- [Documentation Python Officielle](https://docs.python.org/fr/3/)
- [W3Schools Python (FR)](https://www.w3schools.com/python/)
- [Real Python Tutoriels](https://realpython.com/)
- [Python Variables](https://www.w3schools.com/python/python_variables.asp)
- [Python Types de Données](https://www.w3schools.com/python/python_datatypes.asp)

---

## Prochaine étape?

### Python Semaine 2: Instructions Conditionnelles

La semaine prochaine, vous apprendrez:
- Les instructions If
- Elif et else
- Les opérateurs de comparaison (==, !=, <, >, <=, >=)
- Les opérateurs logiques (and, or, not)
- Les conditions imbriquées

Avec les conditions, vos programmes pourront prendre des décisions!

---

## Gardez vos fichiers

Sauvegardez tous vos fichiers Python d'aujourd'hui:
- `script.py`
- `types_donnees.py`
- `interactif.py`
- `systeme_etudiant.py`

Vous pourriez vouloir les consulter plus tard!

---

## Conseils finaux

- **Pratiquez quotidiennement** - Même 15 minutes aident
- **Expérimentez** - Essayez de casser votre code pour apprendre
- **Posez des questions** - Aucune question n'est trop simple
- **Amusez-vous** - La programmation est créative!

---

## Partagez votre succès!

Vous avez terminé votre premier lab Python! Prenez un moment pour célébrer cette réussite. Vous êtes officiellement un programmeur Python!

**Prêt pour plus?** Continuez vers **Python Semaine 2: Instructions Conditionnelles**

---

### À la semaine prochaine! Bon codage!

---

## Commandes à retenir pour la prochaine fois

```bash
# Aller dans votre projet
cd mon_projet_python

# Activer l'environnement virtuel
source venv/bin/activate

# Vous devriez voir (venv) apparaître!

# Pour désactiver quand vous avez fini
deactivate
```

**N'oubliez pas:** Activez toujours votre environnement virtuel avant de coder!
