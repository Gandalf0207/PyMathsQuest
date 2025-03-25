# PyMathsQuest

> [!IMPORTANT]
> Pour toutes informations concernant les droits d'utilisation, veillez vous référer à la [Licence](https://github.com/Gandalf0207/PyMathsQuest?tab=License-1-ov-file)


## Présentation : 
PyMathsQuest est un projet étudiant réalisé par 2 élèves en terminale NSI : LUBAN Théo & PLADEAU Quentin. Le but de ce projet est de réaliser un petit RPG autour des mathématiques grâce au langage python et à la librairie pygame. Le jeu se veut durable et unique, c'est pourquoi le point fort est l'aléatoire. En effet, que ce soit la génération de la carte ou encore les exercices mathématiques, toutes les valeurs sont aléatoires. Cela rend donc chaque partie unique ! De plus, à la fin d'une partie, les différentes exercices rencontrés sont corrigés pas à pas pour vous aider à mieux les comprendre. Cela est possible grâce à notre librairie Py-Maths qui permet la génération d'exercices corrigés.
Ce projet est donc né de la fusion de Maths-Quest et Py-Maths deux anciens projet réalisé lors de l'année de première en NSI. 

Le projet aborde donc plusieurs notion de mathématique, les voici : 
|Seconde                         |Premiere                    |
|--------------------------------|----------------------------|
| Equation du premier degrés     | Suites |
| Volumes                        | Pôlynome du second degrés |
| Equation cartésienne de droite | Dérivés |
| Equation à 2 inconnues         | / |



## Comment jouer : 

#### Liste des contrôles
- E : permet d'interagir
- Z : Avancer
- Q : Aller a gauche
- S : Reculer
- D : Aller a droite
#### Espace : passer les dialogues
- P : Ouvrir l'onglet paramètres
- V : Ouvrir l'onglet volumes sonores
- I : Ouvrir l'inventaire
- B : Ouvrir le livre de cours
- M : Cacher la hotbar
Echap : Ouvrir le menu quitter

Au lancement initial vous devrez choisir le niveau de votre partie entre Seconde et Premiere puis votre difficulté et enfin votre langue, il suffira ensuite d'accepter la licence et d'appuyer sur commencer et le jeu se lancera.
Au début de chaque niveau, vous apparaitrez à gauche de la carte générée, vous devrez ensuite parler à divers personnages non joueur et interagir avec plusieurs éléments pour ramasser des morceaux de cours et arriver jusqu'à l'évènement qui engendre l'exercice. Si jamais vous semblez bloqué utilisez les infobulles situés dans la hotbar. Le niveau se déroulant à l'intérieur d'un volcan signifie que vous allez affronter le problème final et que le jeu est presque fini. Une fois le problème finale résolu vous aurez la possibilité de récupérer une correction des exos auxquels vous avez été confrontés ainsi qu'une médaille indiquant votre taux de réussite.


## Installation : 

> [!NOTE]
> Le projet a été développé sur le systeme d'exploitation windows 11, python 3.12.6 ainsi que les librairies présentes dans le fichier requirements.txt Si vous souhaitez modifier ces parametres, veillez à vous assurer de la compatibilité des systemes d'application et versions.

Afin de pouvoir utiliser le jeu sans soucis, nous vous demandons de bien vouloir suivre pas-à-pas l'installation du projet décrite ci-dessous.

  ##### Téléchargement des .exe nécessaires au jeu :
  Vous devez récupérer les 4 .exe qui sont nécessaires à l'installation :
  - [Git](https://git-scm.com/)
  - [Python](https://www.python.org/downloads/release/python-3123/) *Une version récente est préférable*
  - [MikTeX](https://miktex.org/download)
  - [Visual C++ x64](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)

  Une fois que vous avez récupéré ces 4 fichiers exécutables, executez-les dans l'ordre de téléchargement 1 par 1 et assurez vous d'accorder les droits et autorisation nécessaire à l'installation. Si possible ajoutez les éléments nécessaire au Path de votre ordinateur puis redémarez-le. 

  ##### Clône du repositorie GitHub:
  - Veillez à redémarrer votre machine si nécessaire pour permettre à votre système de bien intégrer l'installation des logiciels précédents. Après cela, il vous faut installer différentes dépendances nécessaires au bon fonctionnement du jeu.
  Après avoir installé les 4 fichiers executables, vous devez récupérer le projet. Pour ce faire, dans votre invite de commande, exécutez la commande ci-dessous :

  > Clone du dossier contenant le jeu
  ```
  git clone https://github.com/Gandalf0207/PyMathsQuest.git
  ```

   ##### Téléchargement des dépendances nécessaires au jeu :
  
  - Vous devez installer manuellement les dépendances. Pour ce faire, ouvrez un invite de commande (cmd / powershell...) et entrez les commandes suivantes dans l'ordre donné.
    Pour chacune des commandes en rapport avec des dépendances Latex, une fenêtre peut s'ouvrir, vous devrez accepter l'installation.

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
  - Après avoir réalisé l'installation, téléchargez les ressources (images, audios et polices) et placez ces trois dossiers dans le dossier PyMathsQuest, au même niveau que le fichier main.py.
  - Lien de téléchargement : [Lien]

<br>

Si vous rencontrez des problèmes avec des éléments de l'installation, vérifiez bien que vous respectez les différents éléments de prévention, présents dans les explications de l'installation ci-dessus.

<br>

> [!NOTE]
> Pour toutes les dépendances LaTeX, un pop-up peut s'ouvrir, vous devez cliquer sur "Install" pour pouvoir l'installer.

> [!TIP]
> Si vous utilisez une ancienne version de Windows ou bien que vous rencontrez toujours une erreur avec Visual C++ x64, installez également [Visual C++ x86](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170).

> [!TIP]
> Lorsque vous exécutez une commande **git clone**, assurez-vous que l'emplacement où vous êtes est le bon pour cloner le dossier. La commande **Git clone** est possible seulement si vous avez téléchargé et installé le .exe git. De plus, si vous possédez déjà un clone ou un dossier possédant le même nom que le projet dans le dossier destination du clône, le clône ne pourra avoir lieu.

> [!WARNING]
> Veuillez faire attention à l'emplacement d'installation des logiciels, et si nécessaire  octroyez-vous les droits en les ajoutant dans le **PATH**.

> [!WARNING]
> Si vous rencontrez un problème lors de l'installation des dépendances, après l'installation des logiciels.exe, veillez à redémarrer votre machine puis à réinstaller les dépendances.





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
  - Ce logiciel est fourni \"tel quel\", sans garantie d'aucune sorte. Les auteurs ne peuvent être tenus responsables d'éventuels dommages résultant de son utilisation.

4. Utilisation de bibliothèques open source
  - Ce projet utilise des bibliothèques open-source telles que Python, Matplotlib, LaTeX, etc. Nous respectons et apprécions le travail de leurs créateurs et nous conformons aux licences respectives de ces bibliothèques.
    
5. Crédits et cadre de réalisation
  - Ce projet a été développé par LUBAN Théo & PLADEAU Quentin dans le cadre du cours de NSI en terminale. Un grand merci à ESCOUTE Cédric et Patrice-Florent Marie-Jeanne pour leur soutien et leur enseignement.

6. Mise à jour des conditions
  - Ces conditions peuvent être mises à jour à tout moment. Consultez le dépôt GitHub pour toute information sur la licence et les modifications du projet.

© 2025 - PyMathsQuest
Publié sous licence GPL v3+",


#

*by LUBAN Théo & PLADEAU Quentin with* :heart: 

  
