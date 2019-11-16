import allEnums


class Liqour:
    def __init__(self, name, idx):
        self.name = name.lower().strip()
        self.id = idx
        
class Mixer:
    def __init(self,name, idx):
        self.name = name.lower().strip()
        self.id = idx


class RecipePart:
    def __init__(self, liquid, volume):
        self.liquid = liquid
        self.volume = volume

class Recipe:
    def __init__(self, listOfParts, sequential=False):
        self.listOfParts = listOfParts
        self.sequential = sequential

    def addPart(self,part):
        flag = True
        for partX in self.listOfParts:
            if partX.liquid.name == part.liquid.name:
                partX.volume += part.volume
                flag = False
        if flag:
            self.listOfParts.append(part)

    def copy(self):
        return Recipe(self.listOfParts, sequential=self.sequential)

    def removePart(self,part, allLiquid = True):
        for partX in self.listOfParts:
            if partX.liquid.name == part.liquid.name:
                if allLiquid:
                    self.listOfParts.remove(partX)
                else:
                    partX.volume -= part.volume

    def replace(self, part2Remove, part2Add):
        self.removePart(part2Remove)
        self.addPart(part2Add)
    #TODO print function


    #TODO getNumRecipeParts()



class Drink:
    def __init__(self, name, volume):
        self.name = name 
