<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>

<h1>Proiect Filme - Iancu Costin 441D</h1>

<h2>1. Prezentarea Funcționalităților</h2>

<p>Aplicația software dezvoltată are ca scop afișarea unor funcționalități pentru un film ales de noi. În cazul meu, am ales să prezint descrierea și câteva recenzii ale filmului <strong>Central Intelligence</strong>. Navigarea prin aceste funcționalități se va face prin apăsarea unor butoane specifice, prezente în aplicația web.</p>

<h3>Pagina Principală a Aplicației Web</h3>
    <img src="https://i.imgur.com/TSrkYfu.png" alt="Pagina Principală">

<h3>Pagina unde este prezentată Descrierea</h3>
<div class="screenshot">
    <img src="https://i.imgur.com/RCqqZk7.png" alt="Descrierea filmului">
</div>

<h3>Pagina unde sunt prezentate Recenziile</h3>
<div class="screenshot">
    <img src="https://i.imgur.com/0rJ8B4Q.png" alt="Recenziile filmului">
</div>

<h2>2. Stadiul Implementării Actuale</h2>

<p>Ultima variantă a codului, și cea funcțională a fost încărcată pe Git și aceasta este funcțională. Se poate găsi la link: <a href="https://github.com/Raluca93/Curs_VCGJ_24_filme">https://github.com/Raluca93/Curs_VCGJ_24_filme</a></p>

<h2>3. Teste Jenkins</h2>

<p>Testele se pot face atât manual, rulând fișierului <code>test_script.py</code> din mașina virtuală, local, dar și prin intermediul Jenkins unde se vor desfășura automat fără a mai fi nevoie de configurare de fiecare dată când se dorește un test.</p>

<h3>Testarea Local</h3>
<p>Pentru a verifica funcționalitatea, putem alege să testăm local, din terminal prin folosirea următoarelor comenzi:</p>
<div class="screenshot">
    <img src="https://i.imgur.com/bY3c2E0.png" alt="Testare locală 1">
</div>
<div class="screenshot">
    <img src="https://i.imgur.com/2FjXfxa.png" alt="Testare locală 2">
</div>

<h3>Jenkins</h3>
<p>Pentru a putea face testele cu Jenkins vom avea nevoie de o configurație Jenkins, iar serviciul va trebui să fie pornit (comanda <code>jenkins</code> în terminal).</p>

<div class="screenshot">
    <img src="https://i.imgur.com/NlcxcHE.png" alt="Configurare Jenkins">
</div>

<p>După ce fișierul Jenkins este configurat, iar codul este funcțional și testele sunt <em>passed</em> la pasul anterior, trebuie să încărcăm proiectul pe Git pentru a putea seta pipeline-ul și a rula testele din Jenkins.</p>

<h3>Configurare Pipeline în Jenkins</h3>
<div class="screenshot">
    <img src="https://i.imgur.com/CruVsFK.png" alt="Configurare Pipeline">
</div>

<p>După ce Pipeline-ul este configurat, se va apăsa pe butonul <em>Build Now</em> și se așteaptă terminarea testelor apoi se verifică dacă acestea sunt <em>passed</em>.</p>

<div class="screenshot">
    <img src="https://i.imgur.com/HIKhmOa.png" alt="Build Now">
</div>
<div class="screenshot">
    <img src="https://i.imgur.com/UiYl6sk.png" alt="Test Passed">
</div>
<div class="screenshot">
    <img src="https://i.imgur.com/l7kXzlH.png" alt="Finalizare Teste">
</div>
<h2>4.Integrarea</h2>
<h3>Pentru a incarca proiectul pe github, in unul din branch-urile de utilizator, vor fi folosite urmatoarele comenzi</h3>
<div class="screenshot">
    <img src="https://i.imgur.com/FfB02ch.png" alt="Finalizare Teste">
</div>
<h3>Apoi vom intra pe git si vom face un pull request nou, pentru a trece de pe devel pe main. Pull request-ul a fost facut astfel incat sa fie nevoie de aprobarea unui reviewer, in cazul meu, Loliciu Andrei.</h3>
<h2>5.Containerizarea</h2>
Pentru containerizare se va folosi un Dockerfile. Se vor da urmatoarele comenzi in terminal :
<h3>docker build -t proiectfilme . //creare imagine</h3>
<h3>docker run -dp 127.0.0.1:5000:5000 proiectfilme // pornire container</h3>
<h3>docker image ls //afisare imagini prezente pe masina</h3>
<h3>docker ps // afiseaza containerele care ruleaza</h3>
<div class="screenshot">
    <img src="https://i.imgur.com/CiMd7Ck.png" alt="Finalizare Teste">
</div>
<div class="screenshot">
    <img src="https://i.imgur.com/ZVokln8.png" alt="Finalizare Teste">
</div>
<div class="screenshot">
    <img src="https://i.imgur.com/599SSQd.png" alt="Finalizare Teste">
</div>
<h2>Fisier DockerFile</h2>
<div class="screenshot">
    <img src="https://i.imgur.com/QLnLSxY.png" alt="Finalizare Teste">
</div>
<h2></h2>
<h2>Aplicatia functioneaza din container</h2>
<div class="screenshot">
    <img src="https://i.imgur.com/L1jVhkf.png" alt="Finalizare Teste">
</div>
