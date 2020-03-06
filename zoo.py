class Animal:
    def __init__(self, nb, regimAlim, qttNouri):
        self.nb = nb
        self.regimAlim = regimAlim
        self.qttNouri = qttNouri

class Marin(Animal):
    def __init__(self, nb, regimAlim, qttNouri, pate = 0, domestique = "non", mammifere = "non"):
        super().__init__(nb, regimAlim, qttNouri)
        self.nbPates = pate
        self.domestique = domestique
        self.mammifere = mammifere

    def __str__(self):
        return "Animal marin Nombre de pates: " + str(self.nbPates) + " Mammifere : " + self.mammifere + " Domestique : " + self.domestique + " Nombre : " + str(self.nb) + " Regime alimentaire : " + self.regimAlim + " Qantite : " + str(self.qttNouri) + "g"

class Terrestre(Animal):
    def __init__(self, nb, regimAlim, qttNouri, pate, domestique, mammifere):
        super().__init__( nb, regimAlim, qttNouri)
        self.nbPates = pate
        self.domestique = domestique
        self.mammifere = mammifere
    
    def __str__(self):
        return "Animal Terrestre Nombre de pates: " + str(self.nbPates) + " Mammifere : " + self.mammifere + " Domestique : " + self.domestique + " Nombre : " + str(self.nb) + " Regime alimentaire : " + self.regimAlim + " Qantite : " + str(self.qttNouri) + "g"
    

if __name__ == "__main__":
    Animal = {}
    Animal["Humain"] = Terrestre(2, "omnivore", 600, 2, "non", "oui")
    Animal["Lion"] = Terrestre(1, "Carnivore", 3000, 4, "non", "oui")
    Animal["Lapin"] = Terrestre(7, "vegetarien", 100, 4, "oui", "oui")
    Animal["Mouton"] = Terrestre(5, "vegetarien", 500, 4, "oui", "oui")
    Animal["Chien"] = Terrestre(2, "omnivore", 500, 4, "oui", "oui")
    Animal["Pieuvre"] = Marin(1, "carnivore", 200, 0, "non", "non")
    Animal["Serpent"] = Terrestre(2, "carnivore", 200, 0, "non", "non")
    Animal["Autruche"] = Terrestre(4, "omnivore", 1000, 2, "non", "non")
    Animal["Poule"] = Terrestre(8, "omnivore", 200, 2, "oui", "non")

    for my_key in Animal:
        print("Non : " + my_key + " " + str(Animal[my_key]))

    print("--------------------------------------------------------------------")
    print("Que voulez vous faire ?")
    print("1 - Quelle quantité de nourriture acheter par semaine ?")
    print("2 - Combien y a t’il d’animaux marins ?")
    print("3 - Combien y a t’il d’omnivores ?")
    print("4 - Combien y a t’il de pattes dans ce zoo ?")

    choix = input()
    qttAchete = 0
    if choix == 1 :
        for my_key in Animal:
            qttAchete = qttAchete + (Animal[my_key].qttNouri * 7)
    
    print(qttAchete)