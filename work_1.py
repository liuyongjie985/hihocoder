# 4 4 2 2
# 1 1 1 2


N, M, X, Y = (int(x) for x in raw_input().strip().split(' '))

A, B, C, D = (int(x) for x in raw_input().strip().split(' '))

total = 0


def algorithm(N, M, X, Y, next_A, next_B, total):
    temp = total + 1

    if X + next_A >= 1 and X + next_A <= N and Y + next_B >= 1 and Y + next_B <= M:
        temp = algorithm(N, M, X + next_A, Y + next_B, next_A, next_B, temp)

    return temp


# if X + next_C >= 1 and X + next_C <= N and Y + next_D >= 1 and Y + next_D <= M:
#     temp += algorithm(N, M, X + next_C, Y + next_D, next_A, next_B, next_C, next_D, 0)




left = algorithm(N, M, X, Y, A, B, 0)
right = algorithm(N, M, X, Y, C, D, 0)

print left + right - 1
