from random import seed
from jeu421.partie import Partie
from jeu421.interface import Interface


if __name__ == "__main__":
    seed(42) # Cette instruction sert à fixer le générateur de nombre aléatoire pour déboguer efficacement votre code
    interface = Interface()
    interface.afficher("{}\n*{:^40s}*\n*{:^40s}*\n*{:^40s}*\n{}".format("*"*42, "",
                       "Bienvenue dans le JEU du 421", "", "*"*42))
    nombre_joueur = 1
    while nombre_joueur < 2:
        nombre_joueur = int(interface.demander_entree("Veuillez saisir un nombre de joueurs (0 pour quitter le jeu): "))
        if nombre_joueur == 0:
            break
        elif not (nombre_joueur >= 2):
            interface.afficher("Le nombre doit être supérieur à 2")
        else:
            jeu = Partie(nombre_joueur)
            jeu.jouer()
