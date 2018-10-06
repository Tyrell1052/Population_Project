

def organism_a():
    print("%4s%6s%12s" %
          ("Organism A:", "Week", "Population",))

    population = 50
    weeks = 0
    total_weeks = 0


   # print("%14s%15s" %
          #(total_weeks, population))

    while total_weeks < 260:
        print("%14s%10s" %
              (total_weeks, population))
        if weeks == 2:
            population = population - (population * .25)
            print(population)
        elif weeks == 4:
            population = population * 2
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
