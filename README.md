<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>

<h1>Proiect Filme - Musuroia Mircea-MIhai 441D</h1>

<h2>1. Functionalitate</h2>

<p>Proiectul de față constă într-o aplicație web care pune la dispoziție diverse funcționalități legate de un anumit film, selectat de dezvoltatori. În cazul de față, am optat să afișăm descrierea și câteva recenzii pentru pelicula <strong>Fight Club</strong>. Utilizatorul va putea accesa aceste caracteristici prin intermediul unor butoane intuitive, integrate în interfața aplicației web.</p>

<h3>Pagina Principală a Aplicației Web Filme</h3>
    <img src="https://i.imgur.com/qEY317h.jpg" alt="Pagina Principală">

<h3>Pagina cu descrierea filmului</h3>
<div class="screenshot">
    <img src="https://i.imgur.com/1RemabQ.jpg" alt="Descrierea filmului">
</div>

<h3>Pagina recenziilor</h3>
<div class="screenshot">
    <img src="https://i.imgur.com/u7Eh1h3.jpg" alt="Recenziile filmului">
</div>

<h2>2. Stadiul Implementării</h2>

<p>Versiunea finală și funcțională a codului a fost încărcată pe platforma Git. Această variantă operațională poate fi accesată prin intermediul următorului link:<a href="https://github.com/Raluca93/Curs_VCGJ_24_filme">https://github.com/Raluca93/Curs_VCGJ_24_filme</a></p>

<h2>3. Testare</h2>

<p>Procesul de testare poate fi realizat atât în mod manual, prin executarea fișierului <code>test_script.py</code> în cadrul mașinii virtuale locale, cât și automat, prin intermediul platformei Jenkins. În cazul utilizării Jenkins, testele se vor derula în mod automat, fără a necesita configurări suplimentare de fiecare dată când se dorește efectuarea unui nou test.</p>

<h3>Testarea Locală</h3>
<p>În scopul verificării funcționalității, avem opțiunea de a efectua testarea în mediul local, utilizând terminalul și executând următoarele comenzi:</p>
<div class="screenshot">
    <img src="https://i.imgur.com/yIThFjx.jpg" alt="Testare locală 1">
</div>
<div class="screenshot">
    <img src="https://i.imgur.com/5xIlsd9.jpg" alt="Testare locală 2">
</div>

<h3>Jenkins</h3>
<p>Pentru a realiza testarea prin intermediul platformei Jenkins, va fi necesară configurarea unui job Jenkins corespunzător, precum și asigurarea că serviciul Jenkins este funcțional (pornit prin executarea comenzii <code>jenkins</code> în terminal).</p>

<div class="screenshot">
    <img src="https://i.imgur.com/u1hPVDX.jpg" alt="Configurare Jenkins">
</div>
<h2>4.Integrarea</h2>
<h3>Pentru a încărca proiectul pe platforma GitHub, într-una dintre ramurile de utilizator, vor fi utilizate următoarele comenzi:</h3>
<div class="screenshot">
    <img src="https://i.imgur.com/zXExcXs.png">
</div>
<h3>Ulterior, vom accesa repository-ul Git și vom crea o nouă solicitare de pull request, cu scopul de a transfera modificările din ramura devel în ramura main. Această solicitare de pull request a fost configurată astfel încât să necesite aprobarea din partea unui reviewer, înainte de a fi acceptată.</h3>
<h2>5.Containerizarea</h2>
În vederea containerizării aplicației, se va utiliza un fișier Dockerfile. Se vor executa următoarele comenzi în terminal:
<h3>docker build -t filme_app . // construirea imaginii Docker</h3>
<h3>docker run -p 5000:5000 filme_app // pornirea containerului</h3>
<h3>docker images // afișarea imaginilor Docker prezente pe mașină</h3>
<h3>docker ps // afișarea containerelor Docker care rulează în prezent</h3>
<div class="screenshot">
    <img src="https://i.imgur.com/CCkwepL.jpg">
</div>
<div class="screenshot">
    <img src="https://i.imgur.com/jzXtUtw.jpg" alt="Finalizare Teste">
</div>
<h2>Fisier DockerFile</h2>
<div class="screenshot">
    <img src="https://i.imgur.com/VC1RS2F.jpg" alt="Finalizare Teste">
</div>
<h2></h2>
<h2>Aplicatia functioneaza din container</h2>
<div class="screenshot">
    <img src="https://i.imgur.com/fD8aZvb.jpg" alt="Finalizare Teste">
</div>
