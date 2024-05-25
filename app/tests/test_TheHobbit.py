import logging
logger = logging.getLogger(__name__)

import sys
sys.path.append('/home/andreichichi/Desktop/dir_Local_Git_AndreiChiran/app')

from app.lib import funfact_TheHobbit
from app.lib import year_TheHobbit



def test_descriere():
    
    fun_facts = [
        "The role of Bilbo Baggins was originally offered to Martin Freeman, but due to scheduling conflicts, he initially turned it down. However, Peter Jackson rescheduled filming to accommodate Freeman's availability.",
        "The Hobbit trilogy features 266 days of principal photography, with additional filming taking place over 10 weeks each year from 2011 to 2013.",
        "Benedict Cumberbatch not only voiced Smaug but also performed the dragon's movements using motion capture technology.",
        "The three films used over 500,000 feet of fake hair, with wigs for the dwarves taking an average of six months to create.",
        "Many of the outdoor scenes were filmed in the picturesque landscapes of New Zealand, showcasing its stunning natural beauty."
    ]

    descriere = funfact_TheHobbit.get_random_fun_fact()

    if descriere in fun_facts:
        logger.info(f"Se genereaza urmatorul funfact {descriere}")
        print(f"Se genereaza urmatorul funfact {descriere}")
        assert True
    else:
        logger.error(f"Nu s-a detectat un fun fact valid.")
        print(f"Nu s-a detectat un fun fact valid.")
        assert False





def test_year():
    
    year = year_TheHobbit.get_release_year()

    if year == "The movie The Hobbit was released in 2012, with two more movies following in the next 2 years.":
        logger.info(f"Descrierea pentru an este cea dorita:{year}\n")
        print(f"DDescrierea pentru an este cea dorita:{year}\n")
        assert True
    else:
        logger.error(f"Descrierea pentru an nu este buna:{year}\n")
        print(f"Descrierea pentru an nu este buna::{year}\n")
        assert False 