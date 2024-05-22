import sys

from flask import Flask, url_for
from flask import render_template
import app.lib.description as dscr
import app.lib.description_Dune as dscr_Dune
import app.lib.rating as rate
import app.lib.rating_Dune as rate_Dune
import app.tests.test_Lotr as tst
import app.tests.test_Dune as tst_Dune
import pytest

#from app.lib import network
#from app.lib import linux
#from app.grafice.exemplu_func_grad_2 import valori_x, valori_y, genereaza_grafice

print(tst.test_rating())
print(tst_Dune.test_rating_Dune())
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

@app.route("/index_Dune")
def index_Dune():
    description_Dune = dscr_Dune.returneaza_descriere()
    rating_Dune = rate_Dune.returneaza_rating()
    return render_template("index_Dune.html", description_D = description_Dune, rating_D = rating_Dune)

@app.route("/description_Dune")
def description_Dune():
    return render_template("description_Dune.html")

@app.route("/cast_Dune")
def cast_Dune():
    return render_template("cast_Dune.html")
    
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
