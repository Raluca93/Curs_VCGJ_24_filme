import sys
from flask import Flask, url_for
from app.lib import biblioteca_filme

actiune_iron_man = biblioteca_filme.actiune_iron_man()
distributie_iron_man = biblioteca_filme.distributie_iron_man()

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    ret = f"<h1><a href={url_for('iron_man')}>Ionescu Raluca 441D - Iron Man</a></h1>"
    return ret
    

@app.route("/iron_man", methods=['GET'])
def iron_man():
  ret = "<h1>Iron Man</h1><br>"
  ret += f"<h2><a href={url_for('actiune')}>Actiune</a></h2>"  
  ret += f"<h2><a href={url_for('distributie')}>Distributie</a></h2>"
  return ret  
	
@app.route("/iron_man/distributie", methods=["GET"])
def distributie():
  ret = "<h1>Distributie</h1>"
  ret += f"<h2><a href={url_for('iron_man')}>Iron Man</a></h2> "
  ret += f"<h2><a href={url_for('actiune')}>Actiune</a></h2>"
  ret += distributie_iron_man
  return ret
  
@app.route("/iron_man/actiune", methods=["GET"])
def actiune():
  ret = "<h1>Actiune</h1>"
  ret += f"<h2><a href={url_for('iron_man')}>Iron Man</a></h2>"
  ret += f"<h2><a href={url_for('distributie')}>Distrinutie</a></h2>"
  ret += actiune_iron_man
  return ret
  
  
@app.cli.command()
def test():
    """
    Rulare 'unit tests'
    
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    
    """
    import pytest
    sys.exit(pytest.main(["app/tests"]))
    
