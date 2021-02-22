def parking_exit(lst):
    moves = []
    i = len(lst)
    j = 0
    xpos = 0
    for x in lst[0]:
        if x == 2:
            xpos = j
            break
        else:
            j += 1

    for x in lst:
        if i == 1:
            move = len(x) - 1 - xpos
            if move > 0:
                moves += ["R%i" %move]
        else:
            k = 0
            stairs = 0
            for y in x:
                if y == 1:
                    stairs = k
                    break
                else:
                    k +=1
            move = stairs - xpos
            if move > 0:
                moves += ["R%i" %move, 1]
            elif move < 0:
                move = -move
                moves += ["L%i" %move]
            else:
                if type(moves[len(moves)-1]) == int:
                    moves[len(moves)-1] += 1
                else:
                    moves += [1]
            xpos += move
        i -= 1

    output = []
    for x in moves:
        if type(x) == int:
            x = "D%i" %x
            output += [x]
        else:
            output += [x]

    return output


lst = [
  [1, 0, 0, 0, 2],
  [0, 0, 0, 0, 0]
]
print(parking_exit(lst))