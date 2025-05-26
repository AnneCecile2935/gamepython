#!/usr/bin/python
def ajouter_livre(book_list, book):
    if book in librairy:
        raise valueError("Le livre existe déjà dans la liste")
    librairy.append(book)

def rechercher_livre(librairy, query):
    query = query.lower
    return[
        book for book in librairy
        if query in book.titre.lower() or query in book.auteur.query()
    ]
def get_genre_stats(librairy):
    stats{}
    genre = getattr(book, 'genre', None)
    if genre:
        genre = genre.lower()
        stats[genre] = stats.get(genre, 0) + 1
    return stats
