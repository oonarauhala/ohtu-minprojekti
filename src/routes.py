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

@app.route('/new_blog', methods=["GET", "POST"])
def new_blog():
   if request.method == "GET":
      return render_template("new_blog.html")
   if request.method == "POST":
      nimi = request.form["nimi"]
      kirjoittaja = request.form["kirjoittaja"]
      url = request.form["url"]
      kommentti = request.form["kommentti"]
      if len(nimi.split())==0 or len(kirjoittaja.split())==0 or len(url.split())==0 or len(kommentti.split())==0:
         return render_template("error.html", viesti="Kaikki kentät tulee täyttää")
      komento = "INSERT INTO Blogivinkit (nimi, kirjoittaja, url, kommentti) VALUES (:nimi, :kirjoittaja, :url, :kommentti)"
      con = sql.connect("tietokanta.db")
      con.row_factory = sql.Row
      con.isolation_level = None
      cur = con.cursor()

      try:
         cur.execute(komento, {"nimi":nimi, "kirjoittaja":kirjoittaja, "url":url, "kommentti":kommentti})
         return redirect("/list")
      except:
         return render_template("error.html", viesti="Lisääminen epäonnistui")

@app.route('/new_video', methods=["GET", "POST"])
def new_video():
   if request.method == "GET":
      return render_template("new_video.html")
   if request.method == "POST":
      #koodi tähän
      return render_template("error.html", viesti="Tätä ei ole vielä ohjelmoitu :)")

@app.route('/new_podcast', methods=["GET", "POST"])
def new_podcast():
   if request.method == "GET":
      return render_template("new_podcast.html")
   if request.method == "POST":
      #koodi tähän
      return render_template("error.html", viesti="Tätä ei ole vielä ohjelmoitu :)")


app.run(debug = True)
