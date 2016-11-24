from jeu421.interface import Interface
from jeu421.combinaison import *
from random import randint


class Joueur:
    """
    Classe représentant un joueur de 421. Un joueur a les attributs
    - nom: son nom
    - nb_jetons: son nombre de jetons, entier entre 0 et 21
    - combinaison actuelle: un objet de la classe Combinaison
    La classe a un attribut static interface qui est l'interface de communication entre les joueurs et le programme

    """
    interface = Interface()


    def __init__(self, nom):
        """
        Constructeur de la classe, doit initialiser le nom du joueur à la valeur passée en paramètre.
        Le nombre de jetons à zéro, et la combinaison_actuelle à None
        :param nom: nom du joueur
        """
        self.nom = nom
        self.nb_jetons = 0
        self.combinaison_actuelle = None


    def lancer_des(self, nombre_des):
        """
        Méthode permettant à un joueur de lancer dés
        :param nombre_des: nombre de dés à lancer
        :return: une liste de longueur nombre_des contenant les valeurs de chaque dés selon le lancé
        """
        self.nombre_des = nombre_des
        self.combinaison_actuelle = []
        for i in range(nombre_des):
            lancer = randint(1, 6)
            self.combinaison_actuelle.append(lancer)
        return self.combinaison_actuelle

    def jouer_tour(self, nb_maximum_lancer=3):
        """
        Cette méthode permet à un joueur de jouer lorsque c'est son tour dans une partie, en lançant les dés.
        Vous devez demandez au joueur de lancer des dés, de choisir les dés à relancer et puis changer l'attribut combinaison actuelle du
        :param nb_maximum_lancer: le nombre maximum de lancés auquel le joueur a droit lors de ce tour.
        :return: retourne le nombre de lancés que le joueur a fait.
        """
        self.nb_maximum_lancer = nb_maximum_lancer
        nb_lancer = 0
        resultat = self.lancer_des(3)
        nb_lancer += 1
        print("Voici les dés que vous avez lancé : ", resultat)
        if self.nb_maximum_lancer:
            des_relancer = int(input("Quels dés voulez-vous relancer? Veuillez entrer les chiffres à relacner séparés d'un espace"))

if __name__ == '__main__':
    joueur1 = Joueur("Antoine")
    print(joueur1.nom, joueur1. nb_jetons)
    print(joueur1.lancer_des(3))
