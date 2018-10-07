def organism_b():

    population = 250
    weeks = 0
    total_weeks = 0

    while total_weeks < 260:

        if weeks == 2:
            population = population - (population * .25)

        elif weeks == 4:
            population = population * 3
            print("%14s" % format(population, ".0f"))
            weeks = 0
        elif population > 1000000:
            print("Organism B will take", total_weeks, "weeks to reach 1 million organisms.")
            break
        elif population < 0:
            print("Organism B will take", total_weeks, "weeks until species reaches 0 organisms. ")
            break
        weeks += 1
        total_weeks += 1

        #print("%0s" % total_weeks)


organism_b()
