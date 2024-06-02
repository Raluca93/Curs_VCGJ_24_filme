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
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Roboto', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #1c1c1c;
                color: #f5f5f5;
            }
            header {
                background-color: #8b0000;
                padding: 20px 0;
                text-align: center;
            }
            h1 {
                margin: 0;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 2px;
            }
            nav {
                margin: 30px;
                text-align: center;
            }
            nav a {
                margin: 0 15px;
                text-decoration: none;
                color: #f5f5f5;
                font-weight: 700;
                transition: color 0.3s;
            }
            nav a:hover {
                color: #8b0000;
            }
            .container {
                padding: 30px;
                background-color: #2d2d2d;
                margin: 30px auto;
                width: 80%;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                border-radius: 5px;
                animation: fade-in 1s;
            }
            @keyframes fade-in {
                from { opacity: 0; }
                to { opacity: 1; }
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Film</h1>
        </header>
        <nav>
            <a href="/">Acasă</a>
            <a href="/descriere/fight-club">Descriere</a>
            <a href="/recenzii/fight-club">Recenzii</a>
        </nav>
        <div class="container">
        Pagina Principala a Aplicatiei Web.
        </div>
    </body>
    </html>
    """
    return ret

@app.route("/descriere/fight-club", methods=['GET'])
def get_descriere():
    descriere=biblioteca_filme.descriere_film()
    return descriere

@app.route("/recenzii/fight-club", methods=['GET'])
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
    errno = pytest.main(["-x", "app/test"])
    sys.exit(errno)
    #sys.exit(pytest.main(["."]))

if __name__ == "__main__":

#if __filme__ == "filme_app":
    app.run()
#app.run(host = "127.0.0.1", port = 5001)