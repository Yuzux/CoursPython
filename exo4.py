import sys

def ecrire(nom_fichier) :
    fichier = open(nom_fichier, "w")
    fichier.write("Je suis l'exo 4 ouai")
    fichier.close();

def lire(nom_fichier) :
    fichier = open(nom_fichier, "r")
    contenu = fichier.read()
    print(contenu)
    fichier.close();

def main() :
    file_name = sys.argv[1]
    ecrire(file_name)
    lire(file_name)

if __name__ == "__main__":
    main()