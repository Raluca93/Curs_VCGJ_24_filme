[DOBRE OCTAVIAN - Curs_VCGJ_24_filme](/../main/README.md)

# Curs_VCGJ_24_filme

# Cuprins

- [Descriere aplicatie](#descriere-aplicatie)
- [Configurare](#configurare)
  - [Configurare .venv si instalare pachete](#configurare-venv-si-instalare-pachete)
- [Testare cu pytest](#testare-cu-pytest)
- [Verificare statica - pylint](#verificare-statica---pylint)
- [Utilizare Docker si containerizare aplicatie](#utilizare-docker-si-containerizare-aplicatie)
- [DevOps CI](#devops-ci)

# Descriere aplicatie

Aplicatia filme contine o descriere a unui film pe care o afiseaza intr-o pagina web. A fost testata pe Ubuntu 22.04. Componenta WEB a aplicatiei se bazeaza pe framework-ul Flask. Aplicatia este simpla, continand informatii legate de filme (ex: distributie, rating, actiune etc) preluate apoi in functii view si returnate clientului WEB care apeleaza serverul.

Pentru o navigare mai usoara in browser, pagina principala contine link-uri catre celelalte pagini. Fiecare pagina specifica contine un link catre pagina principala.

Aplicatia include suport pentru containerizare in fisierul Dockerfile din directorul principal al aplicatiei.

Din punct de vedere al testarii, este inculs unit testing cu pytest, pentru o parte din functiile din biblioteca aplicatiei, aflate in directorul `app/lib`.

## Configurare

### Configurare .venv si instalare pachete

**activeaza_venv**: Incearca sa activeze venv-ul. Daca nu poate, configureaza venv-ul in directorul `.venv` si apoi instaleaza Flask. La urmatoarea rulare, va activa doar venv-ul.

## Testare cu pytest

O parte din functiile din biblioteca de functii a aplicatiei:

Directorul `lib`, fisierele:

- `biblioteca_filme.py`
- `description.py`
- `rating.py`

Au teste de tip 'unit - test' asociate - adica - este apelata functia si se asteapta o anumita valoare. Testul compara valoarea obtinuta la apelul functie cu valoarea asteptata si returneaza PASS daca valoarea primita de la functie este cea asteptata si FAIL in caz contrar.

Pentru testare s-a folosit pachetul `pytest` din Python. Acesta se afla in lista de pachete care trebuie instalate, in fisierul `quickrequirements.txt`.

## Verificare statica - pylint

**pylint** - pachet Python folosit la testarea calitatii codului (spatii, nume variabile, variabile neutilizate etc.)

## Utilizare Docker si containerizare aplicatie

Aplicatia poate fi instalata intr-un container Docker.

Pentru aceasta, este nevoie de fisierul: `Dockerfile`. Acesta contine informatiile de care are nevoie aplicatia Docker pentru a crea containerul. Dupa creerea `Dockerfile`, in acelasi director cu acest fisier trebuie executata comanda:

```bash
sudo docker build -t filme:v01 .
```

Aceasta creeaza o imagine de container care poate fi vizualizata cu comanda:

```bash
sudo docker images
```

Pentru a genera un container din fisierul imagine trebuie executata comanda run:

```bash
sudo docker run --name filme -p 8020:5011 filme:v01
```

## DevOps CI

Pipeline-ul pentru Jenkins este definit in fisierul `Jenkinsfile`.

Pipeline-ul cloneaza codul, creaza mediul de lucru virtual (venv-ul), il activeaza si ruleaza testele (unit test - cu pytest, verificari statice cu pylint).
