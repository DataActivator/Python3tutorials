'''
Python has the following data types:
Text Type      :	str
Numeric Types  :	int, float, complex
Sequence Types :	list, tuple, range
Mapping Type   :	dict
Set Types      :	set, frozenset
Boolean Type   :	bool
Binary Types   :	bytes, bytearray, memoryview

'''

#1 Numeric Data Type :
# int (integer)
# float (floating point number)
# complex (complex number)

#int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
num1= -25
print(type(num1))

#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x = -2.10
print(type(x))

#Complex numbers are written with a "j" as the imaginary part:
a = 7+2j
print(type(a))

#2 Arithmetic & comparison operation on numeric data.
'''
Operator	                  Description	
+ (Addition)	              Adds operands on either side of the operator.	
- (Subtraction)	              Subtracts the right-hand operand from the left-hand operand.	
* (Multiplication)	          Multiplies values on either side of the operator.	
/ (Division)	              Divides the left-hand operand by the right-hand operand.		
// (Floor Division)	          The division of operands where the result is the quotient in which the digits after the decimal point are removed.
% (Modulus)	                  Returns the remainder of the division of the left-hand operand by right-hand operand.	
** (Exponent)	              Calculates the value of the left-operand raised to the right-operand.
'''
x = 10
y = 4
print(x**y)

'''
Operator	Description	
>	        True if the left operand is higher than the right one
<	        True if the left operand is lower than right one	
==	        True if the operands are equal	
!=	        True if the operands are not equal	
>=	        True if the left operand is higher than or equal to the right one	
<=	        True if the left operand is lower than or equal to the right one
'''
x = 10
y = 8
print(x>=y)

#3 Type Conversion :
'''
Built-in Function	  Description
int()                 Returns the integer object from a float or a string containing digits.
float()	              Returns a floating-point number object from a number or string containing digits with decimal point or scientific notation.
complex()	          Returns a complex number with real and imaginary components.
hex()                 Converts a decimal integer into a hexadecimal number with 0x prefix.
oct()                 Converts a decimal integer in an octal representation with 0o prefix.
pow()                 Returns the power of the specified numbers.
abs()                 Returns the absolute value of a number without considering its sign.
round()	              Returns the rounded number.
'''
print(pow(10,2))
print(abs(-10))
print(round(10.37,1))
num1 =int('100')
num2 =int('200')
print(num1+num2)