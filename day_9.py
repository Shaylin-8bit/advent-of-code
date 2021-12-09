def parse():
    with open("input.txt", "r") as fp:
        result = []
        a = fp.readline()
        while (a):
            result.append([int(i) for i in a.strip('\n')])
            a = fp.readline()
    return result

class Point():
    def __init__(self, val):
        self.val = val
        self.key = "#"

class Cave():
    def __init__(self, ctx):
        self.map = [[Point(j) for j in i] for i in ctx]
    
    def basin_sizes(self):
        key = 0
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                point = self.map[i][j]
                if point.val != 9 and point.key == '#':
                    points = []
                    y = i
                    x = j
                    while point.key == '#':
                        points.append(point)
                        if x > 0: 
                            if self.map[y][x-1].val < point.val:
                                point = self.map[y][x-1]
                                x-=1
                                continue
                        if x < len(self.map[y])-1:
                            if self.map[y][x+1].val < point.val:
                                point = self.map[y][x+1]
                                x+=1
                                continue
                        if y > 0:
                            if self.map[y-1][x].val < point.val:
                                point = self.map[y-1][x]
                                y-=1
                                continue
                        if y < len(self.map)-1:
                            if self.map[y+1][x].val < point.val:
                                point = self.map[y+1][x]
                                y+=1
                                continue
                        break
                    if point != 9:
                        if point.key == '#':
                            new = str(key)
                            key += 1
                            point.key = new
                        else:
                            new = point.key
                        for p in points:
                            p.key = new

        basins = [0 for i in range(key)]
        for i in self.map:
            for point in i:
                if point.key != '#':
                    basins[int(point.key)] += 1
        return basins
                        
def process_one(ctx):
    low_points = []
    for i in range(len(ctx)):
        for j in range(len(ctx[i])):
            point = ctx[i][j]
            y = i
            x = j
            while True:
                if x > 0: 
                    if ctx[y][x-1] < point:
                        point = ctx[y][x-1]
                        x-=1
                        continue
                if x < len(ctx[y])-1:
                    if ctx[y][x+1] < point:
                        point = ctx[y][x+1]
                        x+=1
                        continue
                if y > 0:
                    if ctx[y-1][x] < point:
                        point = ctx[y-1][x]
                        y-=1
                        continue
                if y < len(ctx)-1:
                    if ctx[y+1][x] < point:
                        point = ctx[y+1][x]
                        y+=1
                        continue
                break
            if point not in (9, -1):
                low_points.append(point)
                ctx[y][x] = -1
    return len(low_points) + sum(low_points)

def process_two(ctx):
    cave = Cave(ctx)
    basins = cave.basin_sizes()
    basins.sort()
    result = 1
    for i in basins[-3:]:
        result *= i
    return result

print(process_one(parse()))
print(process_two(parse()))
