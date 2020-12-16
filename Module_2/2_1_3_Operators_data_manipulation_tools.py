# Basic operators: +, -, *, /, //, %, **
# hierarchy of priorities/precendence: 
# +x, -x, ~x (unary; one operand. -1, +3)
# **
# *, /, //, %
# +, - (binary; two operands. 4 + 5, 12 % 5)
# <<, >>
# &
# ^
# |
# ==, !, >, >=, <, <=, is, is not, in, not in
# not
# and
# or
print(2 + 2)
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
print(6 // 4)
print(6. // 4)
print(-6 // 4)
print(6. // -4)
print(14 % 4)
# 14 // 4 -> 3; integer quotient;
# 3 * 4 -> 12; quotient and divisor multiplication;
# 14 - 12 -> 2; remainder
print(12 % 4.5)
# 12 // 4.5 -> 2.0
# 2.0 * 4.5 -> 9.0
# 12 - 9.0 -> 3.0
print(-4 + 4)
print(-4 + 8)
print(-4 - 4)
print(4. - 8)
print(-1.1)
print(+2)
print(2 + 3 * 5)
print(9 % 6 % 2) #left sided binding
print(9 % 6 % 2) #right sided binding
print(2 ** 2 ** 3) #exponentiation operator uses right sided binding, therefore 256 instead of 64
#print(2 * 3 % 5)
# //, *, -
# 2 * 3 = 6
#print(6 % 5)
print(6 // 5)
print(1  * 5)
print(5 - 5)
print(5 // 6)
print(0 * 6)
print(6 - 6)
#The result of integer division is always rounded to the nearest integer
#value that is less than the real (not rounded) result.
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
#print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
#print(25 // 13)
#print(1 * 13)
#print(25 - 13)
#print((5 * (12 + 100) / 26) // 2)
#print(5 * 112 / 26 // 2)
#print(560 / 26 // 2) (niet afronden!!, check eem!)
print(21 // 2)
print((2 ** 4), (2 * 4.), (2 * 4))
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print((2 % -4), (2 % 4), (2 ** 3 ** 2))