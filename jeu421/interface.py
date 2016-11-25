class Interface:
    def __init__(self):
        pass

    def choisir_des_a_relancer(self, resultat_du_lancer):
        """
        Méthode permettant de choisir selon un résultat de lancé de dés les dés qu'il veut relancer.
        Dans cette méthode, doit demander à l'utilisateur les valeurs de dés à relancer.
        Tant que les valeurs entrées ne sont pas dans la liste en paramètre, vous devez le redemander au joueur.
        :param resultat_du_lancer:  la liste des valeurs des dés où il faut choisir les valeurs de dés à relancer
        :return: la liste des valeurs des dés choisis pour le relancement
        """
        self.resultat_du_lancer = resultat_du_lancer
        entree_incorrecte = True
        liste_retournee_relancement = []
        while entree_incorrecte == True:
            des_a_relancer = list(self.demander_entree("Quels dés voulez-vous relancer? Veuillez entrer les chiffres à relancer."
                                              "Exemple : 543. Pour garder tous vos dés, appuyez sur la touche enter "))
            for i in des_a_relancer:
                i = int(i)
                if i in resultat_du_lancer:
                    liste_retournee_relancement.append(i)
                    entree_incorrecte = False
                else:
                    self.afficher("Ce choix est invalide.")
                    entree_incorrecte = True
        return liste_retournee_relancement





    def demander_entree(self, message_demande=""):
        return input(message_demande)

    def afficher(self, message=""):
        print(message)

