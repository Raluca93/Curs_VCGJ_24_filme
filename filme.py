import sys

from flask import Flask, url_for, render_template

#from app.lib import network
#from app.lib import linux
#from app.grafice.exemplu_func_grad_2 import valori_x, valori_y, genereaza_grafice

print('filme')

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/", methods=['GET'])
def index():
    ret = f"<h1><a href={url_for('maze_runner')}>Dobre Octavian 441D - Maze Runner</a></h1>"
    return ret

@app.route("/mazerunner", methods=['GET'])
def maze_runner():
    return render_template('mazerunner.html')

@app.route("/mazerunner/trailer", methods=['GET'])
def maze_runner_trailer():
    return render_template('mazerunner-trailer.html')

@app.route("/mazerunner/description", methods=['GET'])
def maze_runner_description():
    return render_template('mazerunner-description.html')
	
@app.cli.command()
def test():
    """
    Rulare 'unit tests'
    
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    
    """
    #import pytest
    #sys.exit(pytest.main(["."]))
