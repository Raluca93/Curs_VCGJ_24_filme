import logging
logger = logging.getLogger(__name__)

import sys
sys.path.append('/home/andreichichi/Desktop/dir_Local_Git_AndreiChiran/app')

from app.lib import description
from app.lib import rating

def test_descriere():
    
    descriere = description.returneaza_descriere()
    if descriere:
        logger.info(f"Se genereaza urmatoarea descriere {descriere}")
        assert True
    else:
        logger.error(f"Nu s-a detectat nicio descriere.")
        assert False
    

def test_rating():
    
    rate = rating.returneaza_rating()

    if rate == "5/5":
        logger.info(f"Ratingul este cel asteptat:{rate}\n")
        assert True
    else:
        logger.error(f"Ratingul nu este cel asteptat:{rate}\n")
        assert False 