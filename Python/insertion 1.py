input()
val = map(int, input().strip().split())
val = list(val)

for i in val:
    for idx, x in enumerate(val):
        temp = 0
        if x < val[idx-1] and idx-1 >= 0:
            val[idx] = val[idx-1]
            print(' '.join(map(str, val)))
            val[idx-1] = x
print(' '.join(map(str, val)))