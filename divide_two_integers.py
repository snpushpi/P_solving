"""
STATEMENT
Divide two integers without using multiplication, division and mod operator.
CLARIFICATIONS
- Do I have to handle 32-bit integer overflow? Yes, return the MAX_INT in that case.
- Can the divisor be zero? Yes, return the MAX_INT.
EXAMPLES
34/3 -> 11
"""
def divide(dividend, divisor):
    sign = ((dividend<0) and (divisor<0)) or ((dividend>0) and (divisor>0))

    dividend, divisor = abs(dividend), abs(divisor)
    INT_MAX =  2147483647
    if divisor==0:
        return INT_MAX
    if dividend<divisor:
        return 0
    i = 0
    temp_div = divisor
    while temp_div<=dividend:
        temp_div+=divisor
        i+=1
    if sign:
        return i 
    else:
        return -i
print(divide(34,3))