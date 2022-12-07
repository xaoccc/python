r1 = int(input())
r2 = int(input())
r3 = int(input())

a = r1 + r2
b = r2 + r3
c = r1 + r3

cos_alfa = ((b * b) + ((r3 + r) * (r3 + r)) - ((r2 + r) * (r2 + r))) / (2 * b * (r3 + r))
cos_alfa = ((c * c) + ((r3 + r) * (r3 + r)) - ((r1 + r) * (r1 + r))) / (2 * c * (r3 + r))

((b * b) + ((r3 + r) * (r3 + r)) - ((r2 + r) * (r2 + r))) / (2 * b * (r3 + r)) = ((c * c) + ((r3 + r) * (r3 + r)) - ((r1 + r) * (r1 + r))) / (2 * c * (r3 + r))  | *(2 * (r3 + r))
((b * b) + ((r3 + r) * (r3 + r)) - ((r2 + r) * (r2 + r))) /  b  = ((c * c) + ((r3 + r) * (r3 + r)) - ((r1 + r) * (r1 + r))) / c  
