
def nwd_i(a, b):
    while b:
        a, b = b, a%b
    return a

a = int(input("Podaj a:"))
b = int(input("Podaj b:"))

nwd = nwd_i(a, b)

print(f'nwd({a}, {b}) = {nwd}')
