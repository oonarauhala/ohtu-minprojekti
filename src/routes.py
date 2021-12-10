from flask import render_template, request, redirect
from app import app
from db_functions import DBFunctions
from werkzeug.security import check_password_hash, generate_password_hash

db_functions = DBFunctions()

def check_no_empty_fields(*fields):
    """
    Checks if any of the provided fields are empty
    
    Returns: True if any of the fields is empty
    """
    return not all(fields)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/list")
def list_function():
    kirjarows = db_functions.get_kirjavinkit()
    blogirows = db_functions.get_blogivinkit()
    podrows = db_functions.get_podcastvinkit()
    vidrows = db_functions.get_videovinkit()
    return render_template(
        "list.html",
        kirjarows=kirjarows,
        blogirows=blogirows,
        podrows=podrows,
        vidrows=vidrows,
    )


@app.route("/new_book", methods=["GET", "POST"])
def new_book():
    if request.method == "GET":
        return render_template("new.html")
    if request.method == "POST":
        otsikko = request.form["otsikko"]
        kirjoittaja = request.form["kirjoittaja"]
        isbn = request.form["isbn"]
        kommentti = request.form["kommentti"]
        if check_no_empty_fields(otsikko, kirjoittaja, isbn, kommentti):
            return render_template("error.html", viesti="Kaikki kentät tulee täyttää")

        if db_functions.new_kirjavinkki(otsikko, kirjoittaja, isbn, kommentti):
            return redirect("/list")

        return render_template("error.html", viesti="Lisääminen epäonnistui")


@app.route("/new_blog", methods=["GET", "POST"])
def new_blog():
    if request.method == "GET":
        return render_template("new_blog.html")
    if request.method == "POST":
        nimi = request.form["nimi"]
        kirjoittaja = request.form["kirjoittaja"]
        url = request.form["url"]
        kommentti = request.form["kommentti"]
        if check_no_empty_fields(nimi, kirjoittaja, url, kommentti):
            return render_template("error.html", viesti="Kaikki kentät tulee täyttää")

        if db_functions.new_blogivinkki(nimi, kirjoittaja, url, kommentti):
            return redirect("/list")

        return render_template("error.html", viesti="Lisääminen epäonnistui")


@app.route("/new_podcast", methods=["GET", "POST"])
def new_podcast():
    if request.method == "GET":
        return render_template("new_podcast.html")
    if request.method == "POST":
        nimi = request.form["nimi"]
        tekija = request.form["tekija"]
        jakson_nimi = request.form["jakson_nimi"]
        kommentti = request.form["kommentti"]
        if check_no_empty_fields(nimi, tekija, jakson_nimi, kommentti):
            return render_template("error.html", viesti="Kaikki kentät tulee täyttää")

        if db_functions.new_podcastvinkki(nimi, tekija, jakson_nimi, kommentti):
            return redirect("/list")

        return render_template("error.html", viesti="Lisääminen epäonnistui")


@app.route("/new_video", methods=["GET", "POST"])
def new_video():
    if request.method == "GET":
        return render_template("new_video.html")
    if request.method == "POST":
        nimi = request.form["nimi"]
        tekija = request.form["tekija"]
        url = request.form["url"]
        kommentti = request.form["kommentti"]
        if check_no_empty_fields(nimi, tekija, url, kommentti):
            return render_template("error.html", viesti="Kaikki kentät tulee täyttää")

        if db_functions.new_videovinkki(nimi, tekija, url, kommentti):
            return redirect("/list")

        return render_template("error.html", viesti="Lisääminen epäonnistui")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        tunnus = request.form["tunnus"]
        salasana = request.form["salasana"]
        salasana_uudelleen = request.form["salasana_uudelleen"]
        if len(tunnus) < 5 or len(tunnus.split()) == 0:
            return render_template("error.html", viesti="Anna käyttjätunnus, joka on vähintään 5 merkkiä pitkä")
        if len(salasana) < 8 or len(salasana.split()) == 0:
            return render_template("error.html", viesti="Anna salasana, joka on vähintään 8 merkkiä pitkä")
        if salasana != salasana_uudelleen:
            return render_template("error.html", viesti="Antamasi salasanat eivät täsmää")
        hash_arvo = generate_password_hash(salasana)
        if db_functions.uusi_kayttaja(tunnus, hash_arvo):
            return redirect("/")
        else:
            return render_template("error.html", viesti="Antamasi käyttäjätunnus on jo käytössä")

@app.route("/mark_read")
def mark_read():
    id_field = request.args.get("id")
    category = request.args.get("category")
    if category == "book":
        if db_functions.merkitse_kirja_luetuksi(id_field):
            return redirect("/list")
        return render_template("/error.html", viesti="Luetuksi merkitseminen epäonnistui")
    elif category == "blog":
        if db_functions.merkitse_blogi_luetuksi(id_field):
            return redirect("/list")
        return render_template("/error.html", viesti="Luetuksi merkitseminen epäonnistui")
    elif category == "podcast":
        if db_functions.merkitse_podcast_kuunnelluksi(id_field):
            return redirect("/list")
        return render_template("/error.html", viesti="Luetuksi merkitseminen epäonnistui")
    elif category == "video":
        if db_functions.merkitse_video_katsotuksi(id_field):
            return redirect("/list")
        return render_template("/error.html", viesti="Luetuksi merkitseminen epäonnistui")
    else:
        return render_template("/error.html", viesti="Luetuksi merkitseminen epäonnistui")
