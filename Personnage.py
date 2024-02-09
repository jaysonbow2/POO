from abc import ABC, abstractmethod

class Personnage(ABC):
    tour = 'joueur1'  # Attribut de classe pour gérer le tour

    def __init__(self, nom, force):
        self._nom = nom  # Attribut protégé pour le nom du personnage
        self._vie = 100  # Attribut protégé pour la vie initiale
        self._force = force  # Attribut protégé pour la force du personnage
        self._experience = 0  # Attribut protégé pour l'expérience, initialement à 0
        self._degats = 0  # Attribut protégé pour les dégâts subis

    @property
    def nom(self):
        return self._nom

    @property
    def vie(self):
        return self._vie - self._degats  # La vie restante après déduction des dégâts

    @property
    def experience(self):
        return self._experience

    @property
    def force(self):
        return self._force + self._experience  # La force inclut l'expérience acquise

    @property
    def degats(self):
        return self._degats

    def gagneExperience(self):
        self._experience += 1  # Augmente l'expérience de 1

    def recoitDegat(self, quantite):
        self._degats += quantite  # Augmente les dégâts subis

    @abstractmethod
    def attaque(self, adversaire):
        pass  # Méthode abstraite à implémenter dans les sous-classes
