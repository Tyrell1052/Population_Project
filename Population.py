""""
Program: Population.py
Author: Tyrell Robbins
This program will Simulate the life cycle of 3 Organisms
based on growth rates, death rates and predictions over
the course of 5 years """


# Display headers for table

# define Organism A in a function
def organism_a():
    # Display headers for table
    print("%4s%14s" %
          ("Year:", "Organism A:"))
    # starting variables for population, weeks and total_weeks
    population = 50
    weeks = 0
    total_weeks = 0
    # this will start the while loop to run until total_weeks is <= 260 weeks (5 years if counted in weeks)
    while total_weeks <= 260:

        if weeks == 2:  # this if statement handles the decrease by 25% every two weeks
            population = population - (population * .25)

        elif weeks == 4:  # this is for when weeks == 4 the population will increase
            population = population * 2
            print("%12s" % format(population, ".0f"))
            weeks = 0  #this sets weeks back to 0 so when the loop continues to go through it can decrease and increase the population

        elif population > 1000000:  # this will print only if the population is greater then 1000000
            print("Organism A will take", total_weeks, "weeks to reach 1 million organisms.")
            break
        elif population < 0:  # this will print if the population is less than 0
            print("Organism A will take", total_weeks, "weeks until species reaches 0 organisms. ")
            break

        weeks += 1  # this adds 1 to weeks each time the while loop iterates
        total_weeks += 1  # this adds 1 to weeks each time the while loop iterates

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