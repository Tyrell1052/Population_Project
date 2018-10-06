""""
Program: Population.py
Author: Tyrell Robbins
This program will Simulate the life cycle of 3 Organisms
based on growth rates, death rates and predictions over
the course of 5 years """


# Define Functions for
# Display headers for table
print("%4s%6s%12s%22s" %
      ("Organism A:", "Week", "Population", "1 million organisms",))


def organism_a():

    population = 50
    weeks = 0
    total_weeks = 0


    print("%10s%15s" %
          (total_weeks, population))

    while total_weeks < 260:
        print(weeks, total_weeks)
        if weeks == 2:
            population = population - (population * .25)
            print(population)
        elif weeks == 4:
            population = population * 2
            print(population)
            weeks = 0
        elif population > 1000000:
            print("Organism A will take", total_weeks, "weeks to reach 1 million organisms.")
            break
        elif population == 0:
            print("Organism A will take", total_weeks, "weeks until species reaches 0 organisms. ")
            break
        weeks += 1
        total_weeks += 1


organism_a()


