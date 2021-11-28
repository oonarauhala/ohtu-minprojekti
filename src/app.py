from flask import Flask, render_template
import sqlite3 as sql


app = Flask(__name__,template_folder='templates')

@app.route('/list')
def list():
   con = sql.connect("tietokanta.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from Vinkit")
   
   rows = cur.fetchall(); 
   return render_template("list.html",rows = rows)

   

@app.route("/")
def index():
   return render_template("index.html")

app.run(debug = True)