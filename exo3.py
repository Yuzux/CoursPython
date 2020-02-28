#import os
#os.chdir("C:/Users/Ly fucheng/OneDrive/Cours_EPSI/Python")

def ecrire() :
    fichier = open("exo3.txt", "w")
    fichier.write("Je suis l'exo 3")
    fichier.close();

def lire() :
    fichier = open("exo3.txt", "r")
    contenu = fichier.read()
    print(contenu)
    fichier.close();

ecrire()
lire()