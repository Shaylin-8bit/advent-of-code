def parse():
    with open("input.txt", "r") as fp:
        return (fp.readline().strip("\n"), {i.strip("\n").split(" -> ")[0]: i.strip("\n").split(" -> ")[1] for i in fp.readlines() if len(i) > 1})

def process(ctx, steps=10):
    start, formulas = ctx
    alpha = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
    nums = {i: 0 for i in formulas.keys()}
    for i in range(len(start)-1):
        nums[start[i:i+2]] += 1
        alpha[start[i]] += 1
    alpha[start[-1]] += 1
    for i in range(steps):
        tmp = dict(nums)
        for key in nums.keys():
            if nums[key]:
                tmp[key] -= nums[key]
                t = formulas[key]
                tmp[key[0]+t] += nums[key]
                tmp[t+key[1]] += nums[key]
                alpha[t] += nums[key]
        nums = tmp
    nums = [i for i in alpha.values() if i]
    return max(nums) - min(nums)

print(process(parse(), 10))
print(process(parse(), 40))