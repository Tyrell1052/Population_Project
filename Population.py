""""
Program: Population.py
Author: Tyrell Robbins
This program will Simulate the life cycle of 3 Organisms
based on growth rates, death rates and predictions over
the course of 5 years """

# import datetime for adding time in weeks and years

import datetime

# Adding today
weeks = datetime.timedelta(weeks=1)


# Define Functions for
def organism_a():
     while (weeks != 260):

        population = 50
        weeks = 0

        if weeks == 4:
            population * 2

        elif weeks == 2:
            population *.25

        elif weeks == 260:
            print(population)

        else:
            weeks += 1






#def organismB():
    startingPopulation = 250

#def organismC():
    StartingPopulation = 1000


#print(startDate)


# main
organism_a()