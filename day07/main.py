"""Day 7: The Treachery of Whales"""

with open('input.txt') as f:
    crabs = [int(n) for n in f.readline().split(',')]

print('part 1:', min(sum(abs(c-i) for c in crabs) for i in range(min(crabs), max(crabs))))
print('part 2:', min(sum((abs(c-i)*(abs(c-i)+1))/2 for c in crabs) for i in range(min(crabs), max(crabs))))
