import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append("../")

from lib import biblioteca_filme as filme

def test_recenzii_film():
    recenzii = filme.recenzii_film()

    if "Its sense of humor is more sly, more sophisticated and more interesting than most PG-13" in recenzii:
        logger.info(f"Functia recenzii_film() functioneaza corect")
        assert True
    else:
        logger.error(f"Functia recenzii_film() NU functioneaza corect")
        assert False

def test_descriere_film():
    descriere = filme.descriere_film()

    if "Filmul a fost apreciat pentru povestea sa captivantă" in descriere:
        logger.info(f"Functia descriere_film() functioneaza corect")
        assert True
    else:
        logger.error(f"Functia descriere_film() NU functioneaza corect")
        assert False
