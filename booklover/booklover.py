import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0, book_list = None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        if book_list is None:
            self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        else:
            self.book_list = book_list
                   
    def add_book(self, book_name, rating):
        if not self.has_read(book_name):
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
            print(f"{book_name} added to list.")
        else:
            print(f"{book_name} already in list.")
        
    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values
    
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
    

if __name__ == "__main__":
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("Breakfast Club", 2)
    test_object.add_book("Harry Potter", 5)
    test_object.add_book("Lord of the Rings", 4)
    test_object.add_book("Game of Thrones", 3)
    test_object.add_book("Harry Potter", 4)

    # checking if book has been read
    print("Has Han read 'Harry Potter'? ", test_object.has_read("Harry Potter"))  # Should be True
    print("Has Han read 'Dr Suess'? ", test_object.has_read("Dr. Suess"))  # Should be False

    # getting num books read
    print("Number of books: ", test_object.num_books_read())  # Should be 5

    # show favorite books
    print("Favorite books:")
    print(test_object.fav_books())
