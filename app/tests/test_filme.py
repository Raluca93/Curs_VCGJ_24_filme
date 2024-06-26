import logging
logger = logging.getLogger(__name__)

import lib.biblioteca_filme as bf

def test_actiune():

    actiune = bf.actiune_iron_man()
    if actiune:
        logger.info(f"Actiunea filmului este: {actiune}")
        assert True
    else:
        logger.error(f"Nu exista nicio descriere pentru acest film...")
        assert False

def test_distributie():
    distributie = bf.distributie_iron_man()

    if distributie:
        logger.info(f"Distributia filmului: \n{distributie}")
        assert True
    else:
        logger.error(f"Nu exista informatii legate de distributie...")
        assert False 
