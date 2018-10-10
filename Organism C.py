
def organism_c():

    # declaring population and week_counter variables
    population = 1000
    week_counter = 0

    # this will start the while loop to run until total_weeks is <= 260 weeks (5 years if counted in weeks)
    while week_counter <= 260:

        if week_counter % 1 == 0:  # this if statement handles the decrease by 25% every two weeks
            population = population - (population * .13)
            week_counter += 1

            if week_counter % 4 == 0:  # this is for when weeks == 4 the population will increase
                population = population + (population * .75)
                week_counter += 1

        if population > 1000000 or population < 1:
            print("Organism C will reach", format(population, ".0f"), "by week", week_counter)
            break
        #print(population)

organism_c()