def parse():
    with open("input.txt", "r") as fp:
        tmp = [int(i) for i in fp.readline().split(",")]
        return [tmp.count(i) for i in range(9)]

def pass_time(fishes, days):
    for i in range(days):
        tmp = [0 for i in range(len(fishes))]
        for j in range(len(fishes)):
            if j == 0:
                tmp[j-1] += fishes[j]
                tmp[6] += fishes[j]
            else:
                tmp[j-1] += fishes[j]
            
        fishes = list(tmp)
    return sum(fishes)

print(pass_time(parse(), 80))
print(pass_time(parse(), 256))
