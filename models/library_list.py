from models.book_class import Book
import datetime
from datetime import timedelta
book1=Book('Title_1','Author_1','Genre_1',True,datetime.date(2022,10,15))
book2=Book('Title_2','Author_2','Genre_2',False,datetime.date(2022,10,1))
book3=Book('Title_3','Author_3','Genre_3',True,datetime.date(2022,10,10))

book_list=[None,book1,book2,book3]

def add_book(book):
    book_list.append(book)



def delete_book(title):
    for item in book_list[1:]:
        if item.title==title:
            book_to_remove=item

    book_list.remove(book_to_remove)

def change_status(booktitle):
    for item in book_list[1:]:
        if item.title == booktitle:
            loan_time=datetime.timedelta(days=21)
            item.returnby=datetime.date.today()+loan_time
            item.check_out=True