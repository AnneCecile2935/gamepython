#!/usr/bin/python
def main():
    librairy = []

    while True:
        afficher_menu()
        choix = input("Choississez une option(1-5) :")

        if choix == 1:
            ajouter(librairy)
        elif choix == 2:
            lister(librairy)
        elif choix == 3:
            rechercher(librairy)
        elif choix == 4:
            statistiques(librairy)
        elif choix == 5:
            print("Au revoir à bientôt!")
        else:
            print("Option invalide, veuillez saisir un chiffre entre 1 et 5")
            
if __name__ == "__main__":
    main()
