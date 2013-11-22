# very simple solution to problem 25 using F(n)=(digits - 1 + log10(5) / 2) / log1o(phi)

# imports
from math import log10, sqrt, ceil

digits = 999

print(int(ceil((digits + log10(5) / 2.0) / log10(( 1 + sqrt(5)) / 2.-0)))) 
