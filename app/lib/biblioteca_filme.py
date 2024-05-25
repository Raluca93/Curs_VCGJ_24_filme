def descriere_film():
    descriere = """
    <html>
    <head>
        <title>Descriere</title>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Montserrat', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f8f9fa;
            }
            header {
                background-color: #007bff;
                color: #fff;
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
                color: #007bff;
                font-weight: 700;
                transition: color 0.3s;
            }
            nav a:hover {
                color: #0056b3;
            }
            .container {
                padding: 30px;
                background-color: #fff;
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
            <a href="/descriere/inception">Descriere</a>
            <a href="/recenzii/inception">Recenzii</a>
        </nav>
        <div class="container">
            <img src="https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_.jpg">
            <p>"Inception" este un film de acțiune științifico-fantastic din 2010, scris și regizat de Christopher Nolan. Filmul explorează conceptul de împărtășire a viselor și implică o echipă de spioni specializați în furtul de secrete corporative prin infiltrarea în subconștientul țintelor lor.</p>
            <p>Leonardo DiCaprio joacă rolul lui Dom Cobb, un "extractor" expert care are abilitatea de a intra în visele altora pentru a obține informații valoroase. Cobb primește o ultimă misiune dificilă: în loc să fure un secret, el trebuie să planteze o idee în mintea unei persoane. Această tehnică, cunoscută sub numele de "inception", este considerată imposibilă.</p>
            <p>Pentru a-și îndeplini misiunea, Cobb adună o echipă de specialiști: Eames (Tom Hardy), un maestru al deghizării; Yusuf (Dileep Rao), un expert în sedative; Ariadne (Ellen Page), un arhitect de vise; și Arthur (Joseph Gordon-Levitt), partenerul de lungă durată al lui Cobb. Împreună, ei se aventurează în lumea complexă și periculoasă a viselor partajate, confruntându-se cu propriile lor secrete și regrete.</p>
            <p>Pe parcursul misiunii, granițele dintre vis și realitate devin din ce în ce mai neclare, punând la încercare atât echipa, cât și pe Cobb însuși, care se luptă cu amintirea tragică a soției sale decedate, Mal (Marion Cotillard).</p>
            <p>"Inception" este un film captivant, care îmbină acțiunea intensă cu concepte filozofice profunde despre natura realității și a subconștientului. Vizual uimitor și plin de suspans, filmul a devenit un succes critic și comercial, consolidând statutul lui Christopher Nolan ca unul dintre cei mai inovativi și provocatori regizori ai generației sale.</p>
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
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Montserrat', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f8f9fa;
            }
            header {
                background-color: #007bff;
                color: #fff;
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
                color: #007bff;
                font-weight: 700;
                transition: color 0.3s;
            }
            nav a:hover {
                color: #0056b3;
            }
            .container {
                padding: 30px;
                background-color: #fff;
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
            <a href="/descriere/inception">Descriere</a>
            <a href="/recenzii/inception">Recenzii</a>
        </nav>
        <div class="container">
            <ol>
                <li>
                    <p><strong>Rolling Stone</strong>: "«Inception» este un triumf al imaginației pure, cu efecte vizuale uimitoare și o poveste captivantă care te ține în suspans până la final. Christopher Nolan a creat o capodoperă a filmelor SF."</p>
                </li>
                <li>
                    <p><strong>The New York Times</strong>: "Un film provocator și inovator, «Inception» te poartă într-o călătorie fascinantă prin labirintul minții umane. Leonardo DiCaprio oferă o interpretare puternică în rolul principal, susținut de o distribuție impresionantă."</p>
                </li>
                <li>
                    <p><strong>The Guardian</strong>: "«Inception» este un reper în istoria cinematografiei, redefinind limitele a ceea ce este posibil pe marele ecran. Nolan a creat un univers complex și stratificat, plin de surprize și răsturnări de situație."</p>
                </li>
                <li>
                    <p><strong>Los Angeles Times</strong>: "Un film care te provoacă intelectual și emoțional, «Inception» este o experiență cinematografică unică. Viziunea lui Nolan despre lumea viselor este atât de bine realizată încât începi să te îndoiești de propria realitate."</p>
                </li>
                <li>
                    <p><strong>The Hollywood Reporter</strong>: "«Inception» este un tur de forță vizual și narativ, care demonstrează încă o dată geniul lui Christopher Nolan. Filmul îmbină acțiunea palpitantă cu idei filozofice profunde, creând o experiență de neuitat."</p>
                </li>
            </ol>
        </div>
    </body>
    </html>
    """
    return recenzii