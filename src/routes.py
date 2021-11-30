from app import app
#from db import db
import sqlite3 as sql
from flask import Flask, render_template, request, redirect

@app.route('/list')
def list():
   con = sql.connect("tietokanta.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from Vinkit")
   
   rows = cur.fetchall()
   return render_template("list.html",rows = rows)

@app.route("/")
def index():
   return render_template("index.html")


@app.route('/new')
def new():
   return render_template("new.html")


@app.route('/create', methods=["POST"])
def create():
   vinkki = request.form["otsikko"]
   if len(vinkki.split())==0:
      return render_template("error.html", viesti="Tyhjää lukuvinkkiä ei voi lähettää")
   komento = "INSERT INTO Vinkit (Otsikko) VALUES (:vinkki)"
   con = sql.connect("tietokanta.db")
   con.row_factory = sql.Row
   con.isolation_level = None
   cur = con.cursor()

   try:
      cur.execute(komento, {"vinkki":vinkki})
      return redirect("/list")
   except:
      return render_template("error.html", viesti="Lisääminen epäonnistui")

app.run(debug = True)
