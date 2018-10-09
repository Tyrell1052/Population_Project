""""
Program: Population.py
Author: Tyrell Robbins
This program will Simulate the life cycle of 3 Organisms
based on growth rates, death rates and predictions over
the course of 5 years """


# Define Functions for
# Display headers for table


def organism_a():
    print("%4s%14s" %
          ("Week:", "Organism A:"))

    population = 50
    weeks = 0
    total_weeks = 0

    while total_weeks < 260:

        if weeks == 2 or 4:
            population = population - (population * .25)

        if weeks == 4:
            population = population * 2
            print(population)
            #print("%12s" % format(population, ".0f"))
            weeks = 0

        if population > 1000000:
            print("Organism A will take", total_weeks, "weeks to reach 1 million organisms.")
            break

        if population == 0:
            print("Organism A will take", total_weeks, "weeks until species reaches 0 organisms. ")
            break

        weeks += 1
        total_weeks += 1

        print("%0s" % total_weeks)
 #---------------------------------------------------------------------------------------

def organism_b():

    print("%4s%14s" %
          ("Week:", "Organism B:"))

    population = 250
    weeks = 0
    total_weeks = 0

    while total_weeks < 260:

        if weeks == 2:
            population = population - (population * .25)

        elif weeks == 4:
            population = population * 3
            print("%12s" % format(population, ".0f"))
            weeks = 0
        elif population > 1000000:
            print("Organism B will take", total_weeks, "weeks to reach 1 million organisms.")
            break
        elif population < 0:
            print("Organism B will take", total_weeks, "weeks until species reaches 0 organisms. ")
            break
        weeks += 1
        total_weeks += 1

        print("%0s" % total_weeks)






print(organism_a(),organism_b())