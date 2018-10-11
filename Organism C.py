
def organism_c():

    # declaring population and week_counter variables
    population = 1000
    week_counter = 0

    # this will start the while loop to run until total_weeks is <= 260 weeks (5 years if counted in weeks)
    while week_counter <= 520:
        week_counter += 1
        if week_counter % 1 == 0:  # this if statement handles the decrease by 25% every two weeks
            population = population - (population * .13)

            if week_counter % 4 == 0:  # this is for when weeks == 4 the population will increase
                population = population + (population * .75)

        if week_counter == 52 or week_counter == 104 or week_counter == 156 or week_counter == 208\
                or week_counter ==260 or week_counter == 312 or week_counter == 364 or week_counter == 416\
                or week_counter == 468 or week_counter == 520 or week_counter == 624 or week_counter == 676\
                or week_counter == 728 or week_counter == 780 or week_counter == 832 or week_counter == 884\
                or week_counter == 936 or week_counter == 936 or week_counter == 988 or week_counter == 1040:
            print("Organisms population", format(population, ".0f"), "at year", week_counter)

        if population > 1000000 or population < 1:
            print("Organism C will reach", format(population, ".0f"), "by week", week_counter)
            break


organism_c()