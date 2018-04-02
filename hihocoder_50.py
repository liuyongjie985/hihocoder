def myprint(word_arv, i, temp_arv, result_map_arv):
    for x in word_arv:
        if not result_map_arv.has_key(x):
            result_map[x] = 1
            temp_arv = temp_arv + x
            i += 1
            if i % 5 == 0:
                print temp_arv
                temp_arv = ""
    return i, temp_arv


while True:
    try:
        word = raw_input()
        my_map = {}

        my_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                   'V',
                   'W', 'X', 'Y', 'Z']
        for i, x in enumerate(word):
            if x == 'J':
                word = word[:i] + 'I' + word[i + 1:]

            my_map[i] = 1

        result_map = dict()
        # j = 0
        # while j < 5:
        temp = ""
        i = 0

        i, temp = myprint(word, 0, temp, result_map)

        i, temp = myprint(my_list, i, temp, result_map)



    except EOFError:
        break
