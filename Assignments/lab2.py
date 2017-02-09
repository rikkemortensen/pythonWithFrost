# Theatre Square

import math


n = float(input("Enter n: "))
m = float(input("Enter m: "))
a = float(input("Enter a: "))

M = int(math.ceil(m / a))
N = int(math.ceil(n / a))

print(M * N)
