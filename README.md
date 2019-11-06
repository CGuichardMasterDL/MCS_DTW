# MCS - DTW et reconnaissance vocale

MCS_DTW est un module de reconnaissance vocal utilisé pour reconnaître des ordres pour un petit robot. Il est développé dans le cadre de l'UE Modélisation de Calculs Scientifiques du semestre 7, M1 Informatique à l'Université Paul Sabatier de Toulouse.

## Bien commencer

Cette partie va vous servir à comprendre le projet, sa structure et son utilisation.

### Prérequis

Il est bon de savoir que certains paquets sont nécessaires au bon fonctionnement du projet. Il est préférable de développer sous un environnement **GNU/Linux**. Avant de procéder à de possibles installations mettez à jour votre système. Voici une commande très pratique :

> sudo apt update --fix-missing && sudo apt upgrade -y && sudo apt autoremove -y

#### Python3 et virtualenv

Ce projet est un projet écrit en **Python**, ce dernier doit donc être installé. La version exacte voulue est la version _3.6.8_.
Vous pouvez installer Python avec la commande :

> sudo apt install **python3**

Lors d'un développement entre plusieurs collaborateurs, il est souvent impossible de connaître l'installation des machines de chacun d'entre eux. C'est pour ça qu'il existe des outils permettant de créer des environnements de développement virtuel. En Python le grand classique est le **virtualenv**. Il crée un dossier local contenant une installation Python, et c'est cette installation qui sera utilisée lors du développement.

Installation du paquet :

> sudo apt install **virtualenv**

Vous n'aurez pas à manipuler ici le virtualenv, le **Makefile** s'en servira pour vous. Je ne détaillerai donc pas son utilisation mais je conseille de regarder quelques tutos rapides pour votre culture, l'utilisation est très simple.

#### Make

Ce projet utilise un **Makefile** pour automatiser l’exécution de tâches. Je détaillerai dans une autre section son utilisation et ses commandes. Il vous faut donc vous assurer que vous pouvez utiliser un Makefile. Si vous ne possédez pas le paquet nécessaire, vous pouvez l'installer via la commande :

> sudo apt install **build-essential**

#### Pylint

Pylint est utilisé pour noter la qualité du code. L'évaluation concerne les bonnes pratiques de programmations selon les normes PEP. Pour l'installer voici la commande :

> sudo apt install **pylint3**

L'utilisation de pylint se fera elle aussi via le **Makefile**. Son utilisation sera détaillée plus tard. Il n'évalue pas le code du point de vue fonctionnel. Faites bien attention à vérifier avec la commande suivante que pylint concerne bien la version de Python 3.6.8 :

> pylint3 --version

## Développement du projet

### Développement

