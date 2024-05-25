import random


# Function to get a random fun fact
def get_random_fun_fact():
    fun_facts = [
        "The role of Bilbo Baggins was originally offered to Martin Freeman, but due to scheduling conflicts, he initially turned it down. However, Peter Jackson rescheduled filming to accommodate Freeman's availability.",
        "The Hobbit trilogy features 266 days of principal photography, with additional filming taking place over 10 weeks each year from 2011 to 2013.",
        "Benedict Cumberbatch not only voiced Smaug but also performed the dragon's movements using motion capture technology.",
        "The three films used over 500,000 feet of fake hair, with wigs for the dwarves taking an average of six months to create.",
        "Many of the outdoor scenes were filmed in the picturesque landscapes of New Zealand, showcasing its stunning natural beauty."
    ]
    return random.choice(fun_facts)
