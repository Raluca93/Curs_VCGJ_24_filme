<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>

<h1>Proiect Filme - Gabor Andrei 441D</h1>

<h2>1. Functionalitate</h2>

<p>Aplicația software dezvoltată are ca scop afișarea unor funcționalități pentru un film ales de noi. În cazul meu, am ales să prezint descrierea și câteva recenzii ale filmului <strong>The Lighthouse</strong>. Navigarea prin aceste funcționalități se va face prin apăsarea unor butoane specifice, prezente în aplicația web.</p>

<h3>Pagina Principală a Aplicației Web Filme</h3>
    <img src="https://i.imgur.com/YzmCsb1.png" alt="Pagina Principală">

<h3>Pagina cu descrierea filmului</h3>
<div class="screenshot">
    <img src="https://i.imgur.com/7uovOjb.png" alt="Descrierea filmului">
    
</div>

<h3>Pagina recenziilor</h3>
<div class="screenshot">
    <img src="https://i.imgur.com/jBWQpf8.png" alt="Recenziile filmului">
</div>

<h2>2. Stadiul Implementării</h2>

<p>Ultima variantă a codului, și cea funcțională a fost încărcată pe Git și aceasta este funcțională. Se poate găsi la link: <a href="https://github.com/Raluca93/Curs_VCGJ_24_filme">https://github.com/Raluca93/Curs_VCGJ_24_filme</a></p>

<h2>3. Testare</h2>

<p>Testele se pot face atât manual, rulând fișierului <code>test_script.py</code> din mașina virtuală, local, dar și prin intermediul Jenkins unde se vor desfășura automat fără a mai fi nevoie de configurare de fiecare dată când se dorește un test.</p>

<h3>Testarea Locala</h3>
<p>Pentru a verifica funcționalitatea, putem alege să testăm local, din terminal prin folosirea următoarelor comenzi:</p>
<div class="screenshot">
    <img src="https://i.imgur.com/7s3N3Eu.png" alt="Testare locală 1">
</div>
<div class="screenshot">
    <img src="https://i.imgur.com/C0nwFbU.png" alt="Testare locală 2">
</div>

<h3>Jenkins</h3>
<p>Pentru a putea face testele cu Jenkins vom avea nevoie de o configurație Jenkins, iar serviciul va trebui să fie pornit (comanda <code>jenkins</code> în terminal).</p>

<div class="screenshot">
    <img src="https://i.imgur.com/R2w6HO1.png" alt="Configurare Jenkins">
</div>

<p>După ce fișierul Jenkins este configurat, iar codul este funcțional și testele sunt <em>passed</em> la pasul anterior, trebuie să încărcăm proiectul pe Git pentru a putea seta pipeline-ul și a rula testele din Jenkins.</p>

<h3>Configurare Pipeline în Jenkins</h3>
<div class="screenshot">
    <img src="https://i.imgur.com/OnbdktL.png" alt="Configurare Pipeline">
</div>

<p>După ce Pipeline-ul este configurat, se va apăsa pe butonul <em>Build Now</em> și se așteaptă terminarea testelor apoi se verifică dacă acestea sunt <em>passed</em>.</p>

<div class="screenshot">
    <img src="https://i.imgur.com/p2PbL0K.png">
</div>
<div class="screenshot">
    <img src="https://i.imgur.com/x1DGcRJ.png">
</div>
<div class="screenshot">
    <img src="https://i.imgur.com/8NUuFWj.png">
</div>
<h2>4.Integrarea</h2>
<h3>Pentru a incarca proiectul pe github, in unul din branch-urile de utilizator, vor fi folosite urmatoarele comenzi</h3>
<div class="screenshot">
    <img src="https://i.imgur.com/31YRu3e.png">
</div>
<h3>Apoi vom intra pe git si vom face un pull request nou, pentru a trece de pe devel pe main. Pull request-ul a fost facut astfel incat sa fie nevoie de aprobarea unui reviewer.</h3>
<h2>5.Containerizarea</h2>
Pentru containerizare se va folosi un Dockerfile. Se vor da urmatoarele comenzi in terminal :
<h3>docker build -t gabor_film . //creare imagine</h3>
<h3>docker run -p 5000:5000 gabor_film // pornire container</h3>
<h3>docker images//afisare imagini prezente pe masina</h3>
<h3>docker ps // afiseaza containerele care ruleaza</h3>
<div class="screenshot">
    <img src="https://i.imgur.com/krwWORz.png">
    <img src="https://i.imgur.com/bzFBo4D.png">
</div>
<h2>Fisier DockerFile</h2>
<div class="screenshot">
    <img src="https://i.imgur.com/o6oZNdA.png" alt="Finalizare Teste">
</div>
<h2></h2>
<h2>Aplicatia functioneaza din container</h2>
<div class="screenshot">
    <img src="https://i.imgur.com/JUJfluZ.png" alt="Finalizare Teste">
</div>
