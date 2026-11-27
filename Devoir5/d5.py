#Question 1
def triangle(n):
    if n < 1:
        return
    else:
        triangle(n-1)
        print("*"*n)



#Question 2
def etoiles(n):
    if n < 1:
        return
    else:
        print("*"*n)
        etoiles(n-1)
        print("*"*n)

#Question 3
def prodListePos_rec(liste, n):
    if n < 1:
        return 1
    else:
        prod = prodListePos_rec(liste, n-1)

        if liste[n-1] > 0:
            return prod * liste[n - 1]

        return prod

def prodLRec1(liste):
    if len(liste) == 0:
        return 1
    
    premier = liste[0]
    rem = liste[1:]

    if premier > 0:
        return premier * prodLRec1(rem)

    return prodLRec1(rem)
