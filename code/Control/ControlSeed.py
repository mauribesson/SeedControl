class ControlSeed:
    def __init__(self):
        self.listSeeds = []

    def save_seed(self,  seed):
        self.listSeeds.append(seed)
        return seed

    def search_seed(self, name):
        for x in self.listSeeds:
            if x.get_name() == name:
                return x
        return None

    def list_seeds(self):
        for x in self.listSeeds:
            print("|"+str(x.get_type())+"|"+"|"+str(x.get_name())+"|"+"|"+str(x.get_time())+"|"+"|"+str(x.get_earth())+"|"+"|"+str(x.get_water())+"|"+"|"+str(x.get_nutrients())+"|"+"|"+str(x.get_chemical_fertilizer())+"|\n")

    def show_seed(self, x):
        print("|"+str(x.get_type())+"|"+"|"+str(x.get_name())+"|"+"|"+str(x.get_time())+"|"+"|"+str(x.get_earth())+"|"+"|"+str(x.get_water())+"|"+"|"+str(x.get_nutrients())+"|"+"|"+str(x.get_chemical_fertilizer())+"|\n")
pass



