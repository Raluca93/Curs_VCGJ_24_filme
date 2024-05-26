
# Curs_VCGJ_24_filme-Badea-Mitrut-441D
# Cuprins
1. [Descriere aplicatie](#descriere-aplicatie)
2. [Structura aplicatie](#structura-aplicatie)
3. [Docker](#docker)
4. [Jenkins](#jenkins)


> # Descriere aplicatie
  Tema proiectului propune realizarea unei aplicatii web care sa prezinte informatii specifice legate de un film la alegere. Filmul ales de mine este Interstellar, structura aplicatiei web fiind descrisa mai jos:

> # Structura aplicatie
  Aplicatia web este alcatuita din 3 pagini, fiecare oferind informatii specifice despre filmul ales.
  * Pagina Home - o scurta descriere a filmului, alaturi de poster si o lista sumara a principalelor nominalizari si premii obtinute
    
    ![Structura aplicatie](readme_images/Interstellar-Home.png)

  * Pagina Cast - o serie de portrete ale principalilor actori si, mai jos, o lista detaliata a rolurilor jucate in film

    ![Structura aplicatie](readme_images/Interstellar-Cast.png)

  * Pagina Reviews - o selectie de recenzii asupra filmului

    ![Structura aplicatie](readme_images/Interstellar-Reviews.png)

> # Docker
  Pentru etapa de containerizare a fost utilizat software-ul _Docker_. Am creat un container, am adaugat un tag pentru imagine si am urcat containerul pe _Docker Hub_ folosind o serie de comenzi specifice prezentate in cadrul cursului de SCC.
>  `sudo docker build -t scc_filme:v1`
> 
>  `sudo docker login`
> 
>  `sudo docker tag scc_filme:v1 mitrutbadea/scc_filme:v1`
> 
>  `sudo docker push mitrutbadea/filme_scc:v1`

  Am rulat aplicatia utilizand comanda:
> `sudo docker run --name site -d -p 8011:5020 mitrutbadea/scc_filme:v1`
>

> # Jenkins
  In aceasta etapa, testele au fost realizate utilizand serverul de automatizare _Jenkins_. Mai jos sunt atasate cateva capturi de ecran ce surprind rezultatele obtinute in urma procesului de testare.

  ![Jenkins](readme_images/test_jenkins_dev.png)
  ![Jenkins](readme_images/test_jenkins_main.png)
  

  


    
