import sys
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


sys.path.append("/home/cristi/Desktop/Curs_VCGJ_24_filme/app")

from lib import biblioteca_filme as filme

def test_recenzii_film():
    recenzii = filme.recenzii_film()

    if "bearfaceproductions" in recenzii:
        logger.info(f"Functia recenzii_film() functioneaza corect:\n")
        assert True
    else:
        logger.error(f"Functia recenzii_film() NU functioneaza corect:\n")
        assert False

def test_descriere_film():
    descriere = filme.descriere_film()

    if "Edd" in descriere:
        logger.info(f"Functia descriere_film() functioneaza corect:\n")
        assert True
    else:
        logger.error(f"Functia descriere_film() NU functioneaza corect:\n")
        assert False
