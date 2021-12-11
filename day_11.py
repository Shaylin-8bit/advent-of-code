def parse():
    with open("input.txt", "r") as fp:
        return [[int(i) for i in j if i != '\n'] for j in fp.readlines()]

class Octopus():
    def __init__(self, energy):
        self.energy = energy
        self.can_flash = True

    def __str__(self):
        return str(self.energy)

    def increment(self):
        if self.can_flash:
            if self.energy < 9:
                self.energy += 1
                return False
            
            else:
                self.energy = 0
                self.can_flash = False
                return True
    
    def reset(self):
        self.can_flash = True

class Octopi():
    def __init__(self, levels):
        self.map = [[Octopus(i) for i in j] for j in levels]

    def __str__(self):
        return "\n".join(["".join([str(i) for i in j]) for j in self.map])

    def reset(self):
        for i in self.map:
            for j in i:
                j.reset()
        
    def flash(self, x, y):
        result = 1
        if x > 0:
            if self.map[y][x-1].increment():
                result += self.flash(x-1, y)

        if x < len(self.map[y])-1:
            if self.map[y][x+1].increment():
                result += self.flash(x+1, y)

        if y > 0:
            if self.map[y-1][x].increment():
                result += self.flash(x, y-1)

        if y < len(self.map)-1:
            if self.map[y+1][x].increment():
                result += self.flash(x, y+1)

        if x > 0:
            if y > 0:
                if self.map[y-1][x-1].increment():
                    result += self.flash(x-1, y-1)

            if y < len(self.map)-1:
                if self.map[y+1][x-1].increment():
                    result += self.flash(x-1, y+1)

        if x < len(self.map[y])-1:
            if y > 0:
                if self.map[y-1][x+1].increment():
                    result += self.flash(x+1, y-1)

            if y < len(self.map)-1:
                if self.map[y+1][x+1].increment():
                    result += self.flash(x+1, y+1)
        
        return result

    def increment(self, steps=1):
        result = 0
        for step in range(steps):
            self.reset()
            for y in range(len(self.map)):
                for x in range(len(self.map[y])):
                    if self.map[y][x].increment():
                        result += self.flash(x, y)
        return result

    def synchronize(self):
        result = 0
        while (sum([sum([i.energy for i in j]) for j in self.map])) > 0:
            self.increment()
            result += 1
        return result

test = [
    [5,4,8,3,1,4,3,2,2,3],
    [2,7,4,5,8,5,4,7,1,1],
    [5,2,6,4,5,5,6,1,7,3],
    [6,1,4,1,3,3,6,1,4,6],
    [6,3,5,7,3,8,5,4,7,8],
    [4,1,6,7,5,2,4,6,4,5],
    [2,1,7,6,8,4,1,7,2,1],
    [6,8,8,2,8,8,1,1,3,4],
    [4,8,4,6,8,4,8,5,5,4],
    [5,2,8,3,7,5,1,5,2,6]
]

print(Octopi(test).increment(100))    # 1656 
print(Octopi(test).synchronize())     # 195
print(Octopi(parse()).increment(100)) # 1634
print(Octopi(parse()).synchronize())