# Curs_VCGJ_24_filme


`FILME`
===================================

# Cuprins

1. [Descriere aplicatie](#descriere-aplicatie)
1. [Configurare](#configurare)
1. [Exemple pagina web](#exemple-pagina-web)
1. [Testare cu pytest](#testare-cu-pytest)
1. [Verificare statica. pylint - calitate cod](#verificare-statica-cu-pylint)
1. [DevOps](#devops-ci)
   1. [Pipeline Jenkins](#exemplu-executie-pipeline-jenkins)
   


# Descriere aplicatie (MONSTERS, INC.)

Aplicația Filme este o platformă pentru prezentarea diverselor filme alese individual de fiecare student. Funcționează exclusiv pe Linux și a fost testată pe Ubuntu 22.04. Componenta web a aplicației utilizează framework-ul `Flask`. Aplicația este simplă, afișând template-uri HTML printr-un model MVC (filme.py). Anumite elemente, precum descrierea filmului, rating-ul sau distribuția, sunt generate de funcții `.py` dedicate, aflate în folderul `app/lib`.

Pentru a facilita navigarea în browser, pagina principală conține linkuri către celelalte pagini, fiecare dedicată unui film diferit.

Aplicația include suport pentru containerizare, definit în fișierul `Dockerfile` din directorul principal al aplicației.

În ceea ce privește testarea, sunt incluse teste unitare cu pytest pentru o parte din funcțiile din biblioteca aplicației, aflate în directorul `app/lib`.

Pentru `DevOps CI`, pipeline-ul Jenkins este definit în fișierul `Jenkinsfile`.

Ambele pipeline-uri clonează codul, creează mediul de lucru virtual (venv), îl activează și rulează testele (teste unitare cu pytest, verificări statice cu pylint).


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
![image](https://github.com/Raluca93/Curs_VCGJ_24_filme/blob/dev-Victor/static/static/main.png)

![image](https://github.com/Raluca93/Curs_VCGJ_24_filme/blob/dev-Victor/static/static/home.png)

![image](https://github.com/Raluca93/Curs_VCGJ_24_filme/blob/dev-Victor/static/static/cast.png)

![image](https://github.com/Raluca93/Curs_VCGJ_24_filme/blob/dev-Victor/static/static/plot.png)




# Testare cu pytest
[cuprins](#testare-cu-pytest)

O parte din functiile din biblioteca de functii a aplicatie:
- directorul lib, fisierele:
  - description_MonstersINCpy
  - rating_MonstersINC.py
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
![image](https://github.com/Raluca93/Curs_VCGJ_24_filme/blob/dev-Victor/static/jenkins.png)
