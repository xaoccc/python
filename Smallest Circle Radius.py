from math import sqrt
r1 = int(input())
r2 = int(input())
r3 = int(input())

a = r1 + r2
b = r2 + r3
c = r1 + r3
d = r1 * r1
e = r2 * r2
f = r3 * r3
g = r1 * r2 * r3
h = r1 + r2 + r3


#cos_alfa = ((b * b) + ((r3 + r) * (r3 + r)) - ((r2 + r) * (r2 + r))) / (2 * b * (r3 + r))
#cos_alfa = ((c * c) + ((r3 + r) * (r3 + r)) - ((r1 + r) * (r1 + r))) / (2 * c * (r3 + r))

#((b * b) + ((r3 + r) * (r3 + r)) - ((r2 + r) * (r2 + r))) / (2 * b * (r3 + r)) = ((c * c) + ((r3 + r) * (r3 + r)) - ((r1 + r) * (r1 + r))) / (2 * c * (r3 + r))  | *(2 * (r3 + r))
#((b * b) + ((r3 + r) * (r3 + r)) - ((r2 + r) * (r2 + r))) /  b  = ((c * c) + ((r3 + r) * (r3 + r)) - ((r1 + r) * (r1 + r))) / c  
#((b * b) + ((r3 + r) * (r3 + r)) - ((r2 + r) * (r2 + r))) /  b  = ((c * c) + ((r3 + r) * (r3 + r)) - ((r1 + r) * (r1 + r))) / c  
#((b * b) + (r * r) + (2 * r * r3) + (r3 * r3) - (r * r) - (2 * r * r2) + (r2 * r2)) /  b  = ((c * c) +  (r * r) + (2 * r * r3) + (r3 * r3) - (r * r) - (2 * r * r1) + (r1 * r1)) / c 
#((b * b) + (2 * r * r3) + f - (2 * r * r2) + e) /  b  = ((c * c) + (2 * r * r3) + f - (2 * r * r1) + d) / c 
#b + (((2 * r * r3) - (2 * r * r2)) / b) + (( f + e) / b) = c + (((2 * r * r3) - (2 * r * r1)) / c) + ((f + d) / c)
#((2 * r * (r3 - r2)) / b) - ((2 * r * (r3 - r1)) / c) = c - b + ((f + d) / c) - ((f + e) / b)
#(2 * r * (((r3 - r2) / b) - ((r3 - r1) / c)) = c - b + ((f + d) / c) - ((f + e) / b)
r = (c - b + ((f + d) / c) - ((f + e) / b)) / ( 2 *(((r3 - r2) / b) - ((r3 - r1) / c)))
rad = g /(2 * sqrt(g * (h)) + (r1 * r2) + (r2 * r3) + (r3 * r1))
print(rad)
