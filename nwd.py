
def nwd_i(a, b):
    while b:
        a, b = b, a%b
    return a

a = input("Podaj a:")
b = input("Podaj b:")

nwd = nwd_i(a, b)

print("nwd = " + nwd)
