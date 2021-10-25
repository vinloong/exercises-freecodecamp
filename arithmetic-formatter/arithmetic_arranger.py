import re


def arithmetic_arranger(problems, display=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    sp = ' ' * 4
    length = 3
    if display:
        length = 4
    arithmetics = [''] * length
    for problem in problems:
        block = process(problem, display)
        if type(block) == str:
            return block
        else:
            for i, v in enumerate(arithmetics):
                arithmetics[i] = v + block[i] + sp
    arithmetic_arranger = ""
    for ari in arithmetics:
        arithmetic_arranger = arithmetic_arranger + ari[: -4] + '\n'
    return arithmetic_arranger[:-1]


def process(problem, display):
    numstrs = [i for i in re.split(' ', problem) if (len(str(i)) != 0)]
    if len(numstrs) != 3:
        return "error: more or less"
    if numstrs[1] not in ['+', '-']:
        return "Error: Operator must be '+' or '-'."
    if numstrs[0].isdigit() is False or numstrs[2].isdigit() is False:
        return "Error: Numbers must only contain digits."
    if len(numstrs[0]) > 4 or len(numstrs[2]) > 4:
        return "Error: Numbers cannot be more than four digits."
    length = max(len(numstrs[0]), len(numstrs[2])) + 2
    up = numstrs[0].rjust(length, ' ')
    down = numstrs[1] + numstrs[2].rjust(length - 1, ' ')
    line = "".rjust(length, '-')
    block = [up, down, line]
    if display:
        result = ''
        if '-' == numstrs[1]:
            result = str(int(numstrs[0]) - int(numstrs[2])).rjust(length, ' ')
        elif '+' == numstrs[1]:
            result = str(int(numstrs[0]) + int(numstrs[2])).rjust(length, ' ')
        else:
            return "Error: Operator must be '+' or '-'."
        block.append(result)
    return block
