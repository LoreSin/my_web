from flask import Flask, render_template, redirect, request
import sqlite3
'''
import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.0.220",
  user="hkit",
  passwd="hkit1234",
  database="my"
)
'''


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_memos')
def get_memos():
    mydb = sqlite3.connect("my.db")
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM memo')
    memos = cursor.fetchall()

    result = {
        'memos': memos
    }
    return render_template('get_memos.html', result=result)


@app.route('/add_memo')
def add_memo():
    return render_template('add_memo.html')


@app.route('/act_add_memo')
def act_add_memo():
    content = request.args.get('content')

    mydb = sqlite3.connect("my.db")
    cursor = mydb.cursor()
    cursor.execute('INSERT INTO memo (content) VALUES (?)', (content,))
    mydb.commit()
    memos = cursor.fetchall()
    return redirect('get_memos')


if __name__ == '__main__':
    app.run()
