from models.book import Book

b1 = Book("1984", "George Orwell", "Dystopia", 1949)
print(b1)

b2 = Book("1984", "George Orwell", "Dystopia", 1949)
print("b1 == b2 ?", b1 == b2)

print("Hash b1:", hash(b1))
print("Hash b2:", hash(b2))
