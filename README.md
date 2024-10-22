### Exemples de documentation avec Sphinx

- [Pandas](https://pandas.pydata.org/docs/)
- [Scikit-learn](https://scikit-learn.org/stable/)

### **Rappel pour Configurer Sphinx**

#### **1. Installer les prérequis**

Tout d'abord, installez les dépendances nécessaires:

```bash
pip install sphinx
pip install sphinx-autodoc-typehints
pip install sphinx-rtd-theme
```

---

#### **2. Initialiser la Documentation Sphinx**

- **Créer un répertoire pour la documentation** :
  ```bash
  mkdir doc
  cd doc
  ```

- **Lancer l'assistant de configuration Sphinx** :
  ```bash
  sphinx-quickstart
  ```
  Cela génère un prompt qui demande des infos avant de générer les fichiers de configuration de base pour Sphinx, comme `conf.py` et `index.rst`.
  Choississez l'option (y) pour séparer le `build` et le `source`

---

#### **3. Configurer le fichier `conf.py`**

Une fois que vous avez initialisé Sphinx, ouvrez le fichier `conf.py` pour configurer les extensions et définir le thème.

**Ajoutez les extensions suivantes** dans `conf.py` :

```python
extensions = [
    'sphinx.ext.autodoc',   # Génère automatiquement la documentation à partir des docstrings Python (par ex. palin.py)
    'sphinx.ext.napoleon',  # Supporte les styles de docstrings NumPy et Google
    'sphinx.ext.viewcode',  # Ajoute des liens vers le code source dans la documentation générée
    'sphinx.ext.intersphinx',  # Permet de créer des liens vers la documentation d'autres projets externes
    "sphinx_autodoc_typehints"  # Inclut automatiquement les annotations de types Python dans la documentation
]
```

- **Explications** :

  - **`sphinx.ext.autodoc`** : Cette extension extrait les docstrings de votre code Python pour générer automatiquement la documentation.
  - **`sphinx.ext.napoleon`** : Supporte les docstrings au format **Google** et **NumPy**, qui sont des formats populaires pour la documentation Python.
  - **`sphinx.ext.viewcode`** : Ajoute des liens vers le code source dans la documentation, ce qui permet de visualiser facilement le code en lien avec chaque fonction ou classe.
  - **`sphinx.ext.intersphinx`** : Permet de créer des liens vers la documentation d’autres projets, comme celle de Python, pour fournir des informations supplémentaires sur les types natifs ou autres bibliothèques.
  - **`sphinx_autodoc_typehints`** : Cette extension extrait et documente automatiquement les annotations de types Python présentes dans les signatures de fonctions et les inclut dans la documentation générée.

**Définir le thème** :

```python
html_theme = 'sphinx_rtd_theme'
```

- **`sphinx_rtd_theme`** : Définit le thème visuel utilisé pour la documentation. Le thème "Read the Docs" (RTD) est largement utilisé pour sa simplicité et son efficacité.

**Configurer le chemin d’accès à votre code source** :

Ajoutez la configuration suivante pour indiquer à Sphinx où trouver vos fichiers Python à documenter :

```python
import os
import sys
## Le chemin depuis conf.py vers les fichiers .py que l'on veut documenter.
sys.path.insert(0, os.path.abspath('../../'))
```

Suivant si on veut le résultat en numpy ou google:  
- `napoleon_google_docstring = True  `
  ou 
- `napoleon_numpy_docstring = True `

Pour enlever le nom des modules avant chaque function:
- `add_module_names = False` # True par défaut

- **Explication** :
  - **`sys.path.insert(0, os.path.abspath('../../'))`** : Cette ligne ajoute le répertoire parent à la variable `sys.path`, permettant ainsi à Sphinx de localiser et d'importer vos fichiers Python situés deux niveaux au-dessus du répertoire de documentation.
  - Exemple : Si votre documentation est dans `doc/source/` et vos fichiers Python sont à la racine du projet, cette configuration permet à Sphinx de localiser ces fichiers.

---

#### **4. Générer la Documentation API**

Utilisez la commande `sphinx-apidoc` pour générer les fichiers `.rst` à partir de votre code Python :

```bash
# depuis la racine, le point signifie le dossier courant
sphinx-apidoc -f -o doc/source/ .

# si vous êtes dans doc
sphinx-apidoc -f -o source/ ../
```

---

#### **5. Modifier `index.rst`**

Ajoutez dans `index.rst` les mots correspondant au nom des fichiers que vous voulez documenter dans l'index de la documentation. Par exemple, si nous avons deux fichiers main.py et utils.py
Même indentation que le reste mais avec un saut de ligne.
```rst
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   main
   utils
```

---

#### **6. Construire la Documentation HTML**

Générez la documentation HTML avec la commande :

```bash
sphinx-build -b html chemin_vers_dossier_source chemin_vers_dossier_build

#Par ex, si vous êtes dans la racine:
sphinx-build -b html doc/source doc/build
```

---

#### **7. Prévisualiser la Documentation**

Une fois la documentation générée, vous pouvez la prévisualiser en lançant un serveur web local :

```bash
cd doc/build
python3 -m http.server 8000
```

Accédez à la documentation dans votre navigateur via l'URL :

```
http://localhost:8000
```

---

