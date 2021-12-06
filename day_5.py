def parse(fn):
    lines = []
    with open(fn, "r") as fp:
        a = fp.readline()
        while (a):
            line = tuple([tuple([int(j) for j in i.strip().split(",")]) for i in a.strip("\n").split("->")])
            lines.append(line)
            a = fp.readline()
    return lines

def map(ctx):
    xlen, ylen = dimss(ctx)
    grid = [[0 for i in range(ylen)] for j in range(xlen)]
    for line in ctx:
        x1, y1 = line[0]
        x2, y2 = line[1]
        grid[x2][y2] += 1
        while (x1 != x2 or y1 != y2):
            grid[x1][y1] += 1
            if (x1 > x2): x1 -= 1 
            elif (x1 < x2): x1 += 1
            if (y1 > y2): y1 -= 1 
            elif (y1 < y2): y1 += 1
    return grid

limit = lambda ctx: [line for line in ctx if line[0][0] == line[1][0] or line[0][1] == line[1][1]]
dimss = lambda ctx: (max([max([point[0] for point in line]) for line in ctx])+1, max([max([point[1] for point in line]) for line in ctx])+1)
count = lambda grid: sum([sum([1 for point in line if point > 1]) for line in grid])

process_one = lambda ctx: count(map(limit(ctx)))
process_two = lambda ctx: count(map(ctx))

print(process_one(parse("input.txt"))) #7473
print(process_two(parse("input.txt"))) #24164
