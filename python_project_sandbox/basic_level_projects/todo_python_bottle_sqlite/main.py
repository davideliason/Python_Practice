#Creae a home page and a page 2 web app

import sqlite3
from bottle import route, run
import mako
#DB
print("Create a TODO list DB")
conn = sqlite3.connect('todo.db')
conn.execute("CREATE TABLE todo (category char(50), theitem char(100),id INTEGER PRIMARY KEY )")
conn.execute("INSERT INTO todo (category, theitem) VALUES ('Shopping','eggs')")
conn.execute("INSERT INTO todo (category, theitem) VALUES ('Shopping','milk')")
conn.execute("INSERT INTO todo (category, theitem) VALUES ('Shopping','bread')")
conn.execute("INSERT INTO todo (category, theitem) VALUES ('Activities','snow tires')")
conn.execute("INSERT INTO todo (category, theitem) VALUES ('Activities','rack lawn')")
conn.commit()
 
print("Database todo.db created")

# define a route for home page
@route('/')
def home_page():
    print("on home page")
    html = """<h1>Home Page</h1>
          <a href='/page2'>Go to Page 2</a>"""
    return html #send HTML to the browser

# now for page 2
@route('/page2')
def page2():
    print("on page 2")
    html = """<h1>Page 2</h1>
           <a href='/'>Go to Home Page</a>"""
    return html

run()
