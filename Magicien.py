import random
from Personnage import Personnage

class Magicien(Personnage):
    FORCE_FRAPPE_1 = 10
    FORCE_FRAPPE_2 = 15

    def __init__(self, nom):
        super().__init__(nom, force=Magicien.FORCE_FRAPPE_1)

    def frappeAvecSonEpee(self, adversaire):
        adversaire.recoitDegat(self.FORCE_FRAPPE_1 + self.experience)
        print(f"{self.nom} frappe avec son épée {adversaire.nom}. Vie restante de {adversaire.nom}: {adversaire.vie}")

    def attaqueAvecSonNazgul(self, adversaire):
        adversaire.recoitDegat(self.FORCE_FRAPPE_2 + self.experience)
        print(f"{self.nom} attaque avec son Nazgûl {adversaire.nom}. Vie restante de {adversaire.nom}: {adversaire.vie}")

    def attaque(self, adversaire):
        self.gagneExperience()  # Correctement appelée depuis la classe parente Personnage
        if random.choice([True, False]):
            self.frappeAvecSonEpee(adversaire)
        else:
            self.attaqueAvecSonNazgul(adversaire)
