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
