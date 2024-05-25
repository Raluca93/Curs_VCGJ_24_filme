import sys
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


sys.path.append("../")

from lib import biblioteca_filme as filme

def test_recenzii_film():
    recenzii = filme.recenzii_film()

    if "«Inception» este un triumf al imaginației pure" in recenzii:
        logger.info(f"Functia recenzii_film() functioneaza corect:\n{recenzii}")
        assert True
    else:
        logger.error(f"Functia recenzii_film() NU functioneaza corect:\n{recenzii}")
        assert False

def test_descriere_film():
    descriere = filme.descriere_film()

    if "Filmul explorează conceptul de împărtășire a viselor" in descriere:
        logger.info(f"Functia descriere_film() functioneaza corect:\n{descriere}")
        assert True
    else:
        logger.error(f"Functia descriere_film() NU functioneaza corect:\n{descriere}")
        assert False
