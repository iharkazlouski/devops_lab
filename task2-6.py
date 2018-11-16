import re


def func(line):
    mo = re.match(r'(%s)(?P<oper>[-/\*\+])(%s)=(%s)$' % ("?P<n1>-?\\d+",
                  "?P<n2>-?\\d+", "?P<n3>-?\\d+"), line)
    if len(line) <= 100 and mo:
        n1 = int(mo.groupdict()['n1'])
        n2 = int(mo.groupdict()['n2'])
        n3 = int(mo.groupdict()['n3'])
        if max(n1, n2, n3) < 30000 and min(n1, n2, n3) > - 30000:
            oper = mo.groupdict()['oper']
            if oper == "/" and n2 == 0:
                print("NO")
            else:
                def m(x, y):
                    return x * y

                def d(x, y):
                    return x / y

                def s(x, y):
                    return x + y

                def p(x, y):
                    return x - y
                do = {"*": m, "/": d, "+": s, "-": p}
                if n3 == do[oper](n1, n2):
                    print("YES")
                else:
                    print("NO")
    else:
        print("Error")


line = str(input("Input line like 3+2=5:"))
func(line)
