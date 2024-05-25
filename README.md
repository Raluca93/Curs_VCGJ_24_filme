# filme
# Cuprins
1. [Descriere aplicatie](#descriere_aplicatie)
2. [Configurare](#configurare)
3. [Pagina web](#pagina_web)
4. [Utilizare Docker](#docker)
5. [Jenkins Pipeline](#jenkins)


> ## Descriere aplicatie
O pagină web care prezintă filmul Iron Man.


> ## Configurare
Configurare .venv si instalare pachete

In directorul curent rulati comenzile:
* activeaza_venv: Incearca sa activeze venv-ul. Daca nu poate, configureaza venv-ul in directorul .venv si apoi instaleaza flask. La urmatoarea rulare, va activa doar venv-ul.
  
![Configurare](images/activate_venv.png)


> ## Pagina web

![Pagina Web](images/pagina_filme.png)
![Pagina Web](images/Barbie_principal.png)
![Pagina Web](images/Barbie_actiune.png)
![Pagina Web](images/Barbie_distributie.png)


> ## Utilizare Docker
> Creare imagine
> 
> sudo docker build -t filme:v01 .
> 
> sudo docker images

![Utilizare Docker](images/filme_flask.png)


> Rulare container
>
> sudo run filme:v01
>
![Utilizare Docker](images/docker_run.png)

> ## Jenkins Pipeline

![Jenkins Pipeline](images/Succes.png)
