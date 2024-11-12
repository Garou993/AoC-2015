from collections import Counter

f = open('inputs/1.txt')
counter = Counter(f.readline())

print(counter['('] - counter[')'])