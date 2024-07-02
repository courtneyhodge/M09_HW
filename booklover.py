import pandas as pd



class BookLover():

    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):

        self.name = name

        self.email = email

        self.fav_genre = fav_genre

        self.num_books = num_books              #are optional according to instructions

        self.book_list = book_list             #are optional according to instructions

        

    def add_book(self, book_name, rating): #method 1

        try:

            if book_name not in self.book_list['book_name'].tolist():

                new_book = pd.DataFrame({

                    'book_name': [book_name],

                    'book_rating': [rating]

                })

                self.book_list = pd.concat([self.book_list, new_book], ignore_index = True)

                self.num_books += 1

            else:

                raise AssertionError("Assert: book name already exists") #this part may be wrong

        except AssertionError as e:                                  #this part may be wrong

            print('Except:', e)                                      #this part may be wrong

            

    def has_read(self, book_name): #method 2

        if book_name in self.book_list['book_name'].values:

            return True

        else:

            return False

         

    def num_books_read(self): #method 3

        return self.num_books

    

    def fav_books(self): #method 4

        return self.book_list[self.book_list['book_rating'] > 3]
