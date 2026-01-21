# PyMathsQuest

> [!IMPORTANT]
> Pour toute information concernant les droits d'utilisation, veuillez vous référer à la [Licence](https://github.com/Gandalf0207/PyMathsQuest?tab=License-1-ov-file)


## Présentation : 
PyMathsQuest est un projet étudiant réalisé par 2 élèves en terminale NSI : LUBAN Théo & PLADEAU Quentin. Le but de ce projet est de réaliser un petit RPG autour des mathématiques grâce au langage Python et à la librairie Pygame. Le jeu se veut durable et unique, c'est pourquoi le point fort est l'aléatoire. En effet, que ce soit la génération de la carte ou encore les exercices mathématiques, toutes les valeurs sont aléatoires. Cela rend donc chaque partie unique ! De plus, à la fin d'une partie, les différentes exercices rencontrés sont corrigés pas à pas pour vous aider à mieux les comprendre. Cela est possible grâce à notre librairie Py-Maths qui permet la génération d'exercices corrigés.
Ce projet est donc né de la fusion de Maths-Quest et Py-Maths, deux anciens projets réalisé lors de l'année de première en NSI. 

> Vidéo de présentation : [Lien](https://tube-sciences-technologies.apps.education.fr/w/c1FtXNSUYeibzeNaJ65ha7)

Le projet aborde donc plusieurs notions de mathématiques, les voici : 
|Seconde                         |Premiere                    |
|--------------------------------|----------------------------|
| Equation du premier degrés     | Suites |
| Volumes                        | Pôlynome du second degrés |
| Equation cartésienne de droite | Dérivées |
| Equation à 2 inconnues         | / |



## Comment jouer : 

#### Liste des contrôles
- E : permet d'interagir
- Z : Avancer
- Q : Aller à gauche
- S : Reculer
- D : Aller à droite
#### Espace : Passer les dialogues
- P : Ouvrir l'onglet paramètres
- V : Ouvrir l'onglet volumes sonores
- I : Ouvrir l'inventaire
- B : Ouvrir le livre de cours
- M : Cacher la hotbar
Echap : Ouvrir le menu général / quitter un menu ouvert

Au lancement initial vous devrez choisir le niveau de votre partie entre Seconde et Premiere puis votre difficulté et enfin votre langue, il suffira ensuite d'accepter la licence et d'appuyer sur Commencer et le jeu se lancera.
Au début de chaque niveau, vous apparaîtrez à gauche de la carte générée, vous devrez ensuite parler à divers personnages non joueurs et interagir avec plusieurs éléments pour ramasser des morceaux de cours et arriver jusqu'à l'événement qui engendre l'exercice. Si jamais vous semblez bloqué, utilisez les infobulles situées dans la hotbar. Le niveau se déroulant à l'intérieur d'un volcan signifie que vous allez affronter le problème final et que le jeu est presque terminé. Une fois le problème final résolu, vous aurez la possibilité de récupérer une correction des exercices auxquels vous avez été confronté(e) ainsi qu'une médaille indiquant votre taux de réussite.


## Installation : 

> [!NOTE]
> Le projet a été développé sur le systeme d'exploitation Windows 11, Python 3.12.6 ainsi que les librairies présentes dans le fichier requirements.txt Si vous souhaitez modifier ces paramètres, veillez à vous assurer de la compatibilité des systèmes d'application et versions.

Afin de pouvoir utiliser le jeu sans soucis, nous vous demandons de bien vouloir suivre pas-à-pas l'installation du projet décrite ci-dessous.

  ##### Téléchargement des .exe nécessaires au jeu :
  Vous devez récupérer les 4 .exe qui sont nécessaires à l'installation :
  - [Git](https://git-scm.com/)
  - [Python](https://www.python.org/downloads/release/python-3123/) *Une version récente est préférable*
  - [MikTeX](https://miktex.org/download)
  - [Visual C++ x64](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)

  Une fois que vous avez récupéré ces 4 fichiers exécutables, executez-les dans l'ordre de téléchargement 1 par 1 et assurez-vous d'accorder les droits et autorisations nécessaires à l'installation. Si possible ajoutez les éléments nécessaires au PATH de votre ordinateur puis redémarrez-le. 

  ##### Clone du repository GitHub:
  - Veillez à redémarrer votre machine si nécessaire pour permettre à votre système de bien intégrer l'installation des logiciels précédents. Après cela, il vous faut installer différentes dépendances nécessaires au bon fonctionnement du jeu.
  Après avoir installé les 4 fichiers éxecutables, vous devez récupérer le projet. Pour ce faire, dans votre invite de commandes, éxecutez la commande ci-dessous :

  > Clone du dossier contenant le jeu
  ```
  git clone https://github.com/Gandalf0207/PyMathsQuest.git
  ```

   ##### Téléchargement des dépendances nécessaires au jeu :
  
  - Vous devez installer manuellement les dépendances. Pour ce faire, ouvrez un invite de commande (cmd / powershell...) et entrez les commandes suivantes dans l'ordre donné.
    Pour chacune des commandes en rapport avec des dépendances LaTeX, une fenêtre peut s'ouvrir, vous devrez accepter l'installation.

  > Mettre à jour pip 
  ```
  python -m ensurepip --upgrade
  python -m pip install --upgrade pip
  ```
  > Installation de la dépendance : requirements.txt
  ```
  python -m pip install -r requirements.txt
  ```
  > Installation extension LaTeX : type1cm.sty
  ```
  mpm --install type1cm
  ```
  > Installation extension LaTeX : type1ec.sty
  ```
  mpm --install cm-super
  ```
  > Installation extension LaTeX : geometry.sty
  ```
  mpm --install geometry
  ```
  > Installation extension LaTeX : underscore.sty
  ```
  mpm --install underscore
  ```
  > Installation extension LaTeX : ttfonts.map
  ```
  mpm --install zhmetrics
  ```
  > Installation extension LaTeX : amsmath
  ```
  mpm --install amsmath
  ```
<br>

   ##### Téléchargement des ressources nécessaires au jeu :
  - Après avoir réalisé l'installation, téléchargez les ressources (image, sound et font) et placez ces trois dossiers dans le dossier PyMathsQuest, au même niveau que le fichier main.py.
  - Lien de téléchargement : [Lien](https://drive.google.com/drive/folders/1XCcF6rdsKvm3UJO9cKkHlKfWQ4sPczDr?usp=sharing)

<br>

Si vous rencontrez des problèmes avec des éléments de l'installation, vérifiez bien que vous respectez les différents éléments de prévention, présents dans les explications de l'installation ci-dessus.

<br>

> [!NOTE]
> Pour toutes les dépendances LaTeX, un pop-up peut s'ouvrir, vous devez cliquer sur "Install" pour pouvoir l'installer.

> [!TIP]
> Si vous utilisez une ancienne version de Windows ou bien que vous rencontrez toujours une erreur avec Visual C++ x64, installez également [Visual C++ x86](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170).

> [!TIP]
> Lorsque vous exécutez une commande **git clone**, assurez-vous que l'emplacement où vous êtes est le bon pour cloner le dossier. La commande **Git clone** est possible seulement si vous avez téléchargé et installé le .exe git. De plus, si vous possédez déjà un clone ou un dossier possédant le même nom que le projet dans le dossier destination du clone, le clone ne pourra avoir lieu.

> [!WARNING]
> Veuillez faire attention à l'emplacement d'installation des logiciels, et si nécessaire octroyez-vous les droits en les ajoutant dans le **PATH**.

> [!WARNING]
> Si vous rencontrez un problème lors de l'installation des dépendances, après l'installation des logiciels.exe, veillez à redémarrer votre machine puis à réinstaller les dépendances.

<br>

### Menu Administrateur

> Un menu administrateur a était implémenté au sein du projet. Pour ouvrir son interface taper simplement le nom "patrick".
> Vous aurez la possibilité de modifier de nombreux éléments, comme l'obtention des cours, le changement de niveau, l'ouverture d'exercice directement...
> Attention, certaines modifications via le menu admin peuvent provoquer des erreurs de chargement.


<br> </br>
## Crédits & Termes et Conditions d'utilisation :
1. Liberté d'utilisation, de modification et de distribution : 
  - Ce programme est sous licence GPL v3+, ce qui signifie que vous êtes libre de :
  - Exécuter le logiciel pour tout usage (personnel, éducatif, commercial, etc.).
  - Étudier, modifier et améliorer son code source.
  - Redistribuer des copies du programme, modifiées ou non, à condition de respecter la même licence.

2. Code source et contributions
  - Le code source du projet est accessible sur GitHub :👉 https://github.com/Gandalf0207/PyMathsQuest
  - Toute contribution est la bienvenue tant qu'elle respecte les termes de la GPL v3.
  
3. Aucune garantie
  - Ce logiciel est fourni tel quel, sans garantie d'aucune sorte. Les auteurs ne peuvent être tenus responsables d'éventuels dommages résultant de son utilisation.

4. Utilisation de bibliothèques open source
  - Ce projet utilise des bibliothèques open-source telles que Python, Matplotlib, LaTeX, etc. Nous respectons et apprécions le travail de leurs créateurs et nous conformons aux licences respectives de ces bibliothèques.
    
5. Crédits et cadre de réalisation
  - Ce projet a été développé par LUBAN Théo & PLADEAU Quentin dans le cadre du cours de NSI en terminale. Un grand merci à ESCOUTE Cédric et MARIE-JEANNE Patrice-Florent pour leur soutien et leur enseignement.

6. Mise à jour des conditions
  - Ces conditions peuvent être mises à jour à tout moment. Consultez le dépôt GitHub pour toute information sur la licence et les modifications du projet.

© 2025 - PyMathsQuest
Publié sous licence GPL v3+",


#

*by LUBAN Théo & PLADEAU Quentin with* :heart: 

  
