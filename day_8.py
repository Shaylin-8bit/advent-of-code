def parse():
    with open("input.txt", "r") as fp:
        result = []
        line = fp.readline()
        while (line):
            parts = line.split('|')
            result.append(tuple([tuple([i.strip() for i in parts[0].split()]), tuple([i.strip().strip("\n") for i in parts[1].split()])]))
            line = fp.readline()
    return tuple(result)

def same_chars(str1, str2):
    if len(str1) != len(str2): return False
    for i in range(len(str1)):
        if str1[i] not in str2: return False
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                str2 = str2[0:j] + "#" + str2[j+1:]
    return True

def decode(nums):
    lst = {}
    for i in nums:
        if len(i) == 2: lst['1'] = i
        if len(i) == 3: lst['7'] = i
        if len(i) == 4: lst['4'] = i
        if len(i) == 7: lst['8'] = i
    zne = [num for num in nums if len(num) == 6]
    for i in range(len(zne)):
        if lst['1'][0] not in zne[i] or lst['1'][1] not in zne[i]:
            lst['6'] = zne.pop(i)
            break
    cross = [i for i in lst['4'] if i not in lst['1']]
    for i in range(len(zne)):
        if cross[0] not in zne[i] or cross[1] not in zne[i]:
            lst['0'] = zne.pop(i)
            break
    lst['9'] = zne[0]
    ttf = [num for num in nums if len(num) == 5]
    for i in range(len(ttf)):
        if [i for i in lst['1'] if i not in lst['6']][0] not in ttf[i]:
            lst['5'] = ttf.pop(i)
            break
    for i in range(len(ttf)):
        if lst['1'][0] not in ttf[i] or lst['1'][1] not in ttf[i]:
            lst['2'] = ttf.pop(i)
            break
    lst['3'] = ttf[0]
    result = {}
    for i in lst.keys():
        result[lst[i]] = i
    return result

process_one = lambda lst: sum([len([num for num in line[1] if len(num) in (2, 3, 4, 7)]) for line in lst])

def process_two(lst):
    result = 0
    for line in lst:
        num_map = decode(line[0])
        nums = line[1]
        temp = ''
        for num in nums:
            for key in num_map.keys():
                if same_chars(num, key):
                    temp += num_map[key]
                    break
        result += int(temp)
    return result

print(process_one(parse()))
print(process_two(parse()))
