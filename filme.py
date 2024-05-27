import sys
from flask import Flask, url_for
from app.lib import biblioteca_filme

actiune_fg = biblioteca_filme.actiune_fg()
distributie_fg = biblioteca_filme.distributie_fg()

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    ret = f"<h1><a href={url_for('fg')}>Ilie Rares 441D - Forrest Gump </a></h1>"
    return ret
    

@app.route("/fg", methods=['GET'])
def fg():
  ret = "<h1>Forrest Gump</h1><br>"
  ret += f"<h2><a href={url_for('actiune')}>Actiune</a></h2>"  
  ret += f"<h2><a href={url_for('distributie')}>Distributie</a></h2>"
  return ret  
	
@app.route("/fg/distributie", methods=["GET"])
def distributie():
  ret = "<h1>Distributie</h1>"
  ret += f"<h2><a href={url_for('fg')}>Forrest Gump</a></h2> "
  ret += f"<h2><a href={url_for('actiune')}>Actiune</a></h2>"
  ret += distributie_fg
  return ret
  
@app.route("/fg/actiune", methods=["GET"])
def actiune():
  ret = "<h1>Actiune</h1>"
  ret += f"<h2><a href={url_for('fg')}>Forrest Gump</a></h2>"
  ret += f"<h2><a href={url_for('distributie')}>Distrinutie</a></h2>"
  ret += actiune_fg
  return ret
  
  
@app.cli.command()
def test():
    import pytest
    sys.exit(pytest.main(["app/tests"])) #Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    
