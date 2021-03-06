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
        Joueur.interface.afficher("Vous avez droit à un maximum de " + str(nb_maximum_lancer) + " lancer(s).")
        Joueur.interface.demander_entree("Appuyer sur la touche enter pour lancer les dés!")
        while nb_lancer < nb_maximum_lancer:
            lancer = self.lancer_des(3-len(resultat))
            Joueur.interface.afficher("Voici les dés que vous avez présentement : " + str(resultat))
            Joueur.interface.afficher("Vous avez lancer : " + str(lancer))
            nb_lancer +=1
            if nb_lancer >= 1 and len(resultat) == 3:
                break
            elif nb_lancer < nb_maximum_lancer:
                for i in range(len(lancer)):
                    resultat.append(lancer[i])
                self.combinaison_actuelle = Combinaison(resultat).valeur
                des_a_relancer = Joueur.interface.choisir_des_a_relancer(resultat)
                if des_a_relancer == []:
                    break
                for i in des_a_relancer:
                    resultat.remove(i)
            elif nb_lancer == nb_maximum_lancer:
                for i in range(len(lancer)):
                    resultat.append(lancer[i])
                Joueur.interface.afficher("Vous avez atteint le nombre maximal de lancer")
                Joueur.interface.afficher("Votre combinaison finale est : " + str(resultat))
                self.combinaison_actuelle = Combinaison(resultat).valeur
        return nb_lancer

    def ajouter_jetons(self, nb_jetons):
        """
        Cette méthode permet d'ajouter un nombre de jetons à ceux déjà détenus par le joueur
        :param nb_jetons: nombre de jetons à ajouter
        :return aucun
        """
        self.nb_jetons += nb_jetons
        return nb_jetons

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
        chaine = str((str(self.nom) + " - " + str(self.nb_jetons)))
        return chaine


    def __le__(self, other):
        """
        Comparaison ( <= ) entre deux joueurs sur la base de leur nombre de jetons.
        :param other: le joueur auquel on se compare
        :return: True si le nombre de jetons de self est inférieur ou égal à celui de other
        """
        if self.nb_jetons <= other.nb_jetons:
            return True
        else:
            return False


    def __ge__(self, other):
        """
        Comparaison ( >= ) entre deux joueurs sur la base de leur nombre de jetons.
        :param other: le joueur auquel on se compare
        :return: True si le nombre de jetons de self est supérieur ou égal à celui de other
        """
        if self.nb_jetons >= other.nb_jetons:
            return True
        else:
            return False

    def __lt__(self, other):
        """
        Comparaison ( < ) entre deux joueurs sur la base de leur nombre de jetons.
        :param other: le joueur auquel on se compare
        :return: True si le nombre de jetons de self est inférieur à celui de other
        """
        if self.nb_jetons < other.nb_jetons:
            return True
        else:
            return False

    def __gt__(self, other):
        """
        Comparaison ( > ) entre deux joueurs sur la base de leur nombre de jetons.
        :param other: le joueur auquel on se compare
        :return: True si le nombre de jetons de self est supérieur à celui de other
        """
        if self.nb_jetons > other.nb_jetons:
            return True
        else:
            return False

    def __eq__(self, other):
        """
        Comparaison ( == ) entre deux joueurs sur la base de leur nombre de jetons.
        :param other: le joueur auquel on se compare
        :return: True si le nombre de jetons de self est égal à celui de other
        """
        if self.nb_jetons == other.nb_jetons:
            return True
        else:
            return False