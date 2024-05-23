import sys
import flask

from lib import biblioteca_filme

print('filme')

__filme__ = "filme_app"
app = flask.Flask(__filme__)

# Parametrii globali pentru descriere si recenzii

@app.route("/", methods=['GET'])
def index():
    ret = """
    <html>
    <head>
        <title>Filme</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            header {
                background-color: #92b9f7;
                color: #fff;
                padding: 10px 0;
                text-align: center;
            }
            
        
            h1 {
                margin: 0;
            }
            nav {
                margin: 20px;
                text-align: center;
            }
            nav a {
                margin: 0 10px;
                text-decoration: none;
                color: #333;
            }
            
           footer {
                position: fixed;
                bottom: 0;
                width: 100%;
                background-color: #92b9f7;
                color: white;
                text-align: center;
                padding: 10px 0;
            }
            
            .container {
                padding: 20px;
                background-color: #fff;
                margin: 20px auto;
                width: 80%;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Film</h1>
        </header>
        <nav>
            <a href="/">Acasă</a>
            <a href="/descriere/die_hard3">Descriere</a>
            <a href="/recenzii/die_hard3">Recenzii</a>
        </nav>
        <div class="container">
        Pagina Principala a Aplicatiei Web.
        </div>
        <footer> Enache Alexandru-Theodor 441D </footer>
    </body>
    </html>
    """
    return ret

@app.route("/descriere/die_hard3", methods=['GET'])
def get_descriere():
    descriere=biblioteca_filme.descriere_film()
    return descriere

@app.route("/recenzii/die_hard3", methods=['GET'])
def get_recenzii():
    recenzii=biblioteca_filme.recenzii_film()
    return recenzii

@app.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    """
    import pytest
    errno = pytest.main(["-x", "app/tests"])
    sys.exit(errno)
    #sys.exit(pytest.main(["."]))

if __filme__ == "filme_app":
    app.run()
