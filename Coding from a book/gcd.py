def findGCD(m,n):
    if n > m :
        return findGCD(n,m)
    if m % n == 0 :
        return n
    else:   return findGCD(n, m%n)