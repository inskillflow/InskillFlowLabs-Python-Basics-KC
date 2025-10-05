# Étape 0 : Préparer votre Environnement Python

## Important: Suivez cette étape obligatoirement!

Nous allons créer un environnement virtuel Python que vous utiliserez pour TOUS les exercices de ce lab.

**À chaque nouvelle étape, vous devrez réactiver cet environnement.**

---

## Qu'est-ce qu'un environnement virtuel?

Imaginez que vous avez plusieurs projets Python sur votre ordinateur. Chaque projet peut avoir besoin de différentes versions de bibliothèques (packages). Un **environnement virtuel** est comme une bulle isolée pour votre projet, qui ne mélange pas les choses avec vos autres projets.

**Analogie simple:** C'est comme avoir un sac à dos séparé pour chaque cours à l'école. Le sac pour les maths ne contient pas les affaires de français!

---

## PARTIE 1 : Vérifier Python

Avant de commencer, vérifions que Python est bien installé.

### Commande 1 : Vérifier l'environnement d'exécution

Avant de commencer, voyons sur quel système d'exploitation nous travaillons:

`cat /etc/os-release`{{execute}}

**Explication:** Cette commande affiche les informations sur le système Linux que vous utilisez.

**RÉSULTAT ATTENDU:**
Vous devriez voir quelque chose comme:
```
PRETTY_NAME="Ubuntu 24.04.3 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04.3 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
```

**Ce que cela signifie:**
- Vous travaillez sur **Ubuntu Linux** version 24.04
- C'est une version **LTS** (Long Term Support = Support à long terme)
- Le nom de code est **Noble Numbat**

**Pourquoi c'est important?** Connaître votre système aide à comprendre quelles commandes fonctionneront et comment installer des packages.

---

### Commande 2 : Vérifier la version de Python

Maintenant, vérifions que Python est bien installé:

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

### Commande 3 : Créer un dossier pour votre projet

D'abord, créons un dossier de travail:

`mkdir mon_projet_python`{{execute}}

**Explication:** Cette commande crée un nouveau dossier nommé "mon_projet_python"

---

### Commande 4 : Aller dans ce dossier

`cd mon_projet_python`{{execute}}

**Explication:** Cette commande vous déplace dans le dossier que vous venez de créer

---

### Commande 3.1 : Vérifier où vous êtes

Pour vérifier que vous êtes bien dans le bon dossier, exécutez:

`pwd`{{execute}}

**Explication:** `pwd` signifie "Print Working Directory" (afficher le répertoire de travail)

**RÉSULTAT ATTENDU:**
```
/root/mon_projet_python
```

Si vous voyez ce chemin, parfait! Vous êtes au bon endroit.

---

### Commande 3.2 : Installer le package python3-venv

Avant de créer un environnement virtuel, nous devons installer le package nécessaire:

`apt update && apt install -y python3-venv`{{execute}}

**Explication de la commande:**
- `apt update` = met à jour la liste des packages disponibles
- `&&` = ensuite (exécute la commande suivante)
- `apt install -y python3-venv` = installe le package python3-venv
- `-y` = répond automatiquement "oui" aux questions

**CE QUI SE PASSE:** Le système télécharge et installe les fichiers nécessaires pour créer des environnements virtuels Python.

⏱️ **Patience:** Cette commande peut prendre 30-60 secondes.

**RÉSULTAT ATTENDU:**
Vous verrez plusieurs lignes défiler, et à la fin quelque chose comme:
```
Setting up python3-venv ...
Done.
```

---

### Commande 4 : Créer l'environnement virtuel

Maintenant que le package est installé, créons l'environnement virtuel:

`python3 -m venv venv`{{execute}}

**Explication de la commande:**
- `python3` = utilise Python 3
- `-m venv` = utilise le module "venv" (environnement virtuel)
- `venv` = nom de notre environnement virtuel (on l'appelle "venv")

**CE QUI SE PASSE:** Python crée un dossier "venv" avec tous les fichiers nécessaires.

⏱️ **Patience:** Cette commande peut prendre 10-20 secondes.

---

### Commande 8 : Vérifier que l'environnement a été créé

`ls -la`{{execute}}

**CE QUE VOUS DEVRIEZ VOIR:**
Un dossier nommé `venv` dans la liste!

---

## PARTIE 3 : Activer l'Environnement Virtuel

Maintenant que l'environnement existe, il faut l'activer (comme "allumer" un interrupteur).

### Commande 9 : Activer l'environnement virtuel

`source venv/bin/activate`{{execute}}

**RÉSULTAT ATTENDU:**
Vous devriez voir `(venv)` apparaître au début de votre ligne de commande:

```
(venv) root@host:~/mon_projet_python#
```

**Ce `(venv)` signifie que votre environnement virtuel est ACTIF!**

---

## PARTIE 4 : Vérification Finale

### Commande 10 : Vérifier que Python utilise bien l'environnement virtuel

`which python3`{{execute}}

**RÉSULTAT ATTENDU:**
```
/root/mon_projet_python/venv/bin/python3
```

Si vous voyez le chemin avec `/venv/` dedans, c'est parfait! Python utilise maintenant votre environnement virtuel.

---

### Commande 11 : Vérifier pip (le gestionnaire de packages)

`which pip`{{execute}}

**RÉSULTAT ATTENDU:**
```
/root/mon_projet_python/venv/bin/pip
```

---

## PARTIE 5 : Installer des Packages (Optionnel)

Si vous avez besoin d'installer des bibliothèques Python plus tard:

### Commande 12 : Exemple d'installation de package

`pip install requests`{{execute}}

**CE QUE FAIT CETTE COMMANDE:**
Elle installe le package "requests" UNIQUEMENT dans votre environnement virtuel, pas globalement sur le système.

---

### Commande 13 : Voir les packages installés

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

## Résumé : Les Commandes Essentielles

Voici ce que vous venez de faire, dans l'ordre:

```bash
# Commande 1 : Vérifier l'environnement système
cat /etc/os-release

# Commande 2 : Vérifier Python
python3 --version

# Commande 3 : Créer un dossier
mkdir mon_projet_python

# Commande 4 : Aller dans le dossier
cd mon_projet_python

# Commande 5 : Vérifier où vous êtes
pwd

# Commande 6 : Installer le package venv
apt update && apt install -y python3-venv

# Commande 7 : Créer l'environnement virtuel
python3 -m venv venv

# Commande 8 : Vérifier la création
ls -la

# Commande 9 : Activer l'environnement
source venv/bin/activate

# Commande 10 : Vérifier Python dans venv
which python3

# Commande 11 : Vérifier pip
which pip
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

### Problème 2: "ensurepip is not available" ou "venv not created successfully"
**Solution:** Le package python3-venv n'est pas installé. Exécutez:
```bash
apt update && apt install -y python3-venv
```
Puis recréez l'environnement virtuel:
```bash
python3 -m venv venv
```

### Problème 3: Je ne vois pas `(venv)` après l'activation
**Solution:** Réexécutez:
```bash
source venv/bin/activate
```

### Problème 4: "Permission denied"
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

