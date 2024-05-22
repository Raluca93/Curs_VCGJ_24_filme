import logging
logger = logging.getLogger(__name__)

from app.lib import description_Dune
from app.lib import rating_Dune

def test_descriere_Dune():
    
    descriere = description_Dune.returneaza_descriere()
    if descriere:
        logger.info(f"Se genereaza urmatoarea descriere {descriere}")
        print(f"Se genereaza urmatoarea descriere {descriere}")
        assert True
    else:
        logger.error(f"Nu s-a detectat nicio descriere.")
        print(f"Nu s-a detectat nicio descriere.")
        assert False
    

def test_rating_Dune():
    
    rate = rating_Dune.returneaza_rating()

    if rate == "⭐⭐⭐⭐☆":
        logger.info(f"Ratingul este cel asteptat:{rate}\n")
        print(f"Ratingul este cel asteptat:{rate}\n")
        assert True
    else:
        logger.error(f"Ratingul nu este cel asteptat:{rate}\n")
        print(f"Ratingul nu este cel asteptat:{rate}\n")
        assert False 