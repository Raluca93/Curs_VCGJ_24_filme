def descriere_film():
    descriere = """
    <html>
    <head>
        <title>Descriere</title>
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
                text-align: center;
                animation: slide-in 1s;
            }
            img {
                max-width: 100%;
                height: auto;
                margin: 30px 0;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                border-radius: 5px;
            }
            @keyframes slide-in {
                from { transform: translateX(-100%); }
                to { transform: translateX(0); }
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Descriere</h1>
        </header>
        <nav>
            <a href="/">Acasă</a>
            <a href="/descriere/fight-club">Descriere</a>
            <a href="/recenzii/fight-club">Recenzii</a>
        </nav>
        <div class="container">
            <img src="https://m.media-amazon.com/images/M/MV5BMmEzNTkxYjQtZTc0MC00YTVjLTg5ZTEtZWMwOWVlYzY0NWIwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg">
            <p>"Fight Club" este un film dramatic și satiric din 1999, regizat de David Fincher, cu Edward Norton și Brad Pitt în rolurile principale. Filmul explorează teme precum consumismul, masculinitatea și alienarea socială.</p>
            <p>Naratorul anonim (Edward Norton) este un funcționar corporatist plictisit și nemulțumit de viața sa. Într-o călătorie de afaceri, îl întâlnește pe Tyler Durden (Brad Pitt), un producător de săpun carismatic și nonconformist. După ce apartamentul naratorului este distrus într-o explozie misterioasă, acesta se mută cu Tyler, iar cei doi formează un "fight club" clandestin, unde bărbații se luptă pentru a scăpa de frustrările vieții moderne.</p>
            <p>Pe măsură ce fight club-ul câștigă popularitate, Tyler începe să creeze un cult anarhist cunoscut sub numele de Project Mayhem, cu scopul de a distruge simbolurile consumismului și de a provoca haos în societate. Naratorul începe să-și pună la îndoială relația cu Tyler și propria sa identitate, descoperind un adevăr tulburător.</p>
            <p>"Fight Club" este o critică incisivă a conformismului și a valorilor materialiste ale societății moderne, explorând impactul psihologic al alienării și al lipsei de sens. Filmul se remarcă prin regia inovatoare a lui David Fincher, performanțele puternice ale lui Edward Norton și Brad Pitt, precum și prin răsturnările de situație șocante din poveste.</p>
            <p>Cu un amestec de umor negru, violență și comentarii sociale, "Fight Club" a devenit un film cult, stârnind controverse și discuții aprinse de la lansarea sa. Filmul rămâne o operă provocatoare și memorabilă, care continuă să captiveze și să inspire publicul.</p>
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
                animation: slide-in 1s;
            }
            @keyframes slide-in {
                from { transform: translateX(100%); }
                to { transform: translateX(0); }
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Recenzii</h1>
        </header>
        <nav>
            <a href="/">Acasă</a>
            <a href="/descriere/fight-club">Descriere</a>
            <a href="/recenzii/fight-club">Recenzii</a>
        </nav>
        <div class="container">
            <ol>
                <li>
                    <p><strong>The New York Times</strong>: "«Fight Club» este un film provocator și captivant, care explorează cu îndrăzneală teme precum masculinitatea toxică, consumismul și alienarea socială. Regia lui David Fincher este impecabilă, iar performanțele lui Edward Norton și Brad Pitt sunt remarcabile."</p>
                </li>
                <li>
                    <p><strong>Rolling Stone</strong>: "Un film cult instantaneu, «Fight Club» combină umorul negru, violența și comentariul social într-un amestec exploziv. Fincher creează o lume vizual uimitoare, în timp ce scenariul inteligent abordează subiecte complexe cu o claritate brutală."</p>
                </li>
                <li>
                    <p><strong>The Guardian</strong>: "«Fight Club» este o satiră îndrăzneață și provocatoare a societății moderne, care pune sub semnul întrebării noțiunile de identitate, consum și conformism. Filmul rămâne la fel de relevant și de șocant astăzi ca și la lansarea sa inițială."</p>
                </li>
                <li>
                    <p><strong>Chicago Sun-Times</strong>: "Cu o distribuție puternică și o regie inventivă, «Fight Club» este un film care te face să gândești și care nu te lasă indiferent. Deși controversat, filmul reușește să abordeze teme profunde într-un mod unic și memorabil."</p>
                </li>
                <li>
                    <p><strong>Entertainment Weekly</strong>: "«Fight Club» este un film îndrăzneț și iconoclast, care sfidează convențiile și așteptările. Cu un ritm alert, răsturnări de situație șocante și imagini vizuale impresionante, filmul lui Fincher lasă o impresie de durată asupra publicului."</p>
                </li>
            </ol>
        </div>
    </body>
    </html>
    """
    return recenzii