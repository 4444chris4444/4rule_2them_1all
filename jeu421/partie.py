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
        self.nb_joueurs = nb_joueurs
        self.joueurs = []
        for i in range(nb_joueurs):
            nom_joueur = "Joueur" + str(i+1)
            joueur = Joueur(nom_joueur)
            self.joueurs.append(joueur.nom)
        self.nb_jetons_du_pot = 21
        self.nb_maximum_lancer = 3
        self.premier = ""


    def determiner_premier_lanceur(self):
        """
        Cette méthode permet de déterminer le premier joueur qui lancera dans la partie.
        Tous les joueurs sont sensé lancer un dé et c'est celui qui a le plus petit nombre qui jouera plus tard le
        premier tour.
        En cas d'égalité, les joueurs concernés répètent l'opération
        L'attribut premier de la classe est initialisé à l'appel de cette méthode
        :return:
        """
        Partie.interface.afficher("*------Détermination du premier joueur------*")
        joueurs = self.joueurs
        recommencer = True
        while recommencer == True:
            plus_petit_lancer = 0
            rejouer = []
            for i in joueurs:
                lanceur_actuel = i
                #Partie.interface.demander_entree("C'est au tour du " + str(lanceur_actuel) + " de jouer. Appuyez sur la toucher Enter pour lancer les dés.")


                lancer = Joueur(lanceur_actuel).lancer_des(1)
                for x in lancer:
                    lancer = x
                    Partie.interface.afficher("Vous avez lancé un " + str(lancer))
                if plus_petit_lancer == 0:
                    plus_petit_lancer = lancer
                    rejouer.append(lanceur_actuel)
                elif plus_petit_lancer > lancer:
                    plus_petit_lancer = lancer
                    rejouer = []
                    rejouer.append(lanceur_actuel)
                elif plus_petit_lancer == lancer:
                    rejouer.append(lanceur_actuel)
            if len(rejouer)>1 :
                joueurs = rejouer
                recommencer = True
                Partie.interface.afficher("Plusieurs joueurs ont tirés la valeur la plus basse. Ils devront donc "
                                          "relancer.")
                for i in rejouer:
                    Partie.interface.afficher("Le " + str(i) + " devra relancer")
            else:
                for i in rejouer:
                    self.premier = i
                recommencer = False
        Partie.interface.afficher("Le " + str(self.premier) + " sera le premier lanceur.")


    def jouer_tour_premiere_phase(self):
        """
        Cette méthode permet de faire le tour de tous les joueurs et leur permet de jouer pendant la charge.
        Rappel: pendant la charge chaque joueur ne peut lancer les dés qu'une seule fois et le perdant du tour doit
        prendre dans le pot un nombre de jetons égale au nombre de points du gagnant du tour.
        Vous devez afficher à l'interface un récapitulatif des jetons des joueurs après chaque tour
        :return: un tuple d'entier qui correspond à l'index du perdant et celui du gagnant du tour
        """
        self.joueurs.remove(self.premier)
        self.joueurs.insert(0, self.premier)
        while self.nb_jetons_du_pot > 0:
            combinaison_plus_faible = 0
            combinaison_plus_forte = 0
            perdant = []
            gagnant = []
            for i in self.joueurs:
                joueur = Joueur(i)
                lancer = joueur.lancer_des(3)
                valeur_lancer = Combinaison(lancer).valeur
                if Combinaison(lancer).est_nenette():
                    joueur.ajouter_jetons(2)
                elif combinaison_plus_faible == 0:
                    combinaison_plus_faible = valeur_lancer
                    combinaison_plus_forte = valeur_lancer
                    perdant = joueur
                    gagnant = joueur
                elif combinaison_plus_faible > valeur_lancer:
                    combinaison_plus_faible = valeur_lancer
                    perdant = joueur
                elif combinaison_plus_forte <= valeur_lancer:
                    combinaison_plus_forte = valeur_lancer
                    gagnant = joueur
            if combinaison_plus_faible > self.nb_jetons_du_pot:
                self.nb_jetons_du_pot -= self.nb_jetons_du_pot
                perdant.nb_jetons += self.nb_jetons_du_pot
            elif combinaison_plus_faible < self.nb_jetons_du_pot:
                self.nb_jetons_du_pot -= combinaison_plus_forte
                perdant.nb_jetons += combinaison_plus_forte
        return (self.joueurs.index(perdant), self.joueurs.index(gagnant))


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
        Partie.determiner_premier_lanceur(self)
        Partie.jouer_tour_premiere_phase(self)
        Partie.jouer_tour_deuxieme_phase(self)

    def verifier_gagnant(self, joueur):
        """
        Cette méthode permet de déterminer si un joueur a gagné la partie, i.e qu'il n'a plus de jetons
        :param joueur: le joueur en question
        :return: True si le joueur n'a plus de jetons, False sinon
        """
        if joueur.nb_jetons == 0:
            return True
        else:
            return False


    def verifier_perdant(self, joueur):
        """
        Cette méthode permet de déterminer si un joueur a perdu la partie
        :param joueur: le joueur en question
        :return: True si le joueur a tous les jetons de la partie, False sinon
        """
        if joueur.nb_jetons == 21:
            return True
        else:
            return False

    def retirer_joueur(self, position):
        """
        Retirer un joueur du jeu
        :param position: la position du joueur dans la liste des joueurs à retirer
        :return:
        """
        del self.joueurs[position]

    def afficher_recapitulatif(self):
        """
        Affiche un tableau récapitulatif de la partie
        """
        Partie.interface.afficher("{}\n|{:^41s}| \n|{:^41s}|\n|{:^41s}|\n{}".format("_" * 42, "","Récapitulatif de la partie", "","_" * 42))