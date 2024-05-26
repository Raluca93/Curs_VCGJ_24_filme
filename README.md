# Curs_VCGJ_24_filme


`filme`
===================================

# Cuprins

1. [Descriere aplicatie](#descriere-aplicatie)
1. [Configurare](#configurare)
1. [Exemple pagina web](#exemple-pagina-web)
1. [Testare cu pytest](#testare-cu-pytest)
1. [Verificare statica. pylint - calitate cod](#verificare-statica-cu-pylint)
1. [DevOps](#devops-ci)
   1. [Pipeline Jenkins](#exemplu-executie-pipeline-jenkins)
   


# Descriere aplicatie (Dune)

Aplicatia filme reprezinta o platforma de prezentare a diverse filme alese de catre fiecare student in parte.
Poate fi executata doar pe Linux. A fost testata pe Ubuntu 22.04.
Componenta WEB a aplicatiei se bazeaza pe framework-ul `Flask`.
Aplicatia este simpla, fiind constituita din afisarea unor template-uri de html printr-un mvc (filme.py).
Anumite elemente precum descrierea filmului, rating sau cast-ul sunt generate prin prisma unor functii .py dedicate aflate in folderul app/lib.

Pentru o navigare mai usoara in browser, pagina principala contine link-uri catre celelalte pagini.
Fiecare pagina specifica trateaza un film diferit.

Aplicatia include suport pentru containerizare in fisierul `Dockerfile` din directorul principal al aplicatiei.

Din punct de vedere al testarii, este inculs unit testing cu pytest, pentru o parte din functiile din biblioteca aplicatiei, aflate in directorul `app/lib`.

`DevOps CI`.
Pipeline-ul pentru Jenkins este definint in fisierul `Jenkinsfile`.


Ambele pipeline-uri cloneaza codul, creaza mediul de lucru virtual (venv-ul), il activeaza si ruleaza testele (unit test - cu pytest, verificari statice cu pylint).




# Configurare
[cuprins](#configurare)

Configurare .venv si instalare pachete

In directorul 'app' rulati comenzile:

1) activeaza_venv: Incearca sa activeze venv-ul. 
                   Daca nu poate, configureaza venv-ul in directorul .venv si apoi instaleaza flask si flask-bootstrap.
                   La urmatoarea rulare, va activa doar venv-ul.
                
2) ruleaza_aplicatia: De rulat doar dupa activarea venv-ului. 
                      Va porni serverul pe IP: 127.0.0.1 si port: 5000.
                      Acces server din browser: http://127.0.0.1:5000






# EXEMPLE pagina web 
## Pagina principala
[cuprins](#exemple-pagina-web)
![image](https://github.com/Raluca93/Curs_VCGJ_24_filme/blob/dev-rusude/static/Description-Dune.png)

![image](https://github.com/Raluca93/Curs_VCGJ_24_filme/blob/dev-rusude/static/Cast-Dune.png)



# Testare cu pytest
[cuprins](#testare-cu-pytest)

O parte din functiile din biblioteca de functii a aplicatie:
- directorul lib, fisierele:
  - descriere_Dune.py
  - rating_Dune.py
au teste de tip 'unit - test' asociate - adica - este apelata functia si se asteapta o anumita valoare.
Testul compara valoarea obtinuta la apelul functie cu valoarea asteptata si returneaza PASS daca valoarea primita de la functie este cea asteptata si FAIL in caz contrar.

Pentru testare s-a folosit pachetul **pytest** din python. Acesta se afla in lista de pachete care trebuie instalate, in fisierul quickrequirements.txt.
Executia testelor se face cu oricare din comenzile de mai jos, apelate din directorul aplicatiei - *sysinfo*:
```
   pytest
   python -m pytest
   flask --app sysinfo test

   Ultima commanda este posibila datorita implementarii comenzii cli test in aplicatia sysinfo.
   Aceasta comanda CLI, apeleaza pytest din program/script:
       pytest.main(["."])
   
   Ultima varianta, desi echivalenta cu primele doua, este mai eleganta.
   Primele doua apeleaza pytest ca fiind ceva extern aplicatiei. 
   Aici insa avem optiunea de a se 'autotesta' inclusa in aplicatie.
```



# Verificare statica cu pylint
[cuprins](#verificare-statica-cu-pylint)

- **pylint** - pachet python folosit la testarea calitatii codului (spatii, nume variabile, variabile neutilizate etc.)
- in cazul de fata, problemele returnate de pylint doar sunt afisate, nu sunt considerate erori







# DevOps CI
[cuprins](#devops-ci)
- CI = Continuous Integration

## Exemplu executie pipeline Jenkins
![image](https://github.com/Raluca93/Curs_VCGJ_24_filme/blob/dev-rusude/static/Jenkins-Dune.png)

