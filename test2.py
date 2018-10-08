
class Organism:

    def __init__(self, population):
        print("%4s%14s%14s%14s" %
              ("Year:", "Organism A:", "Organism B:", "Organism C"))

        self.population = population
        self.weeks = 0
        self.total_weeks = 0
        self.year = 0

        while self.total_weeks < 260:

            if self.total_weeks == 52 or 104 or 156 or 208 or 260:
                self.year += 1
            else:
                break


            if self.weeks == 2:
                self.population = self.population - (self.population * .25)

            elif self.weeks == 4:
                self.population = self.population * 2
                print("%12s" % format(self.population, ".0f"))
                return


            elif self.population > 1000000:
                print("Organism A will take", self.total_weeks, "weeks to reach 1 million organisms.")
                break

            elif self.population == 0:
                print("Organism A will take", self.total_weeks, "weeks until species reaches 0 organisms. ")
                break
            self.weeks += 1
            self.total_weeks += 1

            if self.year <= 5:
                print("%0s" % self.year)
            else:
                break
        return


#Organism("Organism A", "Organism B","Organism C")

Organism_A = Organism(50)
Organism_B = Organism(55)