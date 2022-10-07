# Вычислить число c заданной точностью d
## Пример:
## - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
from math import pi
p = str(pi)
print(p)
d = str(input('Введите число  d в промежутке 10^{-1} ≤ d ≤10^{-10}: '))
print(len(d))
n = int(len(d))
print(n)
print(p[0:n])
