**LE SEIGNEUR DES ANNEAUX – Version POO**

Bienvenue dans cette simulation de combat entre un magicien blanc et un roi sorcier, inspirée de l'univers du Seigneur des Anneaux de Tolkien.

Dans ce jeu, nous allons créer des classes et des méthodes pour modéliser les actions des personnages et déterminer le vainqueur à la fin du combat.

**Classe Personnage :**

Cette classe représente les caractéristiques communes à tous les personnages du jeu :
- Nom
- Points de vie
- Force
- Expérience
- Dégâts
- Tour de jeu

Les propriétés sont privées, à l'exception de "tour" qui est publique et appartient uniquement à la classe Personnage. Des méthodes sont également définies pour gérer les actions telles que frapper, esquiver et recevoir des dégâts.

**Classe Magicien :**

Héritant de la classe Personnage, le magicien possède ses propres méthodes d'attaque telles que lancer un sort ou un rayon de lumière sombre. Il a également la capacité d'attaquer avec une force de frappe variable, basée sur son expérience.

**Classe RoiSorcier :**

Cette classe représente le roi sorcier, avec ses propres méthodes d'attaque distinctes. Tout comme le magicien, le roi sorcier peut attaquer avec différentes forces de frappe en fonction de ses actions.

**Classe Combat :**

La classe Combat permet de démarrer le combat entre le magicien et le roi sorcier. Une boucle gère les attaques de chaque combattant jusqu'à ce que l'un d'eux perde tous ses points de vie. Le vainqueur est ensuite affiché.

**Règles du jeu :**

- Chaque combattant attaque à tour de rôle.
- À chaque attaque réussie, le combattant gagne un point d'expérience, augmentant ainsi sa force de frappe.
- Les dégâts infligés à l'adversaire sont déterminés par la force de frappe du combattant attaquant.
  
**Règles de codage :**

- Chaque classe doit être écrite dans un fichier séparé.
- Le code d'appel est écrit dans index.php.
- Une méthode est fournie pour choisir aléatoirement un entier entre 1 et 2.

Avec ces règles et ces classes bien définies, vous pourrez plonger dans l'univers du Seigneur des Anneaux et vivre des combats épiques entre magiciens et rois sorciers. Que le meilleur gagne !
