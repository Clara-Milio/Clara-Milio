from random import randint

#liste des différentes possibilitées (pierre, feuille, ciseaux)
possi = ["pierre", "feuille", "ciseaux"]

#pour que l'ordi puisse choisir au hasard
ordi = possi[randint(0,2)]

#pour permettre le compte des points 
points_joueur = 0
points_ordi = 0
continuer = True

#algorithme global jeu (conditions etc.)

while(continuer):
    joueur = (input("pierre, feuille, ou ciseaux ? ou écrire Fin pour arrêter\n")).lower()
    if (joueur == "Fin") :
        continuer = False
        print ("voici les scores")
        print("joueur : ", points_joueur)
        print ("ordi : ", points_ordi)
    elif (joueur == ordi) :
        print ("Egalité !")
    elif (joueur == "pierre") :
        if (ordi == "papier") :
            print ("Perdu BOUUUH trop nul", ordi, "recouvre", joueur)
            points_ordi = points_ordi + 1
        else :
            print ("Gagné sale bg", joueur, "écrase", ordi)
            points_joueur = points_joueur + 1
    elif (joueur == "papier") :
        if (ordi == "ciseaux") :
            print ("Perdu trop la honte", ordi, "cut", joueur)
            points_ordi = point_ordi + 1
        else:
            print ("bravo bg", joueur, "recouvre", ordi)
            points_joueur = points_joueur + 1
    elif (joueur == "ciseaux"):
        if (ordi == "pierre"):
            print ("jamais vu quelqu'un d'aussi claqué", ordi, "écrase", joueur)
            points_ordi = points_ordi + 1
        else:
            print ("t'es un génie ou quoi ? féliciation", joueur, "cut", ordi)
            points_joueur = points_joueur + 1
    else:
        print ("votre choix n'existe pas !")

#pour permettre à l'ordinateur de random à chaque tour et permettre le tour suivant 
ordi = possi[randint(0,2)]
print ("prochain tour !")


