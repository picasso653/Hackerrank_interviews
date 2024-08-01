def repeatedString(s, n):
    # Write your code here
    if  "a" in s:
        a = s.count("a")
        print(a)
        x = len(s)
        print(x)
        y = n // x
        print(y)
        z = n % x
        print(z)
        first_a =  a * y

        extra =  s * z
        res = first_a + extra[:z].count("a")
    else:
        res = 0
    return res
print(repeatedString("bc", 10))