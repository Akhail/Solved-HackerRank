M, N = map(int, input().strip().split(' '))
vec = [0 for _ in range(M+1)]
for _ in range(N):
    minus, maxim, value = map(int, input().strip().split(' '))
    vec[minus-1] += value
    vec[maxim] -= value

total = None
maximum = None
for x in vec:
    if total is None:
        total = x
    else:
        total += x
    if maximum is None:
        maximum = total
    elif maximum < total:
        maximum = total

print(maximum)