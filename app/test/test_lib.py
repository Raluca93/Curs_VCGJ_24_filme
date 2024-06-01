import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append("/home/ion/proiect/Curs_VCGJ_24_filme/app")
from lib import lib_filme as filme



def test_descriere_film():
    descriere = filme.descriere_film()

    if "Toei Animation" in descriere:
        logger.info(f"Functia descriere_film functioneaza corect: {descriere}")
        assert True
    else:
        logger.error(f"Functia descriere_film NU functioneaza corect: {descriere}")
        assert False

def test_comentari():
    comentari = filme.comentari()

    if "Watched it today" in comentari:
        logger.info(f"Functia quotes functioneaza corect:\n{comentari}")
        assert True
    else:
        logger.error(f"Functia quotes NU functioneaza corect:\n{comentari}")
        assert False 
