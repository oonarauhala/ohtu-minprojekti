from app import app
import sqlite3 as sql
from flask import Flask, render_template, request, redirect
import db_functions

@app.route('/list')
def list():
   rows = db_functions.get_kirjavinkit()
   return render_template("list.html",rows = rows)

@app.route("/")
def index():
   return render_template("index.html")

@app.route('/new_book', methods=["GET", "POST"])
def new_book():
   if request.method == "GET":
      return render_template("new.html")
   if request.method == "POST":
      otsikko = request.form["otsikko"]
      kirjoittaja = request.form["kirjoittaja"]
      isbn = request.form["isbn"]
      kommentti = request.form["kommentti"]
      if len(otsikko.split())==0 or len(kirjoittaja.split())==0 or len(isbn.split())==0 or len(kommentti.split())==0:
         return render_template("error.html", viesti="Kaikki kentät tulee täyttää")
      if db_functions.new_kirjavinkki(otsikko, kirjoittaja, isbn, kommentti):
         return redirect("/list")
      else:
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

      if db_functions.new_blogivinkki(nimi, kirjoittaja, url, kommentti):
         return redirect("/list")
      else:
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
