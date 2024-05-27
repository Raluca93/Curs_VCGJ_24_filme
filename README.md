> # Descriere aplicatie
O pagină web care prezintă filmul Forrest Gump.


> # Configurare
Configurare .venv si instalare pachete

In directorul curent rulati comenzile:
* activeaza_venv: Incearca sa activeze venv-ul. Daca nu poate, configureaza venv-ul in directorul .venv si apoi instaleaza flask. La urmatoarea rulare, va activa doar venv-ul.
  
![Configurare](images/activate_venv.png)


> # Pagina web

![Pagina Web](images/index.png)
![Pagina Web](images/fg.png)
![Pagina Web](images/actiune.png)
![Pagina Web](images/distributie.png)


> # Utilizare Docker
> Creare imagine
> 
> `sudo docker build -t filme:v02 .`
> 
> `sudo docker images`

![Utilizare Docker](images/flask.png)


> Rulare container
>
> `sudo run filme:v02`
>
![Utilizare Docker](images/docker_container.png)

> # Jenkins Pipeline 

![Jenkins Pipeline](images/jenkins.png)

