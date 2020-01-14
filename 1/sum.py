def matematichka(n):
    if n > 1:
        summ = 0
        for count in range(n):
            summ += 1. / (2 ** count + 1)
        return summ
    else:
        print('n must be more then 1.')

print(matematichka(4))