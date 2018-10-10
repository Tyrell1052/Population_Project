def organism_b():
    # declaring population and week_counter variables
    population = 250
    week_counter = 0
    year = 0




    # this will start the while loop to run until total_weeks is <= 260 weeks (5 years if counted in weeks)
    while week_counter <= 260:

        if week_counter % 1 == 0:  # this if statement handles the decrease by 25% every two weeks
            population = population - (population * .25)
            week_counter += 1

            if week_counter % 4 == 0:  # this is for when weeks == 4 the population will increase
                population = population * 3
                week_counter += 1

        if week_counter == 52 or 104 or 156 or 208 or 260:
            year += 1

        if year == 1 or 2 or 3 or 4 or 5:
            print("Organisms population", population, "at year", year)

        if year == 5:
            break

        if population > 1000000 or population < 1:
            print("Organism B will reach", format(population, ".0f"), "by week", week_counter)
            break
        # print(population)



organism_b()