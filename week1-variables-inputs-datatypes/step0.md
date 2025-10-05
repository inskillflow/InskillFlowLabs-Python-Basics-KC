# Étape 0 : Préparer votre Environnement Python

## Qu'est-ce qu'un environnement virtuel?

Imaginez que vous avez plusieurs projets Python sur votre ordinateur. Chaque projet peut avoir besoin de différentes versions de bibliothèques (packages). Un **environnement virtuel** est comme une bulle isolée pour votre projet, qui ne mélange pas les choses avec vos autres projets.

**Analogie simple:** C'est comme avoir un sac à dos séparé pour chaque cours à l'école. Le sac pour les maths ne contient pas les affaires de français!

---

## PARTIE 1 : Vérifier Python

Avant de commencer, vérifions que Python est bien installé.

### Commande 1 : Vérifier la version de Python

Cliquez sur ce bouton pour vérifier:

`python3 --version`{{execute}}

**RÉSULTAT ATTENDU:**
Vous devriez voir quelque chose comme:
```
Python 3.11.x
```

Si vous voyez ce message, parfait! Python est installé.

---

## PARTIE 2 : Créer l'Environnement Virtuel

Maintenant, nous allons créer un environnement virtuel pour notre projet Python.

### Commande 2 : Créer un dossier pour votre projet

D'abord, créons un dossier de travail:

`mkdir mon_projet_python`{{execute}}

**Explication:** Cette commande crée un nouveau dossier nommé "mon_projet_python"

---

### Commande 3 : Aller dans ce dossier

`cd mon_projet_python`{{execute}}

**Explication:** Cette commande vous déplace dans le dossier que vous venez de créer

**VÉRIFICATION:** Votre terminal devrait maintenant montrer que vous êtes dans `/root/mon_projet_python`

---

### Commande 4 : Créer l'environnement virtuel

`python3 -m venv venv`{{execute}}

**Explication de la commande:**
- `python3` = utilise Python 3
- `-m venv` = utilise le module "venv" (environnement virtuel)
- `venv` = nom de notre environnement virtuel (on l'appelle "venv")

**CE QUI SE PASSE:** Python crée un dossier "venv" avec tous les fichiers nécessaires.

⏱️ **Patience:** Cette commande peut prendre 10-20 secondes.

---

### Commande 5 : Vérifier que l'environnement a été créé

`ls -la`{{execute}}

**CE QUE VOUS DEVRIEZ VOIR:**
Un dossier nommé `venv` dans la liste!

---

## PARTIE 3 : Activer l'Environnement Virtuel

Maintenant que l'environnement existe, il faut l'activer (comme "allumer" un interrupteur).

### Commande 6 : Activer l'environnement virtuel

`source venv/bin/activate`{{execute}}

**RÉSULTAT ATTENDU:**
Vous devriez voir `(venv)` apparaître au début de votre ligne de commande:

```
(venv) root@host:~/mon_projet_python#
```

**Ce `(venv)` signifie que votre environnement virtuel est ACTIF!**

---

## PARTIE 4 : Vérification Finale

### Commande 7 : Vérifier que Python utilise bien l'environnement virtuel

`which python3`{{execute}}

**RÉSULTAT ATTENDU:**
```
/root/mon_projet_python/venv/bin/python3
```

Si vous voyez le chemin avec `/venv/` dedans, c'est parfait! Python utilise maintenant votre environnement virtuel.

---

### Commande 8 : Vérifier pip (le gestionnaire de packages)

`which pip`{{execute}}

**RÉSULTAT ATTENDU:**
```
/root/mon_projet_python/venv/bin/pip
```

---

## PARTIE 5 : Installer des Packages (Optionnel)

Si vous avez besoin d'installer des bibliothèques Python plus tard:

### Commande 9 : Exemple d'installation de package

`pip install requests`{{execute}}

**CE QUE FAIT CETTE COMMANDE:**
Elle installe le package "requests" UNIQUEMENT dans votre environnement virtuel, pas globalement sur le système.

---

### Commande 10 : Voir les packages installés

`pip list`{{execute}}

**RÉSULTAT:** Vous verrez la liste de tous les packages installés dans votre environnement.

---

## IMPORTANT : Commandes à Retenir

### ✅ ACTIVER l'environnement virtuel (à faire CHAQUE FOIS que vous ouvrez un nouveau terminal):
```bash
source venv/bin/activate
```

Vous verrez `(venv)` apparaître au début de votre ligne.

---

### ❌ DÉSACTIVER l'environnement virtuel (quand vous avez fini):
```bash
deactivate
```

Le `(venv)` va disparaître.

---

## Résumé : Les 6 Commandes Essentielles

Voici ce que vous venez de faire, dans l'ordre:

```bash
# Commande 1 : Vérifier Python
python3 --version

# Commande 2 : Créer un dossier
mkdir mon_projet_python

# Commande 3 : Aller dans le dossier
cd mon_projet_python

# Commande 4 : Créer l'environnement virtuel
python3 -m venv venv

# Commande 5 : Vérifier
ls -la

# Commande 6 : Activer l'environnement
source venv/bin/activate
```

**Vous verrez `(venv)` au début de votre ligne = environnement actif!**

---

## Aide-Mémoire Visuel

```
┌─────────────────────────────────────┐
│  SANS environnement virtuel         │
│  root@host:~#                       │
└─────────────────────────────────────┘

         ↓ (activation)

┌─────────────────────────────────────┐
│  AVEC environnement virtuel         │
│  (venv) root@host:~#               │
└─────────────────────────────────────┘
```

Le `(venv)` vous indique que l'environnement est actif!

---

## Pourquoi c'est Important?

1. **Isolation:** Vos packages ne vont pas interférer avec d'autres projets
2. **Propreté:** Vous pouvez facilement supprimer tout en supprimant le dossier `venv`
3. **Reproductibilité:** Facile de recréer le même environnement sur un autre ordinateur
4. **Bonne pratique:** C'est comme ça que les professionnels travaillent!

---

## Que Faire si Quelque Chose ne Marche Pas?

### Problème 1: "command not found: python3"
**Solution:** Python n'est pas installé. Contactez votre formateur.

### Problème 2: Je ne vois pas `(venv)` après l'activation
**Solution:** Réexécutez:
```bash
source venv/bin/activate
```

### Problème 3: "Permission denied"
**Solution:** Assurez-vous d'être dans le bon dossier avec `pwd`

---

## C'est Prêt!

Votre environnement virtuel est maintenant configuré! Vous êtes prêt à commencer à coder en Python.

**IMPORTANT:** Pour les prochaines étapes de ce lab, assurez-vous que vous voyez toujours `(venv)` au début de votre ligne de commande. Si ce n'est pas le cas, réactivez-le avec:

```bash
source venv/bin/activate
```

---

Cliquez sur "Continuer" pour commencer à apprendre les variables Python!

