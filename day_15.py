import os
from datetime import datetime

def parse():
    with open("input.txt", "r") as fp:
        a = fp.readlines()
        return [[Node(int(a[j][i]), (j, i)) for i in range(len(a[j].strip("\n")))] for j in range(len(a))]

def transpose(lst):
    new = [[None for i in range(len(lst))] for j in range(len(lst[0]))]
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            new[j][i] = lst[i][j]
    return new

def clear():
    os.system("cls")

class Node():
    def __init__(self, val, pos):
        self.val = val
        self.trk = False
        self.dst = None
        self.con = None
        self.pos = pos
        
    def __repr__(self):
        return f"val: {self.val}, pos: {self.pos}, trk: {self.trk}, dst: {self.dst}, con: {self.con}"

class Dijkstra():
    def __init__(self, ctx):
        self.grid = ctx

    def print_tracked(self):
        print("\n".join(["".join(["#" if j.trk else "_" for j in i]) for i in self.grid]))

    def __repr__(self):
        return "\n".join(["".join([str(j.val) for j in i]) for i in self.grid])

    def print_trail(self, trail):
        print()
        for i in self.grid:
            for j in i:
                if j in trail:
                    print("#", end="")
                else:
                    print("_", end="")
            print()

    def adjacent(self, pos):
        y, x = pos
        if x > 0:
            if not self.grid[y][x-1].trk:
                return True
        if y > 0:
            if not self.grid[y-1][x].trk:
                return True
        if x < len(self.grid[0])-1:
            if not self.grid[y][x+1].trk:
                return True
        if y < len(self.grid)-1:
            if not self.grid[y+1][x].trk:
                return True
        return False

    def percent_tracked(self):
        return sum([len([i for i in j if i.trk]) for j in self.grid])/(len(self.grid)*len(self.grid[0])) * 100

    def grow(self, times):
        def helper():
            width = len(self.grid[0])
            height = len(self.grid)
            sub_grid = []
            for i in range(height):
                sub_grid.append([Node(self.grid[i][j].val, self.grid[i][j].pos) for j in range(len(self.grid[i]))])
            
            for i in range(times-1):
                for j in range(height):
                    for k in range(width):
                        r = list(range(1, 10))
                        val = (sub_grid[j][k].val + (i))
                        val = r[val%9]
                        pos = (0, 0)
                        self.grid[j].append(Node(val, pos))
        
        helper()
        self.grid = transpose(self.grid)
        helper()
        self.grid = transpose(self.grid)

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j].pos = (i, j)

    def traverse(self, root, tar):
        y, x = root
        root = self.grid[y][x]
        root.dst = 0
        root.trk = True
        x, y = tar
        tar = self.grid[y][x]
        tracked = [root]
        percent = 0
        print(f"{percent}% of board tracked at {datetime.now()}")
        while tar not in tracked:
            n_percent = self.percent_tracked()
            if n_percent > percent:
              print(f"{n_percent}% of board tracked at {datetime.now()}")
              percent = n_percent
            tracked = [i for i in tracked if self.adjacent(i.pos)]
            adjacent = []
            for node in tracked:
                y, x = node.pos
                if x > 0:
                    if not self.grid[y][x-1].trk:
                        adjacent.append(((y, x), self.grid[y][x-1]))
                if y > 0:
                    if not self.grid[y-1][x].trk:
                        adjacent.append(((y, x), self.grid[y-1][x]))
                if x < len(self.grid[0])-1:
                    if not self.grid[y][x+1].trk:
                        adjacent.append(((y, x), self.grid[y][x+1]))
                if y < len(self.grid)-1:
                    if not self.grid[y+1][x].trk:
                        adjacent.append(((y, x), self.grid[y+1][x]))
            closest = adjacent[0]
            for i in adjacent:
                con1 = self.grid[closest[0][0]][closest[0][1]]
                con2 = self.grid[i[0][0]][i[0][1]]
                if i[1].val + con2.dst < closest[1].val + con1.dst:
                    closest = i
            closest[1].con = closest[0]
            closest = closest[1]
            con3 = self.grid[closest.con[0]][closest.con[1]]
            closest.dst = con3.dst + closest.val
            closest.trk = True
            tracked.append(closest)
        trail = [tar]
        while trail[-1].con:
            y, x = trail[-1].con
            trail.append(self.grid[y][x])
        self.print_trail(trail)
        return (tar, trail)
 

a = Dijkstra(parse())
a.grow(5)
start = datetime.now()
b = a.traverse((0, 0), (499, 499)) # 393
end = datetime.now()
print(f"Started at: {start}")
print(f"Ended at:   {end}")
print(b[0])
