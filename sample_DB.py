import streamlit as st
import sqlite3

# データベースに接続する
conn = sqlite3.connect('example.db')
c = conn.cursor()

# データを表示する
def show_data():
    c.execute('SELECT * FROM users')
    data = c.fetchall()
    for d in data:
        id, name, age = d
        name = name.replace('\u3000', '　')
        st.write(f'{id}, {name}, {age}')

# データを追加する
def add_data(name, age):
    c.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    st.write('Data added. Please reload page.')

# データベースにテーブルを作成する
c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)')

# データの表示
show_data()

# データの追加
name = st.text_input('Name')
age = st.number_input('Age', step=1)
if st.button('Add data'):
    add_data(name, age)
    # show_data()

# データベースをクローズする
conn.close()