def organism(a,b,c):
    print("%4s%14s%14s%14s" %
          ("Year:", "Organism A:", "Organism B:", "Organism C"))

    population = 50
    weeks = 0
    total_weeks = 0
    year = 0

    while total_weeks < 260:

        if total_weeks == 52 or 104 or 156 or 208 or 260:
            year += 1
        else:
            break


        if weeks == 2:
            population = population - (population * .25)

        elif weeks == 4:
            population = population * 2
            print("%12s" % format(population, ".0f"))
            return


        elif population > 1000000:
            print("Organism A will take", total_weeks, "weeks to reach 1 million organisms.")
            break

        elif population == 0:
            print("Organism A will take", total_weeks, "weeks until species reaches 0 organisms. ")
            break
        weeks += 1
        total_weeks += 1

        if year <= 5:
            print("%0s" % year)
        else:
            break
    return

organism(1,2,c)