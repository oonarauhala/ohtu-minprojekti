from app import app
#from db import db
import sqlite3 as sql
from flask import Flask, render_template, request, redirect

@app.route('/list')
def list():
   con = sql.connect("tietokanta.db")
   con.row_factory = sql.Row

   cur = con.cursor()
   cur.execute("select * from Kirjavinkit")

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
   otsikko = request.form["otsikko"]
   kirjoittaja = request.form["kirjoittaja"]
   isbn = request.form["isbn"]
   kommentti = request.form["kommentti"]
   if len(otsikko.split())==0 or len(kirjoittaja.split())==0 or len(isbn.split())==0 or len(kommentti.split())==0:
      return render_template("error.html", viesti="Kaikki kentät tulee täyttää")
   komento = "INSERT INTO Kirjavinkit (Otsikko, kirjoittaja, isbn, kommentti) VALUES (:otsikko, :kirjoittaja, :isbn, :kommentti)"
   con = sql.connect("tietokanta.db")
   con.row_factory = sql.Row
   con.isolation_level = None
   cur = con.cursor()

   try:
      cur.execute(komento, {"otsikko":otsikko, "kirjoittaja":kirjoittaja, "isbn":isbn, "kommentti":kommentti})
      return redirect("/list")
   except:
      return render_template("error.html", viesti="Lisääminen epäonnistui")

app.run(debug = True)
