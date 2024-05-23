# Curs VCGJ_24_filme

##  1.Functionalitatea adaugata

#### Aplicatia software dezvoltata are ca scop afisarea descrierii unui film ales, in acest caz Die Hard 3, si a unor recenzii ale acestuia cu posibiliatea de a naviga printre aceste informatii ele fiind afisate la apasarea unui buton.

##### Pagina principala
![pagina principala](https://i.imgur.com/PjBC7Ok.png)

##### Pagina pe care se gaseste descrierea
![descriere](https://i.imgur.com/Jn5ekGB.png)

##### Pagina unde gasim recenziile
![recenzii](https://i.imgur.com/c56lbgB.png)

## 2. Stadiul implementarii

##### Ultima varianta a codului, si cea functionala a fost incarcata pe git si acesta este functional. Se poate gasi la link: https://github.com/Raluca93/Curs_VCGJ_24_filme
##
##
##

## 3. Teste Jenkins
##### Testele se pot face atat manual, ruland fiserului test_content.py din masina virtuala, dar si prin intermediul Jenkins unde se vor desfasura automat fara a mai fi nevoie de configurare de fiecare data cand se doreste un test. 
##
##
##

#### 3 Testare
#### Configurarea pentru testare
##### Putem apela fisierul de teste si direct din terminal prin urmatoarele comenzi
![testare-man](https://i.imgur.com/9UODWIO.png)
##

## Jenkins
##### Pentru a putea face testele cu Jenkins vom avea nevoie de o configuratie jenkins, iar serviciul va trebui sa fie pornit (comanda jenkins in terminal)
##
##

#### Configurare fisier Jenkins
![jenkins](https://i.imgur.com/uSscEWF.png)

##### Dupa ce fisierul jenkins este configurat, iar codul este functionat si testele sunt passed la pasul anterior, trebuie sa incarcam proiectul pe git pentru a putea seta pipe-line-ul si a rula testele din Jenkins.

### Configurare Pipe-line in Jenkins
![pipe-line](https://i.imgur.com/ayEpk9q.png)
##### Dupa ce Pipe-line ul este configurat, se va apasa pe butonul Build Now si se asteapta terminarea testelor apoi se verifica daca acestea sunt passed
![teste](https://i.imgur.com/0e1kwLW.png)
##
##

## 4.Integrarea

##### Pentru a incarca o versiune a programului pe git, va fi nevoie de urmatoarele comezi
![incarcaregit](https://i.imgur.com/amvpRCo.png)

##### Apoi vom intra pe git si vom face un pull request nou, pentru a trece de pe devel pe main
![pullreq](https://i.imgur.com/a56j2Ai.png)

##### Pull request pentru a pune pe main, cu reviewer IancuCostin
![pullreqrev](https://i.imgur.com/zamhy8V.png)
## 
## 5.Containerizarea
##### Pentru containerizare se va folosi un Dockerfile. Se vor da urmatoarele comenzi in terminal :
#### docker build -t proiectfilme . //creare imagine
#### docker run -dp 127.0.0.1:5000:5000 proiectfilme  // pornire container
#### docker image ls //afisare imagini prezente pe masina
#### docker ps // afiseaza containerele care ruleaza
![docker](https://i.imgur.com/6xIibOJ.png)

### Fisier DockerFile 
![dockerfile](https://i.imgur.com/l3EA8Xb.png)

##
##
##

### Aplicatia functioneaza prin intermediul containerului
![cont](https://i.imgur.com/vordqaO.png)














