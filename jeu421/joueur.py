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
        Vous devez demandez au joueur de lancer des dés, de choisir les dés à relancer et puis changer l'attribut
        combinaison actuelle du joueur.
        :param nb_maximum_lancer: le nombre maximum de lancés auquel le joueur a droit lors de ce tour.
        :return: retourne le nombre de lancés que le joueur a fait.
        """
        self.nb_maximum_lancer = nb_maximum_lancer
        nb_lancer = 0
        resultat = []
        continuer = False
        input("Appuyer sur la touche enter pour lancer les dés!")
        while continuer != True:
            tirage = self.lancer_des(3-len(resultat))
            nb_lancer += 1
            print("Voici les dés que vous avez lancés : ", tirage)
            if nb_lancer == self.nb_maximum_lancer:
                print("Vous avez atteint le nombre maximal de lancer!")
                for i in range(len(tirage)):
                     resultat.append(tirage[i])
                continuer = True
            elif nb_lancer < self.nb_maximum_lancer:
                print("Voici les dés que vous avez gardés", resultat)
                des_relancer = list(input("Quels dés voulez-vous relancer? Veuillez entrer les chiffres à relancer. "
                                          "Exemple : 543. Pour garder tous vos dés, appuyez sur la touche enter "))
                if des_relancer == []:
                    for i in range(len(tirage)):
                        resultat.append(tirage[i])
                    break
                for i in des_relancer:
                    i = int(i)
                    if i in(tirage):
                        tirage.remove(i)
                    else:
                        print("Ce choix est invalide.")
                for i in range(len(tirage)):
                     resultat.append(tirage[i])
        self.combinaison_actuelle = resultat
        print("Votre combinaison finale :", self.combinaison_actuelle)
        return nb_lancer

    def ajouter_jetons(self, nb_jetons):
        """
        Cette méthode permet d'ajouter un nombre de jetons à ceux déjà détenus par le joueur
        :param nb_jetons: nombre de jetons à ajouter
        :return aucun
        """
        self.nb_jetons += nb_jetons

    def retirer_jetons(self, nb_jetons):
        """
        Cette méthode permet de retirer un nombre de jetons de ceux détenus par le joueur
        :param nb_jetons: nombre de jetons à retirer
        :return aucun
        """
        self.nb_jetons -= nb_jetons

    def __str__(self):
        """
        Cette méthode retourne une représentation d'un joueur. le format est "nom_du_joueur - nombre_de_jetons"
        Cette méthode est appelée lorsque vous faites print(A) où A est un joueur
        :return: retourne une chaine de caractère qui est une représentation.
            Exemple: "Joueur1 - 12"
        """
        chaine = str((self.nom, " - ", self.nb_jetons))
        return chaine


    def __le__(self, other):
        """
        Comparaison ( <= ) entre deux joueurs sur la base de leur nombre de jetons.
        :param other: le joueur auquel on se compare
        :return: True si le nombre de jetons de self est inférieur ou égal à celui de other
        """
        if self.nb_jetons <= other:
            return True


    def __ge__(self, other):
        """
        Comparaison ( >= ) entre deux joueurs sur la base de leur nombre de jetons.
        :param other: le joueur auquel on se compare
        :return: True si le nombre de jetons de self est supérieur ou égal à celui de other
        """
        if self.nb_jetons >= other:
            return True

    def __lt__(self, other):
        """
        Comparaison ( < ) entre deux joueurs sur la base de leur nombre de jetons.
        :param other: le joueur auquel on se compare
        :return: True si le nombre de jetons de self est inférieur à celui de other
        """
        raise NotImplementedError("Joueur : __lt__ ")

    def __gt__(self, other):
        """
        Comparaison ( > ) entre deux joueurs sur la base de leur nombre de jetons.
        :param other: le joueur auquel on se compare
        :return: True si le nombre de jetons de self est supérieur à celui de other
        """
        raise NotImplementedError("Joueur : __gt__ ")

    def __eq__(self, other):
        """
        Comparaison ( == ) entre deux joueurs sur la base de leur nombre de jetons.
        :param other: le joueur auquel on se compare
        :return: True si le nombre de jetons de self est égal à celui de other
        """
        raise NotImplementedError("Joueur : __eq__")

if __name__ == '__main__':
     joueur = Joueur("Antoine")
     #print(joueur)
     #print(joueur.lancer_des(3))
     print(joueur.jouer_tour(3))
     #print(joueur.combinaison_actuelle)
     #print(joueur.nom)
     print(joueur.nb_jetons)
     joueur.ajouter_jetons(10)
     print(joueur.nb_jetons)
     joueur.retirer_jetons(5)
     print(joueur)
     print(joueur.__le__(10))