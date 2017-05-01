def minsteps(n) :
    memo = [0] * (n + 1)

    for i in range(1, n + 1) :
        if 1 < i :
            memo[i] = 1 + memo[i - 1]
            if i % 2 == 0 :
                memo[i] = min(memo[i], 1 + memo[i // 2])
            if i % 3 == 0 :
                memo[i] = min(memo[i], 1 + memo[i // 3])
        else :
            memo[i] = 0

    return memo[i]

print("minsteps(1) :", minsteps(1))
print("minsteps(2) :", minsteps(2))
print("minsteps(3) :", minsteps(3))
print("minsteps(4) :", minsteps(4))
print("minsteps(7) :", minsteps(7))
print("minsteps(10) :", minsteps(10))
print("minsteps(23) :", minsteps(23))
print("minsteps(237) :", minsteps(237))
print("minsteps(317) :", minsteps(317))
print("minsteps(514) :", minsteps(514))
print("minsteps(997) :", minsteps(997))
print("minsteps(998) :", minsteps(998))