x = str(input())
sumi = 0
index = 0
out = [x, '-->']
while int(x) >= 10:
    for i in x:
        index += 1
        out += [i, '+']
        sumi += int(i)
        if len(x) == index:
            out[-1] = '='
            out += [str(sumi)]
            if int(sumi) >= 10:
                out += ['-->']
            x = str(sumi)
            sumi, index = 0, 0

print(*out)
