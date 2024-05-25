<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>

<h1>Proiect Filme - Loliciu Andrei</h1>

<h2>1. Partea de cod functionala si testata</h2>

<p>Aplicația software dezvoltată are ca scop afișarea a doua functii specifice elementului proiectului, in cazul nostru un film. Am ales filmul Ratatouille, cu functiile specifice <strong>Descriere</strong> si <strong>Recenzii</strong>.</p>

<h3>Pagina Principală a Aplicației Web</h3>
    <img src="https://i.postimg.cc/prb2LwXR/image.png" alt="Pagina Principală">

<h3>Descrierea filmului</h3>
<div class="screenshot">
    <img src="https://i.postimg.cc/Vk05zP8Z/image.png" alt="Descrierea filmului">
</div>
<div class="screenshot">
    <img src="https://i.postimg.cc/bvNysXcj/image.png" alt="Descrierea filmului cont">
</div>

<h3>Recenziile filmului</h3>
<div class="screenshot">
    <img src="https://i.postimg.cc/htMJC1Kc/image.png" alt="Recenziile filmului">
</div>

<h2>2.Integrare pe GitHub</h2>
<h3>Pentru a incarca proiectul pe github, in branch-ul personal vom utilzia urmatoarele comenzi</h3>
<div class="screenshot">
    <img src="https://i.postimg.cc/bNTJKD6g/image.png" alt="Exemplu git add, commit si push">
</div>
<h3>In continuare, avand versiunea finala a proiectului pregatita, din GitHub vom face un pull-request pentru main, avand ca reviewer pe Iancu Costin.</h3>

<h2>3. Testare</h2>

<h3>Testarea Local</h3>
<p>Pentru a verifica funcționalitatea, putem alege să testam local, din terminal prin folosirea urmatoarelor comenzi:</p>
<div class="screenshot">
    <img src="https://i.postimg.cc/SKsNdbnS/image.png" alt="Testare locala 1">
</div>

<h3>Jenkins</h3>
<p>Pentru a putea face testele cu Jenkins vom avea nevoie de o configurație Jenkins, iar serviciul va trebui să fie pornit (comanda <code>jenkins</code> în terminal).</p>

<div class="screenshot">
    <img src="https://i.postimg.cc/wjKsvv4C/image.png" alt="Configurare Jenkins">
</div>

<p>Dupa ce fisierul Jenkins este configurat, dam push la repository-ul local pe branch-ul de dezvoltator ca sa putem verifica functionalitatea codului printr-un pipeline.</p>

<h3>Configurare pipeline în Jenkins</h3>
<div class="screenshot">
    <img src="https://i.postimg.cc/wxs7yNyw/image.png" alt="Configurare Pipeline">
</div>

<p>Dupa ce pipeline-ul este configurat, <em>Build Now</em> si se asteapta terminarea testelor apoi se verifica daca acestea sunt <em>passed</em>.</p>

<div class="screenshot">
    <img src="https://i.postimg.cc/PJvqZCXs/image.png" alt="Test Passed">
</div>

<h2>4.Containerizarea</h2>
Pentru containerizare se va folosi un Dockerfile. Se vor da urmatoarele comenzi in terminal :
<h3>docker build -t curs_vcgj_24_filme:v05 . //creare imagine</h3>
<h3>docker run -p 5000:5000 curs_vcgj_24_filme:v05 // pornire container</h3>
<p>Imaginea este deja creata, asa ca am folosit comanda docker images pentru a vedea imaginile create</p> 
<div class="screenshot">
    <img src="https://i.postimg.cc/dtRQGP2f/image.png" alt="Setup Docker">
</div>

<h2>Fisier DockerFile</h2>
<div class="screenshot">
    <img src="https://i.postimg.cc/VLPH05Wj/image.png" alt="Dockerfile">
</div>
<h2></h2>
<h2>Aplicatia functioneaza din container</h2>
<div class="screenshot">
    <img src="https://i.postimg.cc/qqqB8jT5/image.png" alt="Finalizare Teste">
</div>
