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
                background-color: #52e7f2;
            }
            header {
                background-color: #89e9f0;
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
            .container {
                padding: 20px;
                background-color: #abd1ed;
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
            <a href="/descriere/Ed_Edd_n_Eddys_Big_Picture_Show">Descriere</a>
            <a href="/recenzii/Ed_Edd_n_Eddys_Big_Picture_Show">Recenzii</a>
        </nav>
        <div class="container">
        Pagina dedicata filmului "Ed, Edd, n Eddy's Big Picture Show".
        </div>
    </body>
    </html>
    """
    return ret

@app.route("/descriere/Ed_Edd_n_Eddys_Big_Picture_Show", methods=['GET'])
def get_descriere():
    descriere=biblioteca_filme.descriere_film()
    return descriere

@app.route("/recenzii/Ed_Edd_n_Eddys_Big_Picture_Show", methods=['GET'])
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
