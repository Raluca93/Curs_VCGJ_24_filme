import logging
logger = logging.getLogger(__name__)

import sys
sys.path.append('/home/andreichichi/Desktop/Curs_VCGJ_24_filme-main-Mitrut-Badea/app')

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

    if distributie == "At the 87th Academy Awards, Interstellar received nominations for Best Original Score, Best Production Design, Best Sound Editing, and Best Sound Mixing, and won Best Visual Effects.":
        logger.info(f"Ratingul este cel asteptat:{distributie}\n")
        print(f"Ratingul este cel asteptat:{distributie}\n")
        assert True
    else:
        logger.error(f"Ratingul nu este cel asteptat:{distributie}\n")
        print(f"Ratingul nu este cel asteptat:{distributie}\n")
        assert False 
