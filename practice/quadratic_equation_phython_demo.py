Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> print("hello adeolu")
hello adeolu
>>> print("Enter a,b,c for a quadratic in the form of ax*2 + bx + c =0 to find the root of the quadratic.")
Enter a,b,c for a quadratic in the form of ax*2 + bx + c =0 to find the root of the quadratic.
>>> a = input("what is the value of a?")
what is the value of a?
>>> b = input("what is the value of b")
what is the value of b
>>> b = input("what is the value of c")
what is the value of c
>>> a = float(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a = float(a)
ValueError: could not convert string to float: ''
>>> a = input("what is the value of a?")
what is the value of a? 2
>>> b = input("what is the value of b")
what is the value of b 4
>>> c =input("what is the value of c?")
what is the value of c? 8
>>> a = float(a)
>>> b = float(b)
>>> c = float(c)
>>> determinant = b ** 2 - 4 * a * c
>>> print (determinant)
-48.0
>>> min_x = (-b - (determinant) ** (1 / 2)) /(2 * a)
>>> max_x = (-b + (determinant) ** (1 / 2)) /(2 * a)
>>> print(f "The lesser x is equal to {min_x} and the greater x is qual to {max_x}")
SyntaxError: invalid syntax
>>> print(f"The lesser x is equal to {min_x} and the greater x is qual to {max_x}")
The lesser x is equal to (-1-1.7320508075688772j) and the greater x is qual to (-0.9999999999999999+1.7320508075688772j)
