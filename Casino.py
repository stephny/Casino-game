# Programme du ZCasino

# importation des fonctions utiles

import os
from random import randrange
from math import ceil


# Déclaration des fonctions

def pair(nb):
    """Fonction permettant de vérifier si un nombre est pair ou impair"""
    impair = True
    if nb % 2 == 0:
        impair = False
    return impair


# Programme pricipal

if __name__ == "__main__":

    # Déclaration des variables de départ

    argent = 1000  # On a 1000 $ au début du jeu
    continuer_partie = True  # Booléen qui est vrai tant qu'on doit
    # continuer la partie

    print("Vous vous installez à la table de roulette avec", argent, "$.")

    while continuer_partie:  # Tant qu'on doit continuer la partie

        # on demande à l'utilisateur de saisir le numero sur lequel il va miser
        numero_mise = -1
        while numero_mise < 0:
            numero_mise = input("Saisissez le numero sur lequel vous voulez miser (0 et 49): ")
            # On convertit le numero misé
            try:
                numero_mise = int(numero_mise)
                assert numero_mise < 50 and numero_mise > 0
            except ValueError:
                print("Vous n'avez pas saisis un nombre.")
                numero_mise = -1
                continue
            except AssertionError:
                print("Le numero saisi n'est pas compris entre 0 et 49.")
                numero_mise = -1
                continue
            else:

                # À présent, on sélectionne la somme à miser sur le numero
                montant_mise = -1
                while montant_mise < 0 or montant_mise > argent:
                    montant_mise = input("Saisissez votre mise : ")
                    try:
                        montant_mise = int(montant_mise)
                        assert montant_mise > 0
                    except ValueError:
                        print("Vous n'avez pas saisis un nombre.")
                        montant_mise = -1
                        continue
                    except AssertionError:
                        print("Le montant saisi n'est pas positif.")
                        montant_mise = -1
                        continue
                    else:
                        if montant_mise > argent:
                            print("Vous ne pouvez miser autant, vous n'avez que", argent, "$")

                # Le nombre misé et la mise ont été sélectionnés par
                # l'utilisateur, on fait tourner la roulette

                numero_gagnant = randrange(50)
                print("La roulette tourne... ... et s'arrête sur le numéro ", numero_gagnant)

                # On établit le gain du joueur

                if numero_gagnant == numero_mise:
                    argent = argent - montant_mise
                    print("Félicitations ! Vous obtenez ", montant_mise * 3, "$ !")
                    argent = argent + (3 * montant_mise)
                elif pair(numero_mise) == pair(numero_gagnant):  # ils sont de la même couleur
                    argent = argent - montant_mise
                    mise = montant_mise / 2
                    print("Vous avez misé sur la bonne couleur. Vous obtenez ", mise, "$")
                    argent = argent + ceil(montant_mise / 2)
                else:
                    print("Désolé l'ami, c'est pas pour cette fois. Vous perdez votre mise.")
                    argent = argent - montant_mise

                # On interrompt la partie si le joueur est ruiné
                if argent <= 0:
                    print("Vous êtes ruiné ! C'est la fin de la partie.")
                    continuer_partie = False
                else:

                    # On affiche l'argent du joueur
                    print("Vous avez à présent", argent, "$")
                    # On demande au joueur s'il veut quitter
                    quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")
                    if quitter == "o" or quitter == "O":
                        print("Vous quittez le casino avec vos gains.")
                        continuer_partie = False