Le code doit être écrit dans le dossier **mcs_dtw/**. Mais avant de coder, il vous faudra taper la commande suivante :

> make init

Cette commande va mettre en place le virtualenv, dans un dossier **venv/** qui sera créé. Si vous voulez utiliser des librairies Python qu'il faut installer via **pip** mettez le nom de la librairie dans **requirements/install.pip**.
Pour mettre à jour votre environnement d'exécution Python, tapez la commande suivante :

> make update

Il est conseillé d'utiliser cette commande après que vous ayez récupéré le travail d'autres collaborateurs, afin d'être sûr de posséder toutes les librairies nécessaires à l'exécution.

Vous pouvez organiser le code en divisant le code par package. Un package en Python est appelé "module" et est très simple à créer, il suffit de créer un dossier dans lequel vous mettez un fichier "**_\_init_\_.py**". Ainsi dans notre cas, pour créer un module "_monmodule_" dans le projet il faut faire un dossier "mcs_dtw/_monmodule_" et mettre un fichier "\__init\__.py" dedans. Tous les fichiers qui seront dans le dossier mcs_dtw/_monmodule_/, appartiendront au module _monmodule_. Vous pourrez importer le code de ce module depuis le module "top-level" mcs_dtw avec la ligne Python :

> import monpackage

Je vous conseille de vous renseigner sur l'utilisation des [modules][bf764510] en Python.
Il est préférable pour le projet de bien diviser le code dans plusieurs fichiers, afin de rendre le projet plus lisible avec une bonne organisation.

  [bf764510]: https://docs.python.org/fr/3/tutorial/modules.html "Doc module Python"

Pour vérifier la qualité de l'écriture de votre code utilisez la commande suivante :

> make evaluate

La commande vous renvoie une note du code, les rapports complets de la note étant précisés dans le dossier **out/pylint/**. Il serait préférable de maintenir une note de **10.0/10.0** . Regardez les recommandations présentes dans les rapports pour effectuer vos corrections.

### Ecriture des tests

Les tests sont effectués avec la librairie **unittest**. Celle-ci est incluse directement dans Python, pas besoin de l'installer.
Je vous conseille d'aller lire la [doc][c4c5eda2] de unittest pour écrire vos tests.

  [c4c5eda2]: https://docs.python.org/fr/3/library/unittest.html "docs.python.org unittest"

L'écriture des tests se fait dans le dossier **tests/**. Pour tester une fonctionnalité, vous pouvez créer un fichier selon le format "**test_<:fonctionnalité>.py**", avec _<:fonctionnalité>_ remplacé par le nom de la fonctionnalité testée par ce fichier de test. Pour écrire un fichier test, vous pouvez vous inspirer du fichier **tests/test_basic.py**.

Pour lancer les tests, utilisez la commande suivante :

> make test

Si vous n'avez aucune erreur, vous pouvez continuer votre développement. Sinon corrigez-les bien évidemment.

### Gestion du Git

Concernant la gestion du Git, nous allons faire un développement par branch.
Chaque branch sera nommée selon un certain format : "**<:nom>-<:fonctionnalité-à-implémenter>**". On pourrait avoir par exemple une branch _guichard-fouillededossier_, pour l'implémentation de fonctions permettant de récupérer l'ensemble des fichiers et dossiers contenus dans un répertoire.

Faites vos commits intelligemment, nommez vos commits avec des messages compréhensibles pour que les autres collaborateurs puissent savoir ce qu'apporte le commit au projet. Surtout ne commitez jamais du code non testé !

Petit rappel, pour créer une branch vous pouvez faire :

> git checkout -b <:branch-name>

Cette commande crée la branch et vous bascule dessus.
Pour voir les branches locales sur votre répertoire Git :

> git branch -v #_-a # Si vous voulez voir également les branches des remotes_

Avant de **pull** pour récupérer le travail des autres, basculez sur la branch master.

> git checkout master ; git pull

Ne travaillez _jamais_ sur le master, toujours sur une branch. Quand votre branch est finie, vous pouvez faire un push, et le signaler aux autres.

### Les commandes

Différentes commandes sont à votre disposition. En voici la liste :

- Make **init** : Crée un virtualenv, et effectue les installations nécessaires.
> make init

- Make **update** : Mets à jour l'environnement Python (librairies décrites dans "_requirements/_").
> make update

- Make **test** : Lance les tests (situés dans "_tests/_").
> make test

- Make **evaluate** : Note le code avec Pylint (Rapports complets dans "_out/pylint/_").
> make evaluate

- Make **build** : Encapsule le code pour pouvoir former un package.
> make build

- Make **package** : Créer un package distribuable du projet.
> make package

- Make **install** : Installe le projet (code Python dans "*mcs_dtw/*") dans l'environnement Python pour qu'il soit utilisable dans d'autres projets avec un simple `import mcs_dtw`. Cependant si un virtualenv est présent l'installation s'effectue dedans.
> make install

- Make **uninstall** : Désinstalle les installations du projet.
> make uninstall

- Make **cleanout** : Supprime le dossier "_out/_".
> make cleanout

- Make **cleanvenv** : Supprime le virtualenv "_venv/_".
> make cleanvenv

- Make **cleanpackage** : Supprime les dossiers générés par les commandes _build_ et _package_.
> make cleanpackage

- Make **cleanall** : Effectue _cleanout_, _cleanvenv_, et _cleanpackage_.
> make cleanall

Dans notre cas les commandes _build_, _package_, _install_, _uninstall_, _cleanpackage_ ne sont pas utiles. Les commandes à utiliser lors du développement sont _init_, _update_, _test_, et _evaluate_, ainsi que les clean.

## Les standards utilisés

Le standard Python utilisé ici est Python 3.6.8, et les standards d'écriture de code sont ceux de la norme PEP. Le linter Pylint pour Python3 est utilisé et assure le respect des normes, pour en savoir plus sur les normes de programmation vérifiées par Pylint, consultez son [site][df9924d0].

  [df9924d0]: https://www.pylint.org "www.pylint.org"

## Versionnage du projet

Ce projet est versionné avec l'outil de Git, et son [remote][5a896169] se trouve sur Github.

  [5a896169]: https://github.com/CGuichardMasterDL/MCS_DTW "https://github.com/CGuichardMasterDL/MCS_DTW"

## Auteurs

* **Clément GUICHARD** - *Maintainer* - [clement.guichard@master-developpement-logiciel.fr] ([GITHUB](https://github.com/CGuichardMasterDL))
* **Dorian AZEMA** - *Développeur* - ([GITHUB](https://github.com/dorian-pixel))
* **Kévin DELCOURT** - *Développeur* - ([GITHUB](https://github.com/KevinDelcourt))

## Licence

Voir le fichier **LICENSE**.
