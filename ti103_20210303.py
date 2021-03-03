import random


class Etudiant:
    """
    +==============+
    | Etudiant     |
    +==============+
    | nom          |
    | prenom       |
    | numero       |
    | adresse      |
    +==============+
    """
    id_ = 0

    def __init__(self, nom, prenom, adresse):
        self.nom = nom
        self.prenom = prenom
        self.numero = self.__class__.id_
        self.adresse = adresse
        self.x = random.randint(1, 15)

        self.__class__.id_ += 1

    def email(self):
        return self.prenom + "." + self.nom + "@usb.ca"


jean_dupont = Etudiant("dupont", "jean", "N/A")
jeanne_dupont = Etudiant("dupont", "jeanne", "N/A")
guillaume_mantelet = Etudiant("mantelet", "guillaume", "N/A")

print(jean_dupont.nom)
print(guillaume_mantelet.nom)
print(jean_dupont.email())

print(Etudiant.id_)

print(jean_dupont)
print(id(jean_dupont))
print(id(Etudiant))
