#!/usr/bin/python
class Book:
    """
    A class to represent book.

    Attributes:
        titre : titre du livre
        auteur : auteur du libre
        genre : genre du livre
        année : année de parution du livre

        Example:
        >>> b = Book("1984", "George Orwell", "Fiction", 1949)
        >>> str(b)
        '1984 by George Orwell (Fiction, 1949)'

    """
    def __init__(self, titre, auteur, genre, annee):
        self.titre = titre
        self.auteur = auteur
        self.genre = genre
        self.annee = annee

    def __str__(self):
        """ Affiche le livre"""
        return f"{self.titre} par {self.auteur} {self.genre}, {self.annee}"

    def __eq__(self, other):
        """ Vérifie si deux livres ont le même titre, auteur, genre et année
        """
        if not isinstance(other, Book):
            return NotImplemented
        return (self.titre == other.titre and
                self.auteur == other.auteur and
                self.genre == other.genre and
                self.annee == other.annee)

    def __hash__(self):
        """
        pourra être utilisé comme clé de dictionnaire(dict) ou un élément d'ensemble
        (set)
        """
        return hash((self.titre, self.auteur, self.genre, self.annee))

    def afficher_menu(librairy):
        print("Menu")
        print("1. AJouter un livre")
        print("2. Lister les livres")
        print("3. Rechercher un livre")
        print("4. Statistiques")
        print("5. Quitter")

    def ajouter(librairy):
        titre = input("Titre du livre : ")
        auteur = input("Auteur du livre : ")
        genre = input("Genre du livre : ")
        annee = input("Année de publication du livre : ")
        livre = Book(titre, auteur, genre, annee)
        librairy.append(livre)
        print("Le livre a été ajouté avec succès")

    def lister(librairy):
        pass

    def rechercher(librairy):
        pass

    def statistiques(librairy):
        pass

    def quitter(self, value):
        pass
    """

    """
