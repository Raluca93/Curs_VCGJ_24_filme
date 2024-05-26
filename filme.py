import sys

from flask import Flask, url_for
from flask import render_template
import app.lib.descriere_film as desc
import app.lib.distributie_film as dist
import app.tests.test_Terminator2 as tst
import pytest

#from app.lib import network
#from app.lib import linux
#from app.grafice.exemplu_func_grad_2 import valori_x, valori_y, genereaza_grafice

print('filme')
print(tst.test_descriere())
print(tst.test_rating())


app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    descriere = desc.returneaza_descriere()
    distributie = dist.returneaza_distributie()
    return render_template("index.html", descriere = descriere, distributie = distributie)

@app.route("/cast")
def cast():
	return render_template("cast.html")
    
@app.route("/reviews")
def reviews():
	return render_template("reviews.html")


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
