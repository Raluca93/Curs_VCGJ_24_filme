import sys
from flask import Flask, url_for
from app.lib import biblioteca_filme

descriere_matrix = biblioteca_filme.actiune_matrix()
distributie_matrix = biblioteca_filme.distributie_matrix()

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    ret = f"<h1><a href={url_for('matrix')}>Vasile Valentin 441D - Iron Man</a></h1>"
    return ret
    

@app.route("/matrix", methods=['GET'])
def matrix():
  ret = "<h1>Matrix</h1><br>"
  ret += f"<h2><a href={url_for('descriere')}>Descriere</a></h2>"  
  ret += f"<h2><a href={url_for('distributie')}>Distributie</a></h2>"
  return ret  
	
@app.route("/matrix/distributie", methods=["GET"])
def distributie():
  ret = "<h1>Distributie</h1>"
  ret += f"<h2><a href={url_for('matrix')}>Matrix</a></h2> "
  ret += f"<h2><a href={url_for('descriere')}>Descriere</a></h2>"
  ret += distributie_matrix
  return ret
  
@app.route("/matrix/descriere", methods=["GET"])
def descriere():
  ret = "<h1>Descriere</h1>"
  ret += f"<h2><a href={url_for('matrix')}>Matrix</a></h2>"
  ret += f"<h2><a href={url_for('distributie')}>Distributie</a></h2>"
  ret += descriere_matrix
  return ret
  
  
@app.cli.command()
def test():
    """
    Rulare 'unit tests'
    
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    
    """
    import pytest
    sys.exit(pytest.main(["app/tests"]))
    
