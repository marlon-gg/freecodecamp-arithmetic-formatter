def arithmetic_arranger(*args):
    ops = []
    if len(args[0]) > 5:
        return "Error: Too many problems."
    else:
        for p in args[0]:
            splitted = p.split(" ")
            if str(splitted[0]).isdigit() and str(splitted[2]).isdigit():
                if len(str(splitted[0])) <= 4 and len(str(splitted[2])) <= 4:
                    if splitted[1] == "+" or splitted[1] == "-":
                        biggest = len(str(splitted[0])) if len(str(splitted[0])) > len(str(splitted[2])) else len(str(splitted[2]))
                        space = " "
                        separator_sign = "-"
                        second = splitted[1]+space+(space*(biggest - (len(splitted[2]))))+splitted[2]
                        first = space*(len(second)-len(splitted[0]))+splitted[0]
                        result = str(eval(p))
                        opr = [first, second, separator_sign * (len(second))]
                        if len(args) > 1 and args[1]:
                            opr.append(space*(len(second)-len(result))+result)
                        ops.append(opr)
                    else:
                        return "Error: Operator must be '+' or '-'."
                else:
                    return "Error: Numbers cannot be more than four digits."
            else:
                return "Error: Numbers must only contain digits."
    out = ""
    for v in zip(*ops):
        for t in v:
            out += t+"    "
        out = out.rstrip(" ")
        out += "\n"
    out = out.rstrip("\n")
    return out
