def isSimilar(left, right):
    if len(left) != len(right):
        return False
    result_map = {}
    i = 0
    while i < len(left):
        temp = left[i] - right[i]
        if temp < 0:
            temp += 26
        if result_map.has_key(temp):
            result_map[temp] += 1
        else:
            result_map[temp] = 1
        i += 1
    if len(result_map) != 1:
        return False
    else:
        return True


def isInList(list_A, list_B):
    for x in list_A:
        if len(x) != len(list_B):
            continue
        i = 0
        sign = True
        while i < len(x):
            if x[i] != list_B[i]:
                sign = False
                break
            i += 1
        if sign == True:
            return True
    return False


N = int(raw_input())

str_list = []
for x in xrange(N):
    temp = raw_input()
    str_list.append(temp)

my_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
          'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
          'Z': 26}

result_list = []

for x in str_list:
    temp_num = list()
    for y in x:
        if y == ' ':
            continue
        temp_num.append(my_map[y])

    # temp_num = int(temp_str)

    if not isInList(result_list, temp_num):
        if len(result_list) == 0:
            result_list.append(temp_num)
        else:
            sign2 = 0
            for p in result_list:
                if isSimilar(p, temp_num):
                    sign2 = 1
                    break;
            if sign2 == 0:
                result_list.append(temp_num)

print len(result_list)
