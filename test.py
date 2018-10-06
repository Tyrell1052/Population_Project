
print("%4s%6s%12s%22s" %
      ("Organism A:", "Week", "Population", "1 million organisms",))

population_a = 50
weeks_a = 0
weeks_in_years_a = 0

#print("%10s%15s" %
     # (weeks_in_years_a, population_a))

while weeks_in_years_a < 260:
    print(weeks_a, weeks_in_years_a)
    if weeks_a == 2:
        population_a = population_a - (population_a * .25)
        print("%25s" % population_a)
    elif weeks_a == 4:
        population_a = population_a * 2
        print(population_a)
        weeks_a = 0
    elif population_a > 1000000:
        print("Organism A will take",weeks_in_years_a,"weeks to reach 1 million organisms")
        break
    weeks_a += 1
    weeks_in_years_a += 1



