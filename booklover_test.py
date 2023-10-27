import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Lord of the Rings", 4)
        self.assertTrue(test_object.has_read("Lord of the Rings"))

    def test_2_add_book(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Game of Thrones", 3)
        test_object.add_book("Game of Thrones", 5)
        self.assertEqual(test_object.num_books_read(), 1)

    def test_3_has_read(self): 
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Harry Potter", 4)
        self.assertTrue(test_object.has_read("Harry Potter"))

    def test_4_has_read(self): 
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Breakfast Club", 4)
        self.assertFalse(test_object.has_read("Bible"))
    
    def test_5_num_books_read(self): 
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Lord of the Rings", 4)
        test_object.add_book("Harry Potter", 4)
        test_object.add_book("Game of Thrones", 3)
        self.assertEqual(test_object.num_books_read(), 3)

    def test_6_fav_books(self):
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("Lord of the Rings", 5)
        test_object.add_book("Harry Potter", 4)
        test_object.add_book("Game of Thrones", 4)
        test_object.add_book("Breakfast Club", 2)
        test_object.add_book("If I Did It", 3)
        
        favs = test_object.fav_books()
        self.assertTrue(all(favs['book_rating'] > 3))
        

if __name__ == '__main__':
    unittest.main(verbosity=3)