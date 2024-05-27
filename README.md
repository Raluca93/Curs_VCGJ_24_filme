
# Curs_VCGJ_24_filme

# Cuprins

- [Descriere aplicatie](#descriere-aplicatie)
- [Testare cu pytest](#testare-cu-pytest)
- [Verificare statica - pylint](#verificare-statica---pylint)
- [DevOps CI](#devops-ci)

# Descriere aplicatie

Aplicatia filme contine o descriere a unui film pe care o afiseaza intr-o pagina web. A fost testata pe Ubuntu 22.04. Componenta WEB a aplicatiei se bazeaza pe framework-ul Flask. Aplicatia este simpla, continand informatii legate de filme (ex: descriere , citate) preluate apoi in functii view si returnate clientului WEB care apeleaza serverul.

Pentru o navigare mai usoara in browser, pagina principala contine link-uri catre celelalte pagini. Fiecare pagina specifica contine un link catre pagina principala.

Aplicatia include suport pentru containerizare in fisierul Dockerfile din directorul principal al aplicatiei.

Din punct de vedere al testarii, este inculs unit testing cu pytest, pentru o parte din functiile din biblioteca aplicatiei, aflate in directorul `app/lib`.

Structura aplicatiei cuprinde fisierul principal filme.py care foloseste biblioteca creata de noi lib_filme‎.py in care sunt continute functiile :
- descriere_film()
- quotes()




## Testare cu pytest

O parte din functiile din biblioteca de functii a aplicatiei:

Directorul `lib`, fisierul:

- `lib_filme‎.py`

Are teste de tip 'unit - test' asociate - adica - este apelata functia si se asteapta o anumita valoare. Testul compara valoarea obtinuta la apelul functie cu valoarea asteptata si returneaza PASS daca valoarea primita de la functie este cea asteptata si FAIL in caz contrar.

Pentru testare s-a folosit pachetul `pytest` din Python. Acesta se afla in lista de pachete care trebuie instalate, in fisierul `quickrequirements.txt`.

## Verificare statica - pylint

**pylint** - pachet Python folosit la testarea calitatii codului (spatii, nume variabile, variabile neutilizate etc.)


## DevOps CI

Pipeline-ul pentru Jenkins este definit in fisierul `Jenkinsfile`.

Pipeline-ul cloneaza codul, creaza mediul de lucru virtual (venv-ul), il activeaza si ruleaza testele (unit test - cu pytest, verificari statice cu pylint).
