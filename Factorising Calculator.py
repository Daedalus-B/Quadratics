###Factorising for simple quadratics##
#Please Note your a value must always equal to 1
import math
import random
def factor(a, b, c):
    t = False
    while t == False:
        n = random.randint(-1000,1000)
        m = random.randint(-1000,1000)

        if n*m == c:
            if n+m == b:
                t = True
        else:
            t = False
    print('Note This is the form of Quadratic Factor (x+a) (x+b) where a and b is: ')      
    print("a = ",n)
    print("b = ", m)
def solve(a,b,c): # Note this should only be used when a > 1 or the x values are decimals
    #Quadratic formula broken down into methods
    f1 = b**2 - 4*a*c
    f2 = math.sqrt(f1)
    f3 = -b + f2
    f4 = 2*a
    ans = f3 / f4
    print("First value for x: ", ans)

    #Note this is the second value of x
    g1 = b**2 - 4*a*c
    g2 = math.sqrt(g1)
    g3 = -b - g2
    g4 = 2*a
    ans1 = g3 / g4
    print("Second value for x: ", ans1)
#solve() If you want to solve initiate a,b,c in the brackets e.g solve(2,-16,12) and run the program
#factor() If you want to factor initiate the value in the brackets and a must equal to = 1.  e.g. factor(1,8,16)
