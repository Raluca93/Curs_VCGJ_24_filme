import sys

from flask import Flask, url_for
from flask import render_template
import app.lib.description as dscr
import app.lib.rating as rate
import app.tests.test_Lotr as tst
import pytest

import app.lib.funfact_TheHobbit as funfact_TheHobbit
import app.lib.year_TheHobbit as year_TheHobbit

#from app.lib import network
#from app.lib import linux
#from app.grafice.exemplu_func_grad_2 import valori_x, valori_y, genereaza_grafice

print(tst.test_rating())
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    
    return render_template("index.html")

@app.route("/index_Lotr")
def home():
    description = dscr.returneaza_descriere()
    rating = rate.returneaza_rating()
    return render_template("index_Lotr.html", description = description, rating = rating)


@app.route("/cast_Lotr")
def cast():
    return render_template("cast_Lotr.html")

@app.route("/description_Lotr")
def description():
    return render_template("description_Lotr.html")


#The Hobbit - Radu Alexandru-Theodor 441D
@app.route("/index_TheHobbit")
def home_TheHobbit():
    funfact = funfact_TheHobbit.get_random_fun_fact()
    return render_template("index_TheHobbit.html", funfact = funfact)

@app.route("/cast_TheHobbit")
def cast_TheHobbit():
    releaseyear = year_TheHobbit.get_release_year()
    return render_template("cast_TheHobbit.html", releaseyear = releaseyear)

@app.route("/description_TheHobbit")
def description_TheHobbit():
    return render_template("description_TheHobbit.html")
    
@app.cli.command()
def test():
    """
    Rulare 'unit tests'
    
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    
    """

    errno = pytest.main(["-x", "app/tests"])
    sys.exit(errno)
    #sys.exit(pytest.main(["."]))


if __name__ == '__main__':
   app.run(debug=True)
