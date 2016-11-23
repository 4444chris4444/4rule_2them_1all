from jeu421.interface import Interface
from jeu421.combinaison import *
from jeu421.joueur import Joueur


class Partie:
    """
    Classe représentant une partie de 421. Une partie a les attributs suivants:
    - nb_joueurs: le nombre de joueurs dans la partie
    - joueurs: la liste des joueurs de la partie
    - nb_jetons_du_pot: le nombre de jetons dans le pot de la partie
    - nb_maximum_lancer: le nombre maximum de lancés permis pendant la décharge
    - premier: l'indice du premier joueur pour le tour courant, donc change possiblement
    """
    interface = Interface()

    def __init__(self, nb_joueurs):
        """
        Constructeur de la classe. Vous devez initialisez les attributs
        :param nb_joueurs: le nombre de joueur de la partie
        """
        raise NotImplementedError("Partie : Constructeur de la classe ")

    def determiner_premier_lanceur(self):
        """
        Cette méthode permet de déterminer le premier joueur qui lancera dans la partie.
        Tous les joueurs sont sensé lancer un dé et c'est celui qui a le plus petit nombre qui jouera plus tard le
        premier tour.
        En cas d'égalité, les joueurs concernés répètent l'opération
        L'attribut premier de la classe est initialisé à l'appel de cette méthode
        :return:
        """
        raise NotImplementedError("Partie : determiner_premier_lanceur ")

    def jouer_tour_premiere_phase(self):
        """
        Cette méthode permet de faire le tour de tous les joueurs et leur permet de jouer pendant la charge.
        Rappel: pendant la charge chaque joueur ne peut lancer les dés qu'une seule fois et le perdant du tour doit
        prendre dans le pot un nombre de jetons égale au nombre de points du gagnant du tour.
        Vous devez afficher à l'interface un récapitulatif des jetons des joueurs après chaque tour
        :return: un tuple d'entier qui correspond à l'index du perdant et celui du gagnant du tour
        """
        raise NotImplementedError("Partie : jouer_tour_premiere_phase ")

    def jouer_tour_deuxieme_phase(self):
        """
        Cette méthode permet de faire le tour de tous les joueurs et leur permet de jouer pendant la décharge.
        Rappel: pendant la décharge chaque joueur peut lancer les  dés autant de fois que le premier joueur
        de la charge l'a fait. De plus, le gagnant du tour doit donner un nombre de jetons égale à son nombre de points au perdant du tour.
        Vous devez afficher à l'interface un récapitulatif des jetons des joueurs après le tour
        :return: un tuple d'entier qui correspond à l'index du perdant et celui du gagnant du tour
        """
        raise NotImplementedError("Partie : jouer_tour_deuxieme_phase ")

    def jouer(self):
        """
        Cette méthode permet de jouer une partie complète de 421.
        La partie doit commencer avec la détermination du joueur qui commence la décharge, puis il s'en suit la charge.
        Une fois la charge terminé, la décharge débute par le dernier perdant de la charge.
        Le jeu se termine dès qu'un joueur a tous les jetons de la partie
        """
        raise NotImplementedError("Partie : jouer ")

    def verifier_gagnant(self, joueur):
        """
        Cette méthode permet de déterminer si un joueur a gagné la partie, i.e qu'il n'a plus de jetons
        :param joueur: le joueur en question
        :return: True si le joueur n'a plus de jetons, False sinon
        """
        raise NotImplementedError("Partie : verifier_gagnant ")

    def verifier_perdant(self, joueur):
        """
        Cette méthode permet de déterminer si un joueur a perdu la partie
        :param joueur: le joueur en question
        :return: True si le joueur a tous les jetons de la partie, False sinon
        """
        raise NotImplementedError("Partie : verifier_perdant ")

    def retirer_joueur(self, position):
        """
        Retirer un joueur du jeu
        :param position: la position du joueur dans la liste des joueurs à retirer
        :return:
        """
        raise NotImplementedError("Partie : retirer_joueur ")

    def afficher_recapitulatif(self):
        """
        Affiche un tableau récapitulatif de la partie
        """
        raise NotImplementedError("Partie : afficher_recapitulatif ")
