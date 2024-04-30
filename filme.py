from flask import Flask, url_for
from app.lib.biblioteca_fructe import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    ret = "<h1>Filme</h1>"
    
    ret += f"<a href={url_for('V_For_Vendetta')}>V for Vendetta - Rujoiu Alexandru-Valentin</a> <br/>"

    return ret


    
@app.route('/V_For_Vendetta', methods=['GET'])
def .():
	quotes = quotes()
	descriere = descriere_film() 
	
	ret = "<h1>V for Vendetta</h1>"
	
	#Linkuri
	ret += f"<a href={url_for('index')}>[Filme]</a> | "
	ret += f"<a href={url_for('view_quotes_V')}>[quotes]</a> | "
	ret += f"<a href={url_for('view_descriere_V')}>[descriere]</a>"
	
	ret += "<h2>Descriere: </h2>"
	
	ret += descriere 
	
	ret += "<h2>quotes: </h2>"
	ret += quotes
	
	
	
	return ret


@app.route('/V_For_Vendetta/quotes', methods=['GET'])
def view_quotes_V():
    quotes = quotes()  
    
    ret = "<h1>Quotes from V:</h1>"
    ret += f"<a href={url_for('index')}>[Filme]</a> | "
    ret += f"<a href={url_for('V_For_Vendetta')}>[V for Vendetta]</a> <br/> <br/>"
    ret += quotes
    
    return ret

@app.route('/V_For_Vendetta/descriere', methods=['GET'])
def view_descriere_acai():
    descriere = descriere_film()   
    
    ret = "<h1>Descriere V for Vendetta:</h1>"
    ret += f"<a href={url_for('index')}>[Filme]</a> | "
    ret += f"<a href={url_for('V_For_Vendetta')}>[V for Vendetta]</a> <br/> <br/>"
    ret += descriere
    
    return ret
    
    
@app.cli.command()
def test():
    """
    Rulare 'unit tests'
    
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    
    """
    import pytest
    sys.exit(pytest.main(["."]))
    
if __name__ == '__main__':
    app.run(host='127.0.0.1')
