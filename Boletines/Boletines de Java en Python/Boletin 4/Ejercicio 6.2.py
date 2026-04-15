import math


def esPrimo(num):
    raiz = int(math.sqrt(num)+1)
    primo = True
    if(num % 2 != 0):
        i=3
        while primo == True and i <= raiz:
            if num % i == 0:
                primo = False
            i+=1
    else:
        if(num != 2):
            primo = False
    return primo

print(esPrimo(17))



n=51
while esPrimo(n) == False or esPrimo(n+2) == False:
    n += 2
print(n, "y", n+2)