from Magicien import Magicien
from RoiSorcier import RoiSorcier
from Combat import Combat

def main():
    # Création des personnages
    gandalf = Magicien("Gandalf")
    roiSorcier = RoiSorcier("Le Roi Sorcier d'Angmar")

    # Initialisation du combat
    combat = Combat()

    # Démarrage du combat
    combat.demarrerCombat(gandalf, roiSorcier)

if __name__ == "__main__":
    main()
