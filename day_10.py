def parse():
    with open("input.txt", "r") as fp:
        return [i.strip('\n') for i in fp.readlines()]

class Node():
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

class Stack():
    def __init__(self, val=None):
        self.head = Node(val) if val else None

    def push(self, val):
        self.head = Node(val, self.head)

    def peak(self):
        return self.head.val if self.head else None

    def pop(self):
        if self.head:
            val = self.head.val
            self.head = self.head.nxt if self.head.nxt else None
            return val

def process(lines):
    corruption = 0
    incomplete = []
    for line in lines:
        stack = Stack()
        corrupted = False
        for bracket in line:
            if bracket in "([{<":
                stack.push(")]}>"["([{<".index(bracket)])
            else:
                if bracket == stack.peak():
                    stack.pop()
                else:
                    corruption += {')': 3, ']': 57, '}': 1197, '>': 25137}[bracket]
                    corrupted = True
                    break
        if not corrupted:
            tmp = 0
            while (stack.peak()):
                tmp *= 5
                tmp += [')', ']', '}', '>'].index(stack.pop()) + 1
            incomplete.append(tmp)
    incomplete.sort()
    return (corruption, incomplete[int(len(incomplete) / 2)])

print(process(parse()))
