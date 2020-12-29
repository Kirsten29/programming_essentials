3_1_3_5
var = 17
varRight = var >> 1
varLeft = var << 2
print(var, varLeft, varRight)

The final print() invocation produces the following output:

17 68 8

Note:

17 // 2 → 8 (shifting to the right by one bit is the same as integer division by two)
17 * 4 → 68 (shifting to the left by two bits is the same as integer multiplication by four)
