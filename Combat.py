from Magicien import Magicien
from RoiSorcier import RoiSorcier
from Personnage import Personnage

class Combat:
    def demarrerCombat(self, magicien: Magicien, roiSorcier: RoiSorcier):
        while magicien.vie > 0 and roiSorcier.vie > 0:
            if Personnage.tour == 'joueur1':
                print(f"Tour de {magicien.nom}")
                magicien.attaque(roiSorcier)
                if roiSorcier.vie - roiSorcier.degats <= 0:
                    print(f"Le vainqueur est {magicien.nom}!")
                    break
                Personnage.tour = 'joueur2'
            else:
                print(f"Tour de {roiSorcier.nom}")
                roiSorcier.attaque(magicien)
                if magicien.vie - magicien.degats <= 0:
                    print(f"Le vainqueur est {roiSorcier.nom}!")
                    break
                Personnage.tour = 'joueur1'
