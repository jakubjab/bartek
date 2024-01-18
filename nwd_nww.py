
def nwd(a, b):
    while a != b:
        if a > b:
            print(f'{a} > {b}')
            a = a - b
        else:
            print(f'{b} > {a}')
            b = b - a
    return a

def nww(a, b):
    return a * b / nwd_j(a, b)

a = int(input("Podaj a:"))
if a <= 0:
    print('Liczba a musi być dodatnia')
    quit()

b = int(input("Podaj b:"))
if b <= 0:
    print('Liczba b musi być dodatnia')
    quit()

nwd = nwd(a, b)
nww = nww(a, b)

print(f'nwd({a}, {b}) = {nwd}')
print(f'nww({a}, {b}) = {nww}')
