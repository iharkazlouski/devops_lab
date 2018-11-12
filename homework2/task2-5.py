n = int(input("Input number: "))
number = list(bin(n)[2:])
for i in range(len(number)):
    number[i] = str(1 - int(number[i]))
newnum = ''.join(number)
print(int(newnum, 2))
