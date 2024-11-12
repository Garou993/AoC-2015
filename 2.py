f = open('inputs/2.txt')

ans = 0
for s in f.readlines():
    s = sorted(list(map(int, s.split('x'))))
    area = 0
    for i in range(2, -1, -1):
        if i == 1:
            area += 3*s[i]*s[i-1]
            continue
        area += 2*s[i]*s[i-1]
    ans += area
print(ans)