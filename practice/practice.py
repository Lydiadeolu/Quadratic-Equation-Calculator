Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> input("is the world flat")
       
SyntaxError: EOL while scanning string literal
>>> 


>>> 

>>> 

>>> input("is the world flat")
is the world flat yes
' yes'
>>> if yes
...     print('then be careful with your steps so as not to fall')
SyntaxError: invalid syntax
>>> if yes
SyntaxError: invalid syntax
>>> # this is common error
>>> 7 * 2
14
>>> weight = 12
>>> height = 2
>>> weight * height
24
>>> print
<built-in function print>
>>> print("body mass is " weight * height)
SyntaxError: invalid syntax
>>> print("body mass is " _)
SyntaxError: invalid syntax
>>> print('"body mass is" _')
"body mass is" _
>>> 'spam egg'
'spam egg'
>>> weight = 12
>>> height = 2
>>> weight = int(weight)
>>> height = int(height)
>>> body_mass = weight * height
>>> print(body_mass)
SyntaxError: multiple statements found while compiling a single statement
>>> weight = 24
>>> height = 14
>>> body_mass = weight * height
>>> print(body_mass)
336
>>> print(body_mass , "is your body mass")
SyntaxError: invalid syntax
>>> s = 'First line.\nSecond line.'
>>> s
'First line.\nSecond line.'
>>> print(s)
First line.
Second line.
>>> ....
SyntaxError: invalid syntax
>>> 3 * 'un'+ 'ium'
'unununium'
>>> 'py' 'thon'
'python'
>>> 'ly' 'dia'
'lydia'
>>> 
>>> text = ('Put several strings within parentheses '
        'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
>>> body_mass
336
>>> body_mass , 'is the body mass index'
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    body_mass + 'is the body mass index'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> word = 'oyelabi'
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    word = oylabi
    # I was suppose to add ' ' to concertnate a string
NameError: name 'oylabi' is not defined
>>> word = 'OELABI'
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    word
NameError: name 'word' is not defined
=
>>> word = 'OYELABI'
>>> word[2]
'E'
>>> word[4]
'A'
>>> word[0]
'O'
>>> word[:2] + word[:2]
'OYOY'
>>> word[-2]
'B'
>>> word[-4]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    wor[-4]
    # the letter d was missing in the name created
NameError: name 'wor' is not defined
>>> word[-4]
'L'
>>> word[2:5]
'ELA'
>>> 'w' + word[1:]
'wYELABI'
>>>print('the body masss calculated' , body_mass)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    'the body masss calculated' + body_mass
    # , is suppose to be use instead of using a +  
TypeError: can only concatenate str (not "int") to str
>>> print('the body mass calculated is' , body_mass)
the body mass calculated is 336
>>> 
