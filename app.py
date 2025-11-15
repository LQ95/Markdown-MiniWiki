'''
Progetto MINI WIKI

Crea una piccola wiki scritta in markdown usando un parser JS

Pagine editabili, e cancellabili, con tanto di cronologia

Possibili utenti multipli
'''
#TODO: cambia il database a un database che usa Postgres
#TODO: carica tutto su una immagine Docker
#TODO: login e registrazione utenti, con hasing delle password

from __future__ import annotations
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3, os, time
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key-change-this-in-production"

DB_PATH = os.path.join(os.path.dirname(__file__), "app.db")

def get_db():
    conn = sqlite3.connect(DB_PATH,check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as db:
        db.execute("""
        CREATE TABLE IF NOT EXISTS pages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL UNIQUE,
            body TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
        """)
        #not implemented yet
        db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,email TEXT NOT NULL, Sysop INTEGER NOT NULL);")
        db.execute("CREATE TABLE IF NOT EXISTS edits (id INTEGER PRIMARY KEY AUTOINCREMENT,page_id INTEGER NOT NULL,type TEXT NOT NULL,timestamp TEXT NOT NULL);")

def populate(db):
    pass

with app.app_context():
    init_db()
    #popolamento
    with get_db() as db:
        db.execute("INSERT OR IGNORE INTO pages (title,body,created_at) VALUES (?,?,?)",
                   ("test","This is a test page",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
        row = db.execute("SELECT * FROM pages WHERE title=\"test\"").fetchone()
        test_page_id=row['id']
        db.execute("INSERT INTO edits(page_id,type,timestamp) SELECT ?,?,? WHERE NOT EXISTS(SELECT 1 FROM edits WHERE page_id=?)",
                   (test_page_id,"creation",time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), test_page_id))



def add_user(username,password,email,is_sysop):
    with get_db() as db:
        db.execute("INSERT OR REPLACE INTO users (name,password,email) VALUES (?,?,?)",
                   (username,password,email))

def add_page(name,content):
    timestamp=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    with get_db() as db:
        db.execute("INSERT OR REPLACE INTO pages (title,body,created_at) VALUES (?,?,?)",
                   (name,content,timestamp))


def add_edit(page_id,type):
    timestamp=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    with get_db() as db:
        db.execute("INSERT OR IGNORE INTO edits (page_id,type,timestamp) VALUES (?,?,?)",(page_id,type,timestamp))

#routing
@app.route('/')
def main():
    return redirect(url_for('main_page'))

@app.get("/login")
def login():
    return render_template("login.html")

@app.get("/signup")
def login():
    return render_template("signup.html")

@app.get("/user/<username>")
def login(username):
    return render_template("userpage.html",username=username)

@app.route('/index')
def index():
    return redirect(url_for('main_page'))

@app.route('/wiki')
def wiki():
    return redirect(url_for('main_page'))

@app.route("/wiki/Main_Page",methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':    
        title=request.form['search']
        return redirect(url_for("read_page",pagename=title))
    else: 
        pages=db.execute("SELECT * FROM pages").fetchall()
        return render_template('index.html',pages=pages)


@app.route("/wiki/<pagename>")
def read_page(pagename):
    with get_db() as db:
        row = db.execute("SELECT * FROM pages WHERE title=?", (pagename,)).fetchone()
    if not row:
        db.close()
        return redirect(url_for("create_page",pagename=pagename))
    pagecontent=row['body']
    return render_template('page.html',content=pagecontent,title=pagename)

@app.route("/edit/<pagename>",methods=['GET', 'POST'])
def edit_page(pagename):
    with get_db() as db:
        row = db.execute("SELECT * FROM pages WHERE title=?", (pagename,)).fetchone()
    if not row:
        return redirect(url_for("create_page",pagename=pagename))
    if request.method == 'POST':    
        newcontent=request.form['content']
        page_id=row['id']
        with get_db() as db:
            db.execute("UPDATE pages SET body=? WHERE id=?",(newcontent,page_id))
            add_edit(page_id,"edit")
        return redirect(url_for("read_page",pagename=pagename))
    pagecontent=row['body']
    return render_template('page_edit.html',content=pagecontent,title=pagename)

@app.route("/create/<pagename>",methods=['GET', 'POST'])
def create_page(pagename,):
    with get_db() as db:
        row = db.execute("SELECT * FROM pages WHERE title=?", (pagename,)).fetchone()
    if row:
        return redirect(url_for("edit_page",pagename=pagename))
    if request.method == 'POST':    
        content=request.form['content']
        with get_db() as db:
            db.execute("INSERT OR REPLACE INTO pages (title,body,created_at) VALUES (?,?,?)",
                   (pagename,content,time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) ))
            row = db.execute("SELECT * FROM pages WHERE title=?", (pagename,)).fetchone()
            page_id=row['id']
            add_edit(page_id,"creation")
        return redirect(url_for("read_page",pagename=pagename))
    else: return render_template('page_create.html',title=pagename) 
     
@app.route("/delete/<pagename>")
def delete_page(pagename):
    with get_db() as db:
        row = db.execute("SELECT * FROM pages WHERE title=?", (pagename,)).fetchone()
        if not row:
            flash("attempting to delete non-existing page.")
            return redirect(url_for("index"))
        else:
            page_id=row['id']
            row= db.execute("DELETE FROM edits WHERE page_id=?", ((str(page_id)),))
            row = db.execute("DELETE FROM pages WHERE title=?", (pagename,)).fetchone()
            flash("page successfully deleted.")
            return redirect(url_for("index"))

@app.route("/wiki/<pagename>/chron")
def page_chron(pagename):
    with get_db() as db:
        row = db.execute("SELECT * FROM pages WHERE title=?", (pagename,)).fetchone()
    if not row:
        return redirect(url_for("index"))
    else:
        page_id=row['id']
        edits= db.execute("SELECT * FROM edits WHERE page_id=?", ((str(page_id)),) ).fetchall()
        return render_template("page_chronology.html",edits=edits,title=pagename)

if __name__=="__main__":
    app.run(debug=True)