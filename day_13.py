def parse(fn):
    with open(fn, "r") as fp:
        dots = []
        folds = []
        a = fp.readline()
        while (a):
            if (a[0] != "f" and len(a) > 1):
                dots.append(tuple(int(i) for i in a.strip("\n").split(",")))
            elif (len(a) > 1):
                a = a.strip("\n").strip("fold along ").split("=")
                folds.append((a[0], int(a[1])))
            a = fp.readline()
        return (tuple(dots), tuple(folds))

def transpose(lst):
    new = [[None for i in range(len(lst))] for j in range(len(lst[0]))]
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            new[j][i] = lst[i][j]
    return new

class Paper():
    def __init__(self, points):
        sze = (max([i[0] for i in points])+1, max([i[1] for i in points])+1)
        self.grid = [[0 for i in range(sze[0])] for j in range(sze[1])]
        for point in points:
            self.grid[point[1]][point[0]] = 1

    def fold(self, instructions):
        def helper(grid, point):
            lst1 = [line for line in grid[:point]]
            lst2 = [line for line in grid[point+1:]]
            mod = lst1 if len(lst1) < len(lst2) else lst2
            tar = lst1 if mod != lst1 else lst2
            for i in range(len(mod)):
                for j in range(len(mod[i])):
                    tar[-(i+1)][j] += mod[i][j]
            return tar
        
        for inst in instructions:
            self.grid = transpose(helper(transpose(self.grid), inst[1])) if inst[0] == 'x' else helper(self.grid, inst[1])

    def points(self):
        return sum([sum([True if point else False for point in line]) for line in self.grid])

    def __repr__(self):
        return "\n".join(["".join(['#' if i else " " for i in line]) for line in self.grid])

parsed = parse("input.txt")
paper = Paper(parsed[0])
paper.fold([parsed[1][0]])
print(paper.points())

paper.fold(parsed[1][1:])
print(paper)