import sys
from flask import Flask, url_for, render_template

print('filme')
app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['TESTING'] = True

@app.route("/", methods=['GET'])
def index():
    ret = f"<h1><a href={url_for('maze_runner')}>Dobre Octavian 441D - Maze Runner</a></h1>"
    return ret

@app.route("/mazerunner", methods=['GET'])
def maze_runner():
    return render_template('/Octavian/mazerunner.html')

@app.route("/mazerunner/trailer", methods=['GET'])
def maze_runner_trailer():
    return render_template('/Octavian/mazerunner-trailer.html')

@app.route("/mazerunner/description", methods=['GET'])
def maze_runner_description():
    return render_template('/Octavian/mazerunner-description.html')
