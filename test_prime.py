#!usr/bin/env python3

def main():
    x = int(input(""))
    factorize(x)

def factorize(x):
    m = 2
    p = x
    print("{0} is".format(x) ,end=" ")
    while (m <= (p)**0.5):
        if (x % m == 0):
            if (x == p): 
               print(m ,end="")
            else:
               print(" x {0}" .format(m) ,end="")
            x = x//m
        elif (x % m != 0):
           m = m + 1
    if (x == p):
        print("prime",end="")
    elif (x != 1):
        print(" x {0}".format(x),end="")
    print()

    print("mainn editor1")

    print("test2")

if __name__ == '__main__':
    main()
        
        
