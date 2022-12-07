from math import sqrt
r1 = int(input())
r2 = int(input())
r3 = int(input())

k1 = 1 / r1
k2 = 1 / r2
k3 = 1 / r3

k4 = k1 + k2 + k3 + 2 * sqrt(k1 * k2 + k2 * k3 + k1 * k3)
r = 1 / k4
#source: https://brilliant.org/wiki/descartes-theorem/?fbclid=IwAR1k03vvEUikHabIefKl4Yb3BSaiUJwdZ-erI_Tir6Zjuvd2m_ItPZ26VwY
