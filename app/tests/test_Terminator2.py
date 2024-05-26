import logging
logger = logging.getLogger(__name__)

import sys
sys.path.append('/home/andreichichi/Desktop/Curs_VCGJ_24_filme-main-alexslavoiu/app')

from app.lib import descriere_film
from app.lib import distributie_film

def test_descriere():
    
    descriere = descriere_film.returneaza_descriere()
    if descriere:
        logger.info(f"Se genereaza urmatoarea descriere {descriere}")
        print(f"Se genereaza urmatoarea descriere {descriere}")
        assert True
    else:
        logger.error(f"Nu s-a detectat nicio descriere.")
        print(f"Nu s-a detectat nicio descriere.")
        assert False
    

def test_rating():
    
    distributie = distributie_film.returneaza_distributie()

    if distributie == "In the Year 1992, at the Academy Award, Terminator 2: Judgment Day received nominations for Best Cinematography and Best Film Editing , and won for Best Sound, Best Effects, Sound Effects Editing, Visual Effects and Best Makeup.":
        logger.info(f"Ratingul este cel asteptat:{distributie}\n")
        print(f"Ratingul este cel asteptat:{distributie}\n")
        assert True
    else:
        logger.error(f"Ratingul nu este cel asteptat:{distributie}\n")
        print(f"Ratingul nu este cel asteptat:{distributie}\n")
        assert False 
