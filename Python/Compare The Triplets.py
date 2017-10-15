def solve(alice, bob):
    val = [0, 0]
    for ali, bo in zip(alice, bob):
        if ali > bo:
            val[0] += 1
        elif bo > ali:
            val[1] += 1
    val = map(str, val)
    return ' '.join(val)