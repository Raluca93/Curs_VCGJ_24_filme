from flask import Flask , url_for
from app.lib import lib_filme as filme

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    ret = "<h1>Filme</h1>"
    
    ret += f"<a href={url_for('One_Piece_RED')}>One Piece RED - Toader Florin</a> <br/>"

    return ret


    
@app.route('/One_Piece_RED', methods=['GET'])
def One_Piece_RED():
	comentari = filme.comentari()
	descriere = filme.descriere_film() 
	
	ret = "<h1>One Piece RED</h1>"
	
	#Linkuri
	ret += f"<a href={url_for('index')}>[Filme]</a> | "
	ret += f"<a href={url_for('view_comentari')}>[comentari]</a> | "
	ret += f"<a href={url_for('view_descriere')}>[descriere]</a>"
	
	ret += "<h2>Descriere: </h2>"
	
	ret += descriere 
	
	ret += "<h2>comentari: </h2>"
	ret += comentari
	
	
	
	return ret


@app.route('/One_Piece_RED/comentari', methods=['GET'])
def view_comentari():
    comentari =filme.comentari()  
    
    ret = "<h1>comentari:</h1>"
    ret += f"<a href={url_for('index')}>[Filme]</a> | "
    ret += f"<a href={url_for('One_Piece_RED')}>[One Piece RED]</a> <br/> <br/>"
    ret += comentari
    
    return ret

@app.route('/One_Piece_RED/descriere', methods=['GET'])
def view_descriere():
    descriere =filme.descriere_film()   
    
    ret = "<h1>Descriere One Piece RED:</h1>"
    ret += f"<a href={url_for('index')}>[Filme]</a> | "
    ret += f"<a href={url_for('One_Piece_RED')}>[One Piece RED]</a> <br/> <br/>"
    ret += descriere
    
    return ret
    
    
@app.cli.command()
def test():
    """
    Rulare 'unit tests'
    
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    
    """
    import pytest
    sys.exit(pytest.main(["-x","app/test"]))
    
if __name__ == '__main__':
    app.run(host='127.0.0.1')
