import sys
from flask import Flask, url_for
from flask import render_template

import pytest


from app.lib import movie

actiune_the_martian = movie.actiune_the_martian()
distributie_the_martian = movie.distributie_the_martian() 
  



app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():

    ret = f"<h1><a href={url_for('the_martian')}>The Martian</a></h1>"
    return ret


@app.route("/the_martian", methods=['GET'])
def the_martian():
  ret = "<h1>The Martian</h1><br>"
  ret += f"<h2><a href={url_for('actiune')}>Actiune</a></h2>"  
  ret += f"<h2><a href={url_for('distributie')}>Distributie</a></h2>"
  return ret  

@app.route("/the_martian/distributie", methods=["GET"])
def distributie():
  ret = "<h1>Distributie</h1>"
  ret += f"<h2><a href={url_for('the_martian')}>The Martian</a></h2> "
  ret += f"<h2><a href={url_for('actiune')}>Actiune</a></h2>"
  ret += distributie_the_martian
  return ret
  
@app.route("/the_martian/actiune", methods=["GET"])
def actiune():
  ret = "<h1>Actiune</h1>"
  ret += f"<h2><a href={url_for('the_martian')}>The Martian</a></h2>"
  ret += f"<h2><a href={url_for('distributie')}>Distrinutie</a></h2>"
  ret += actiune_the_martian
  return ret	
    
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
   sys.exit(pytest.main(["app/tests"]))
    

