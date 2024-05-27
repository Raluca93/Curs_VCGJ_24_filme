# Curs_VCGJ_24_filme-Slavoiu_Alexandru-441D
# Cuprins
1. [Descriere aplicatie](#descriere-aplicatie)
2. [Structura aplicatie](#structura-aplicatie)
3. [Docker](#docker)
4. [Jenkins](#jenkins)


> # Descriere aplicatie
  Tema proiectului propune realizarea unei aplicatii web care sa prezinte informatii specifice legate de un film la alegere. Filmul pe care l-am ales este Terminator 2: Judgment Day. Mai jos am descris forma acestei aplicatii web. 

> # Structura aplicatie
  Aplicatia web este alcatuita din 3 pagini, fiecare oferind informatii specifice despre filmul ales.
  * Pagina Home - o scurta descriere a filmului alaturi de poster si o scurta trecere in revista a principalelor nominalizari si premii obtinute
    
    ![Structura aplicatie](readme_images/Terminator2Home.png)

  * Pagina Cast - o serie de portrete ale principalilor actori si, mai jos, o lista detaliata a rolurilor jucate in film

    ![Structura aplicatie](readme_images/Terminator2Cast.png)

  * Pagina Reviews - o selectie de recenzii ale unor critici asupra filmului

    ![Structura aplicatie](readme_images/Terminator2Review.png)

> # Docker
  Pentru etapa de containerizare am folosit software-ul _Docker_. Am creat un container, am adaugat un tag pentru imagine si am urcat containerul pe _Docker Hub_ folosind o serie de comenzi specifice prezentate in cadrul cursului de SCC.
>  `sudo docker build -t proiectscc:v01 .`
> 
>  `sudo docker login`
> 
>  `sudo docker tag proiectscc:v01 alexslavoiu/proiectscc:v01`
> 
>  `sudo docker push alexslavoiu/proiectscc:v01`

  ![Image](https://github.com/Raluca93/Curs_VCGJ_24_filme/blob/dev-alexslavoiu/readme_images/Docker.png)  

  In aceasta poza arat ca am realizat cu succes aceasta operatie de creare a unui container si urcarea acestuia pe Docker Hub. 

> # Jenkins
  In aceasta etapa, testele au fost realizate utilizand serverul de automatizare _Jenkins_. Mai jos sunt atasate cateva capturi de ecran ce surprind rezultatele obtinute in urma procesului de testare.
  
  ![Jenkins](readme_images/Jenkins_Dev.png)
  ![Jenkins](readme_images/Jenkins_Main.png)
  
  


    
