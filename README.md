**Descriere aplicatie**:
Pagina web simpla facuta cu Flask.

**Functionalitate**:
Codul a fost preluat de pe alt branch si modificat. In urma modificarilor -> pagina web Film Matrix.
Pagina devine functionala prin intermediu fisierului ruleaza_aplicatia

**Teste**:
Teste Jenkins:

***
import logging
logger = logging.getLogger(__name__)

import lib.biblioteca_filme as bf

def test_descriere():

    descriere = bf.actiune_matrix()
    if descriere:
        logger.info(f"Descrierea filmului este: {descriere}")
        assert True
    else:
        logger.error(f"Nu exista nicio descriere pentru acest film...")
        assert False

def test_distributie():
    distributie = bf.distributie_matrix()

    if distributie:
        logger.info(f"Distributia filmului: \n{distributie}")
        assert True
    else:
        logger.error(f"Nu exista informatii legate de distributie...")
        assert False 
***
![teste_jenkins](https://github.com/Raluca93/Curs_VCGJ_24_filme/assets/152555998/9ce6c366-f355-443c-b384-26f9f86911e7)

