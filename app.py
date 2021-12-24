from flask import Flask
from flask import render_template, redirect, url_for, flash
from flask import request
from database import *

app = Flask(__name__)

@app.route('/')
def index():
  return redirect(url_for('home'))

@app.route('/reset')
def reset():
  init_db()
  return redirect(url_for('home'))

@app.route('/home', methods=['GET', 'POST'])
def home():
  if request.method == 'GET':
    conn = sqlite3.connect(database='./db/book.db')
    cursor = conn.cursor()
    cursor.execute("select * from book order by book_id")
    books = cursor.fetchall()
    cursor.close()
    return render_template('home.html', books=books)

  elif request.method == 'POST':
    if request.form['action'] == '查询':
      book_id = request.form['book_id']
      book_name = request.form['book_name']
      book_isbn = request.form['book_isbn']
      book_author = request.form['book_author']
      book_publisher = request.form['book_publisher']
      book_price = request.form['book_price']
      interview_times = request.form['interview_times']

      conn = sqlite3.connect(database='./db/book.db')
      cursor = conn.cursor()
      query_sql = "select * from book"
      book_id_cond = "book_id = '{}'".format(book_id) if book_id != '' else 'true'
      book_name_cond = "book_name = '{}'".format(book_name) if book_name != '' else 'true'
      book_isbn_cond = "book_isbn = '{}'".format(book_isbn) if book_isbn != '' else 'true'
      book_author_cond = "book_author = '{}'".format(book_author) if book_author != '' else 'true'
      book_publisher_cond = "book_publisher = '{}'".format(book_publisher) if book_publisher != '' else 'true'
      book_price_cond = "book_price = {}".format(book_price) if book_price != '' else 'true'
      interview_times_cond = "interview_times = {}".format(interview_times) if interview_times != '' else 'true'
      cond = ' where ' + book_id_cond + \
             ' and ' + book_name_cond + \
             ' and ' + book_isbn_cond + \
             ' and ' + book_author_cond + \
             ' and ' + book_publisher_cond + \
             ' and ' + book_price_cond + \
             ' and ' + interview_times_cond
      query_sql += cond
      query_sql += ' order by book_id'
      cursor.execute(query_sql)
      books = cursor.fetchall()
      cursor.close()
      return render_template('home.html', books=books)

    elif request.form['action'] == '添加':
      book_id = request.form['book_id']
      book_name = request.form['book_name']
      book_isbn = request.form['book_isbn']
      book_author = request.form['book_author']
      book_publisher = request.form['book_publisher']
      book_price = request.form['book_price']
      interview_times = request.form['interview_times']

      conn = sqlite3.connect(database='./db/book.db')
      cursor = conn.cursor()
      try:
        insert_sql = "insert into book (book_id, book_name, book_isbn, book_author, book_publisher, book_price, interview_times) \
                      values ('{}', '{}', '{}', '{}', '{}', {}, {})" \
                      .format(book_id, book_name, book_isbn, book_author, book_publisher, book_price, interview_times)
        cursor.execute(insert_sql)
      except:
        return redirect(url_for('home'))
      conn.commit()
      cursor.close()
      return redirect(url_for('home'))

@app.route('/edit/<book_id>', methods=['GET', 'POST'])
def edit(book_id):
  conn = sqlite3.connect(database='./db/book.db')
  cursor = conn.cursor()

  if request.method == 'POST':
    book_name = request.form['book_name']
    book_isbn = request.form['book_isbn']
    book_author = request.form['book_author']
    book_publisher = request.form['book_publisher']
    book_price = request.form['book_price']
    interview_times = request.form['interview_times']

    conn = sqlite3.connect(database='./db/book.db')
    cursor = conn.cursor()
    update_sql = "update book set " + \
                "book_name = '{}', ".format(book_name) + \
                "book_isbn = '{}', ".format(book_isbn) + \
                "book_author = '{}', ".format(book_author) + \
                "book_publisher = '{}', ".format(book_publisher) + \
                "book_price = {}, ".format(book_price) + \
                "interview_times = {} ".format(interview_times) + \
                "where book_id = '{}'".format(book_id)
    cursor.execute(update_sql)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('home'))

  cursor.execute("select * from book where book_id = '{}'".format(book_id))
  book = cursor.fetchone()
  cursor.close()
  conn.close()
  return render_template('edit.html', book=book)

@app.route('/delete/<book_id>', methods=['GET', 'POST'])
def delete(book_id):
  conn = sqlite3.connect(database='./db/book.db')
  cursor = conn.cursor()

  if request.method == 'POST':
    delete_sql = "delete from book where book_id = '{}'".format(book_id)
    cursor.execute(delete_sql)      
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('home'))

  cursor.execute("select * from book where book_id = '{}'".format(book_id))
  book = cursor.fetchone()
  cursor.close()
  conn.close()
  return render_template('delete.html', book=book)

if __name__ == "__main__":
  app.run(host='127.0.0.1', port=5000, debug=True)
