def parse():
    with open("input.txt", "r") as fp:
        return [int(i) for i in fp.readline().split(",")]

def factorial_sum(num):
    a = num / 2
    return int((a * 2 + 1)*a) if num % 2 == 0 else int(a+1) * num

def process_one(crabs):
    l = max(crabs)
    fuel = 0
    for i in crabs:
        a = abs(-i)
        b = abs(i - l)
        fuel += (a if a > b else b)
    index = -1
    for i in range(min(crabs), l+1):
        tmp = 0
        for j in crabs:
            tmp += abs(j - i)
            if tmp > fuel: break
        if tmp < fuel:
            fuel = tmp
            index = i
    return (fuel, index)

def process_two(crabs):
    l = max(crabs)
    r =  range(min(crabs), l+1)
    fuel = 0
    for i in crabs:
        a = factorial_sum(abs(-i))
        b = factorial_sum(abs(i-l))
        fuel += a if a > b else b
    index = -1
    for i in r:
        tmp = 0
        for j in crabs:
            tmp += factorial_sum(abs(j-i))
            if tmp > fuel: break
        if tmp < fuel:
            fuel = tmp
            index = i
    return (fuel, index)

print(process_one(parse())) # 349769   @ 331
print(process_two(parse())) # 99540554 @ 479

test = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
print(process_one(test)) # 37  @ 2
print(process_two(test)) # 168 @ 5
