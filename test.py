""""
Program: Population.py
Author: Tyrell Robbins
This program will Simulate the life cycle of 3 Organisms
based on growth rates, death rates and predictions over
the course of 5 years """

# import datetime for adding time in weeks and years

import datetime

# Adding today
WEEK = datetime.timedelta(weeks=1)


# Define Functions for
#def organism_a(population, weeks):

population = 50
weeks = 0

if weeks < 4:

    population = population * 2


elif weeks < 2:
    population = population *.25

elif weeks == 260:
    print(population)

else:
    weeks += 1
    print(weeks)

    #return (population,weeks)








#def organismB():
#    population = 250

#def organismC():
#    population = 1000


#print(startDate)


# main
#organism_a(50,10)
