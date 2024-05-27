import logging
logger = logging.getLogger(__name__)

import lib.biblioteca_filme as bf

def test_actiune():

    actiune = bf.actiune_fg()
    if actiune:
        logger.info(f"Actiunea filmului: {actiune}")
        assert True
    else:
        logger.error(f"Nu exista paragraf despre actiune!")
        assert False

def test_distributie():
    distributie = bf.distributie_fg()

    if distributie:
        logger.info(f"Distribuția filmului: \n{distributie}")
        assert True
    else:
        logger.error(f"Nu exista paragraf legat de distributie!")
        assert False 
