from Personnage import Personnage

class RoiSorcier(Personnage):
    def __init__(self, nom):
        super().__init__(nom, force=20)

    def attaque(self, adversaire):
        self.gagneExperience()
        force_de_frappe = self._force + self._experience  # Accès aux attributs protégés
        adversaire.recoitDegat(force_de_frappe)
        print(f"{self._nom} attaque {adversaire.nom}. Vie restante de {adversaire.nom}: {adversaire.vie}")
