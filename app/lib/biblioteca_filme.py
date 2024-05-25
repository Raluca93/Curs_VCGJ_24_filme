def descriere_film():
    descriere = """
    <html>
    <head>
        <title>Descriere</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@400;700&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Roboto Slab', serif;
                margin: 0;
                padding: 0;
                background-color: #1c1c1c;
                color: #f0f0f0;
            }
            header {
                background-color: #8b0000;
                color: #f0f0f0;
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
                color: #8b0000;
                font-weight: 700;
                transition: color 0.3s;
            }
            nav a:hover {
                color: #f0f0f0;
            }
            .container {
                padding: 30px;
                background-color: #333;
                margin: 30px auto;
                width: 80%;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                border-radius: 5px;
                text-align: center;
                animation: fade-in 1s;
            }
            img {
                max-width: 100%;
                height: auto;
                margin: 30px 0;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                border-radius: 5px;
            }
            @keyframes fade-in {
                from { opacity: 0; }
                to { opacity: 1; }
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Descriere</h1>
        </header>
        <nav>
            <a href="/">Acasă</a>
            <a href="/descriere/the-lighthouse">Descriere</a>
            <a href="/recenzii/the-lighthouse">Recenzii</a>
        </nav>
        <div class="container">
            <img src="https://m.media-amazon.com/images/M/MV5BZmE0MGJhNmYtOWNjYi00Njc5LWE2YjEtMWMxZTVmODUwMmMxXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_FMjpg_UX1000_.jpg">
            <p>"The Lighthouse" este un film de groază psihologic din 2019, regizat de Robert Eggers. Filmul prezintă povestea a doi faristi care încearcă să mențină sănătatea mintală pe o insulă misterioasă și îndepărtată din New England la sfârșitul secolului al XIX-lea.</p>
            <p>Ephraim Winslow (Robert Pattinson) este un tânăr care se angajează pentru o perioadă de patru săptămâni ca asistent de far sub comanda farului veteran Thomas Wake (Willem Dafoe). Pe măsură ce timpul trece, Winslow devine din ce în ce mai frustrat de sarcinile degradante și de naturul arogant și autoritar al lui Wake. Izolarea, alcoolul și elementele dure încep să ia tribut asupra sănătății lor mentale.</p>
            <p>Pe măsură ce granița dintre realitate și halucinație devine din ce în ce mai neclară, tensiunile dintre cei doi bărbați escaladează, ducând la un conflict intens și violent. Trecutul misterios al lui Winslow și secretele întunecate ale insulei ies la suprafață, adăugând și mai multă complexitate psihologică.</p>
            <p>"The Lighthouse" este un film captivant, care combină elemente de dramă psihologică, groază și umor negru. Imaginea alb-negru evocatoare, performanțele intense ale lui Pattinson și Dafoe și atmosfera claustrofobică creează o experiență cinematografică unică și neliniștitoare.</p>
        </div>
    </body>
    </html>
    """
    return descriere

def recenzii_film():
    recenzii = """
    <html>
    <head>
        <title>Recenzii</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@400;700&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Roboto Slab', serif;
                margin: 0;
                padding: 0;
                background-color: #1c1c1c;
                color: #f0f0f0;
            }
            header {
                background-color: #8b0000;
                color: #f0f0f0;
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
                color: #8b0000;
                font-weight: 700;
                transition: color 0.3s;
            }
            nav a:hover {
                color: #f0f0f0;
            }
            .container {
                padding: 30px;
                background-color: #333;
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
            <h1>Recenzii</h1>
        </header>
        <nav>
            <a href="/">Acasă</a>
            <a href="/descriere/the-lighthouse">Descriere</a>
            <a href="/recenzii/the-lighthouse">Recenzii</a>
        </nav>
        <div class="container">
            <ol>
                <li>
                    <p><strong>The Guardian</strong>: "«The Lighthouse» este un film hipnotic și tulburător, care explorează adâncimile întunecate ale psihicului uman. Performanțele lui Pattinson și Dafoe sunt excepționale, aducând la viață o poveste plină de tensiune și ambiguitate."</p>
                </li>
                <li>
                    <p><strong>The New York Times</strong>: "Robert Eggers a creat o capodoperă vizuală și psihologică cu «The Lighthouse». Imaginile alb-negru evocatoare și atmosfera claustrofobică te atrag într-o lume a nebuniei și a obsesiei."</p>
                </li>
                <li>
                    <p><strong>Variety</strong>: "Un film provocator și enigmatic, «The Lighthouse» te ține captivat de la început până la sfârșit. Pattinson și Dafoe oferă unele dintre cele mai bune performanțe ale carierei lor, aducând la viață o dinamică complexă și neliniștitoare."</p>
                </li>
                <li>
                    <p><strong>The Hollywood Reporter</strong>: "«The Lighthouse» este o experiență cinematografică unică, care combină elemente de groază, umor negru și dramă psihologică. Eggers demonstrează încă o dată măiestria sa în crearea unor lumi imersive și tulburătoare."</p>
                </li>
                <li>
                    <p><strong>Rolling Stone</strong>: "Un tur de forță al actoriei și al cinematografiei, «The Lighthouse» te lasă cu imaginile și temele sale întipărite în minte mult timp după ce creditele se rostogolesc. Un film care merită văzut și discutat."</p>
                </li>
            </ol>
        </div>
    </body>
    </html>
    """
    return recenzii