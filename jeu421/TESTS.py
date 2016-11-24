#from jeu421.combinaison import *

@staticmethod
def trouver_valeur(representant):
    """
    Méthode statique de la classe qui permet de retourner la valeur et le type associé à une combinaison de dés
    :param representant: liste de 3 entiers, trié en ordre décroissant
    :return: tuple dont le premier élément est la valeur des dés en paramètre,
    et le second élément est leur type (de type TypeComb)
    """


    if representant == [4,2,1]:
        tuple = (int(10),)
    return tuple




def main():
    print(trouver_valeur())
















