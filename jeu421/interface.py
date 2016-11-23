class Interface:
    def __init__(self):
        pass

    def choisir_des_a_relancer(self, resultat_du_lancer):
        """
        Méthode permettant de choisir selon un résultat de lancé de dés les dés qu'il veut relancer.
        Dans cette méthode, doit demander à l'utilisateur les valeurs de dés à relancer.
        Tant que les valeurs entrées ne sont pas dans la liste en paramètre, vous devez le redemander au joueur.
        :param resultat_du_lancer:  la liste des valeurs des dés où il faut choisir les valeurs de dés  à relancer
        :return: la liste des valeurs des dés choisis pour le relancement
        """
        raise NotImplementedError("Interface : choisir_des_a_relancer ")

    def demander_entree(self, message_demande=""):
        return input(message_demande)

    def afficher(self, message=""):
        print(message)
