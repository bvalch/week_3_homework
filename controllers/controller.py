from flask import render_template, request, redirect
from app import app
from models.library_list import book_list, add_book, delete_book, change_status
from models.book_class import Book
import datetime
from datetime import date



@app.route('/')
def home():
    return render_template('html_nav/home.html')

@app.route('/book_list/')
def allbooks():
    return render_template('html_nav/book_list.html',list=book_list)

@app.route('/book/<index>')
def book(index):
    book=book_list[int(index)]
    return render_template('html_nav/book.html', book=book)

@app.route('/book_list/new')
def new():
    return render_template('/html_nav/add_book.html')

@app.route('/book_list/', methods=['POST'])
def create():
    title=request.form['title']
    author=request.form['author']
    genre=request.form['genre']
    check_out=False
    returnby=date.today()
    new_book=Book(title,author,genre,check_out,returnby)
    add_book(new_book)
    return redirect('/book_list')

@app.route('/book_list/delete/<title>', methods=['POST'])
def delete(title):
    delete_book(title)
    return redirect("/book_list")

@app.route('/book/checkout/<booktitle>', methods=['POST'])
def checkout(booktitle):
    if request.form:
        change_status(booktitle)

    return redirect ("/book_list")





