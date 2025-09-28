# Create a class Book.
# Attributes: title, author, year.
# Method: get_summary() → returns "Book: Title by Author (Year)".
# Create 2 book objects and print their summaries.

class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year

    def get_summary(self):
        return f"Book: {self.title} by {self.author} ({self.year})"

book1 = Book("Kite Runner","Khaled Husseni",1990)
book2 = Book("Alchemist","Pauello",1992)

print(book1.get_summary())
print(book2.get_summary())