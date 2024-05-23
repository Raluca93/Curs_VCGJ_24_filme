import logging
import pytest
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append("../")

from lib import biblioteca_filme as filme

def test_recenzii_film():
    recenzii = filme.recenzii_film()

    if "a remarcat că filmul are o structură frenetică și explozivă" in recenzii:
        logger.info(f"Functia recenzii_film() functioneaza corect:\n")
        assert True
    else:
        logger.error(f"Functia recenzii_film() NU functioneaza corect:\n{recenzii}")
        assert False

    if "reflectă aceste opinii mixte, cu scoruri medii care indică" in recenzii:
        logger.info(f"Functia recenzii_film() functioneaza corect:\n")
        assert True
    else:
        logger.error(f"Functia recenzii_film() NU functioneaza corect:\n{recenzii}")
        assert False

    if "a fost mai critic, menționând că filmul împrumută prea" in recenzii:
        logger.info(f"Functia recenzii_film() functioneaza corect:\n")
        assert True
    else:
        logger.error(f"Functia recenzii_film() NU functioneaza corect:\n")
        assert False

    if "a subliniat că filmul reușește să mențină interesul publicului printr-o combinație" in recenzii:
        logger.info(f"Functia recenzii_film() functioneaza corect:\n")
        assert True
    else:
        logger.error(f"Functia recenzii_film() NU functioneaza corect:\n")
        assert False

def test_descriere_film():
    descriere = filme.descriere_film()

    if "Acțiunea filmului se desfășoară în New York și continuă să-l urmărească pe John McClane" in descriere:
        logger.info(f"Functia descriere_film() functioneaza corect:\n")
        assert True
    else:
        logger.error(f"Functia descriere_film() NU functioneaza corect:\n")
        assert False
        
