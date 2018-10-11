
def organism_a():

    # declaring population and week_counter variables
    population = 50
    week_counter = 0

    # this will start the while loop to run until weeks_counter is <= 260 weeks
    # (5 years if counted in weeks)
    while week_counter <= 520:
        week_counter += 1
        if week_counter % 2 == 0:  # this if statement handles the decrease by 25% every two weeks
            population = population - (population * .25)

            if week_counter % 4 == 0:  # this is for when weeks == 4 the population will increase
                population = population * 2

        if week_counter == 52 or week_counter == 104 or week_counter == 156 or week_counter == 208 or week_counter ==260 or week_counter == 312 or week_counter == 364 or week_counter == 416 or week_counter == 468 or week_counter == 520:
            print("Organisms population", format(population, ".0f"), "at year", week_counter // 52)

        if population > 1000000 or population < 1:
            print("Organism A will reach", format(population, ".0f"), "by week", week_counter)
            break


organism_a()