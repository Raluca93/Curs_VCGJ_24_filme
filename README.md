<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>

<h1>Proiect Filme - Pipoi-Ionescu Andrei 441D</h1>

<h2>1. Functionalitate</h2>

<p>Proiectul de față constă într-o aplicație web care pune la dispoziție diverse funcționalități legate de un anumit film, selectat de dezvoltatori. În cazul de față, am optat să afișăm descrierea și câteva recenzii pentru pelicula <strong>Inception</strong>. Utilizatorul va putea accesa aceste caracteristici prin intermediul unor butoane intuitive, integrate în interfața aplicației web.</p>

<h3>Pagina Principală a Aplicației Web Filme</h3>
    <img src="https://i.imgur.com/gXKODuU.png" alt="Pagina Principală">

<h3>Pagina cu descrierea filmului</h3>
<div class="screenshot">
    <img src="https://i.imgur.com/Rrqf0km.png" alt="Descrierea filmului">
    <img src="https://i.imgur.com/pH0oTFw.png">
</div>

<h3>Pagina recenziilor</h3>
<div class="screenshot">
    <img src="https://i.imgur.com/HPCxx09.png" alt="Recenziile filmului">
</div>

<h2>2. Stadiul Implementării</h2>

<p>Versiunea finală și funcțională a codului a fost încărcată pe platforma Git. Această variantă operațională poate fi accesată prin intermediul următorului link:<a href="https://github.com/Raluca93/Curs_VCGJ_24_filme">https://github.com/Raluca93/Curs_VCGJ_24_filme</a></p>

<h2>3. Testare</h2>

<p>Procesul de testare poate fi realizat atât în mod manual, prin executarea fișierului <code>test_script.py</code> în cadrul mașinii virtuale locale, cât și automat, prin intermediul platformei Jenkins. În cazul utilizării Jenkins, testele se vor derula în mod automat, fără a necesita configurări suplimentare de fiecare dată când se dorește efectuarea unui nou test.</p>

<h3>Testarea Locală</h3>
<p>În scopul verificării funcționalității, avem opțiunea de a efectua testarea în mediul local, utilizând terminalul și executând următoarele comenzi:</p>
<div class="screenshot">
    <img src="https://i.imgur.com/dw4ExPi.png" alt="Testare locală 1">
</div>
<div class="screenshot">
    <img src="https://i.imgur.com/oHgg4JL.png" alt="Testare locală 2">
</div>

<h3>Jenkins</h3>
<p>Pentru a realiza testarea prin intermediul platformei Jenkins, va fi necesară configurarea unui job Jenkins corespunzător, precum și asigurarea că serviciul Jenkins este funcțional (pornit prin executarea comenzii <code>jenkins</code> în terminal).</p>

<div class="screenshot">
    <img src="https://i.imgur.com/Pfy3cBh.png" alt="Configurare Jenkins">
</div>

<p>Odată ce jobul Jenkins a fost configurat corespunzător, codul sursă este funcțional, iar testele locale au fost trecute cu succes (<em>passed</em>), următorul pas constă în încărcarea proiectului pe platforma Git. Această etapă este necesară pentru a putea configura pipeline-ul Jenkins și a rula testele automate din cadrul acestei platforme.</p>

<h3>Configurare Pipeline în Jenkins</h3>
<div class="screenshot">
    <img src="https://i.imgur.com/KAoGaFq.png" alt="Configurare Pipeline">
</div>

<p>După finalizarea configurării pipeline-ului Jenkins, va fi necesară declanșarea procesului de testare prin apăsarea butonului <em>Build Now</em>. Se va aștepta terminarea rulării testelor automate, după care se va verifica dacă acestea au trecut cu succes (<em>passed</em>).</p>

<div class="screenshot">
    <img src="https://i.imgur.com/JPf2f4g.png">
</div>
<div class="screenshot">
    <img src="https://i.imgur.com/S3X325P.png">
</div>
<div class="screenshot">
    <img src="https://i.imgur.com/eIhO4Ud.png">
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
    <img src="https://i.imgur.com/uyFmpZw.png">
</div>
<div class="screenshot">
    <img src="https://i.imgur.com/KKHUnaf.png" alt="Finalizare Teste">
</div>
<h2>Fisier DockerFile</h2>
<div class="screenshot">
    <img src="https://i.imgur.com/sVy49LB.png" alt="Finalizare Teste">
</div>
<h2></h2>
<h2>Aplicatia functioneaza din container</h2>
<div class="screenshot">
    <img src="https://i.imgur.com/pWYT90D.png" alt="Finalizare Teste">
</div>
