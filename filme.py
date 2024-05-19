import sys

from flask import Flask, url_for
from flask import render_template
import app.lib.description as dscr
import app.lib.rating as rate
import app.tests.test_Lotr as tst


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

    
@app.cli.command()
def test():
    """
    Rulare 'unit tests'
    
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    
    """
    import pytest
    sys.exit(pytest.main(["."]))


if __name__ == '__main__':
   app.run(debug=True)
