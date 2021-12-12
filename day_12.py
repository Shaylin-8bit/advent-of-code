def parse():
    with open("input.txt", "r") as fp:
        return [i.strip("\n") for i in fp.readlines()]

class Cave():
    def __init__(self, connections):
        segments = {}
        for i in connections:
            for j in i.split('-'):
                segments[j] = []
        for i in connections:
            i = i.split('-')
            segments[i[0]].append(i[1])
            segments[i[1]].append(i[0])
        self.segments = segments
    
    def map_cave(self, double=False, start="start", nogo=["start"]):
        result = 0
        for i in [j for j in self.segments[start] if j != "start"]:
            if i == "end": 
                result += 1
            elif i not in nogo:
                if i.islower():
                    result += self.map_cave(double, i, [*[j for j in nogo], i])
                else:
                    result += self.map_cave(double, i, nogo)
            elif double:
                result += self.map_cave(False, i, nogo)
        return result

print(Cave(parse()).map_cave())
print(Cave(parse()).map_cave(True))
