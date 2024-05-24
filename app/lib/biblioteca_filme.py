def descriere_film():
    descriere = """
    <html>
    <head>
        <title>Descriere</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            header {
                background-color: #333;
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
                background-color: #fff;
                margin: 20px auto;
                width: 80%;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            img {
                max-width: 100%;
                height: auto;
                margin: 20px 0;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Descriere</h1>
        </header>
        <nav>
            <a href="/">Acasă</a>
            <a href="/descriere/Ratatouille">Descriere</a>
            <a href="/recenzii/Ratatouille">Recenzii</a>
        </nav>
        <div class="container">
            <img src="/static/poza1.jpg" alt="Imagine film">
            <p>"Ratatouille" este un film de animație produs de Pixar Animation Studios și lansat de Walt Disney Pictures în 2007. Regizat de Brad Bird, filmul spune povestea unui șobolan pe nume Remy, care visează să devină un mare bucătar, în ciuda condiției sale de rozător și a dezaprobării familiei sale.</p>
            <p>Acțiunea se desfășoară la Paris, unde Remy își găsește drumul către bucătăria unui restaurant de renume, fondat de faimosul bucătar Auguste Gusteau. Acolo, Remy face echipă cu un tânăr și stângaci angajat, Alfredo Linguini. Remy controlează mișcările lui Linguini ascunzându-se sub boneta acestuia și trăgându-l de păr, transformându-l într-un bucătar desăvârșit. Împreună, ei creează feluri de mâncare uimitoare care atrag atenția criticilor culinari, inclusiv a temutului critic Anton Ego.</p>
            <p>"Ratatouille" este un omagiu adus pasiunii pentru gătit și ideii că talentul poate veni de oriunde. Filmul a fost apreciat pentru povestea sa captivantă, animația de înaltă calitate și mesajele sale inspiraționale. A câștigat Premiul Oscar pentru cel mai bun film de animație și a fost nominalizat la alte patru categorii.</p>
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
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }
            header {
                background-color: #333;
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
                background-color: #fff;
                margin: 20px auto;
                width: 80%;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Recenzii</h1>
        </header>
        <nav>
            <a href="/">Acasă</a>
            <a href="/descriere/Ratatouille">Descriere</a>
            <a href="/recenzii/Ratatouille">Recenzii</a>
        </nav>
        <div class="container">
            <ol>
                <p><b> The Holywood Reporter</b>: "Brad Bird and Pixar recapture the charm and winning imagination of classic Disney animation."</p>
                <p><b>Variety</b>: "Ratatouille is delicious. In this satisfying, souffle-light tale of a plucky French rodent with a passion for cooking, the master chefs at Pixar have blended all the right ingredients -- abundant verbal and visual wit, genius slapstick timing, a soupcon of Gallic sophistication -- to produce a warm and irresistible concoction that's sure to appeal to everyone's inner Child."</p>
                <p><b>Chicago Tribune</b>: "Its sense of humor is more sly, more sophisticated and more interesting than most PG-13 or R-rated comedies at the moment. The film may be animated, and largely taken up with rats, but its pulse is gratifyingly human."</p>
                <p><b>New York Times</b>: "A nearly flawless piece of popular art, as well as one of the most persuasive portraits of an artist ever committed to film. It provides the kind of deep, transporting pleasure, at once simple and sophisticated, that movies at their best have always promised."</p>
                <p><b>Wallstreet Journal</b>: "The characters are irresistible -- why would anyone want to resist a hero who so gallantly transcends his rattiness? -- the animation is astonishing and the film, a fantasy version of a foodie rhapsody, sustains a level of joyous invention that hasn't been seen in family entertainment since "The Incredibles.""</p>
            </ol>
        </div>
    </body>
    </html>
    """
    return recenzii