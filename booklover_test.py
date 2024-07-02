import unittest

from booklover import BookLover



class BookLoverTestSuite(unittest.TestCase):



    def test_1_add_book(self): 

        # add a book and test if it is in `book_list`.

        reader1 = BookLover('Sarah', 'Sarah_Reads@gmail.com', 'horror')

        reader1.add_book('Lord of the Rings', 4)

        

        #error message in case test fails

        message = "Book is already in list"

        

        #assertTrue(test_value, message)

        self.assertTrue('Lord of the Rings' in reader1.book_list['book_name'].values, message)

        

        print(reader1.book_list)



    def test_2_add_book(self):

        # add the same book twice. Test if it's in `book_list` only once.

        reader1 = BookLover('Sarah', 'Sarah_Reads@gmail.com', 'horror')

        reader1.add_book('Lord of the Rings', 4)

        reader1.add_book('Lord of the Rings', 4)

        

        expected = 1

        

        #error message in case test fails

        message = "Book is already in list"

        

        #assertEqual(first_val, second_val, message)

        self.assertEqual(len(reader1.book_list[reader1.book_list['book_name'] == 'Lord of the Rings']), expected, message)

        

        

        

        print(reader1.book_list)



    def test_3_has_read(self): 

        # pass a book in the list and test if the answer is `True`.

        reader1 = BookLover('Sarah', 'Sarah_Reads@gmail.com', 'horror')

        reader1.add_book('Lord of the Rings', 4)

        test_value = reader1.has_read('Lord of the Rings')

        

        #error message in case test failed

        message = "Test value is not true."

        

        #assertTrue(test_value, message)

        self.assertTrue(test_value, message)



    def test_4_has_read(self): 

        # pass a book NOT in the list and use `assert False` to test the answer is `True`

        reader1 = BookLover('Sarah', 'Sarah_Reads@gmail.com', 'horror')

        reader1.add_book('Lord of the Rings', 4)

        test_value = reader1.has_read('Planet of the Apes')

        

        #error message in case test failed

        message = "Test value is not false"

        

        #assertFalse(test_value, message)

        self.assertFalse(test_value, message)



    def test_5_num_books_read(self): 

        # add some books to the list, and test num_books matches expected.

        reader1 = BookLover('Sarah', 'Sarah_Reads@gmail.com', 'horror')

        reader1.add_book('Lord of the Rings', 4)

        reader1.add_book('Twilight', 2)

        reader1.add_book('Hunger Games', 4)

        reader1.add_book('The Hobbit', 5)

        

        num_books = reader1.num_books_read()

        expected = 4

        

        #error message in case test fails

        message = "num_books does NOT equal expected"

        

        #assertEqual(first_val, second_val, message)

        self.assertEqual(num_books, expected, message)

        



    def test_6_fav_books(self):

        # add some books with ratings to the list, making sure some of them have rating > 3. 

        # Your test should check that the returned books have rating  > 3

        reader1 = BookLover('Sarah', 'Sarah_Reads@gmail.com', 'horror')

        reader1.add_book('Lord of the Rings', 4)

        reader1.add_book('Pride and Prejudice', 2)

        reader1.add_book('The Great Gatsby', 1)

        reader1.add_book('1984', 3)

        reader1.add_book('Don Quixote', 5)

        

        fav_book_list = reader1.fav_books()

        print(fav_book_list)



if __name__ == '__main__':



    unittest.main(verbosity=3)
