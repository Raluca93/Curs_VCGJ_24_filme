import sys
from flask import Flask, url_for
from app.lib import biblioteca_filme

actiune_barbie = biblioteca_filme.actiune_barbie()
distributie_barbie = biblioteca_filme.distributie_barbie()

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    ret = f"<h1><a href={url_for('barbie')}>Marcu Alexandra 441D - Barbie</a></h1>"
    return ret
    

@app.route("/barbie", methods=['GET'])
def barbie():
  ret = "<h1>Barbie</h1><br>"
  ret += f"<h2><a href={url_for('actiune')}>Actiune</a></h2>"  
  ret += f"<h2><a href={url_for('distributie')}>Distributie</a></h2>"
  return ret  
	
@app.route("/barbie/distributie", methods=["GET"])
def distributie():
  ret = "<h1>Distributie</h1>"
  ret += f"<h2><a href={url_for('barbie')}>Barbie</a></h2> "
  ret += f"<h2><a href={url_for('actiune')}>Actiune</a></h2>"
  ret += distributie_barbie
  return ret
  
@app.route("/barbie/actiune", methods=["GET"])
def actiune():
  ret = "<h1>Actiune</h1>"
  ret += f"<h2><a href={url_for('barbie')}>Barbie</a></h2>"
  ret += f"<h2><a href={url_for('distributie')}>Distrinutie</a></h2>"
  ret += actiune_barbie
  return ret
  
  
@app.cli.command()
def test():
    """
    Rulare 'unit tests'
    
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    
    """
    import pytest
    sys.exit(pytest.main(["."]))
