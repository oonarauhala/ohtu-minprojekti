# Ohtu miniprojekti

![GitHub Actions](https://github.com/oonarauhala/ohtu-minprojekti/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/oonarauhala/ohtu-minprojekti/branch/master/graph/badge.svg?token=dp9vxjSeY3)](https://codecov.io/gh/oonarauhala/ohtu-minprojekti)

Ohjelma on lukuvinkkisovellus ja on toteutettu ryhmätyönä ohjelmistotuotanto-kurssille.

## Käyttö- ja testausohjeet

Asenna riippuvuudet komennolla

```
poetry install
```

Avaa virtuaaliympäristö komennolla

```
poetry shell
```

Käynnistä ohjelma komennolla

```
python3 src/index.py
```

Avaamalla terminaaliin ilmestynyt linkki ohjelma aukeaa.

Robottestit voidaan ajaa virtuaaliympäristössä komennolla
```
robot src
```

Ja yksikkötestit komennolla
```
pytest src
```

## Dokumentaatio

[Backlog](https://docs.google.com/spreadsheets/d/18ML2sxw8d6rkpPOPR_jcKxy2z214WIsQhWD_ZzRB4dU/edit#gid=1442053365)

## Definition of done

* Product backlog ja sprint backlog ajan tasolla ja kattavat
* User storyt testattu Robot Frameworkilla
* Yksikkötestit ainakin 70% testauskattavuudella
* Kaikki testit menevät läpi ja uusin versio läpäisee CI:n
* Koodityyli on yhtenäistä, arkkitehtuuri järkevää ja koodi on ylläpidettävää: Pylint arvosanalla 9/10
* Käyttökokemus asiakasta miellyttävä
* Asiakas pystyy näkemään koodin ja testien tilanteen CI-palvelusta

## License

[MIT-License](https://github.com/oonarauhala/ohtu-minprojekti/blob/master/LICENSE)



