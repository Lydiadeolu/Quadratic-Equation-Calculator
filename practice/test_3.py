Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
a = 847
b = 905
c== a**2 + b**2
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    c== a**2 + b**2
NameError: name 'c' is not defined
a**2 + b**2
1536434
a = 'flimsy'
b = 'miserable'
c = b[0:1] + a[2:]
SyntaxError: multiple statements found while compiling a single statement
c = b[0:1] + a[2:]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    c = b[0:1] + a[2:]
TypeError: 'int' object is not subscriptable
a = 'flimsy'
b = 'miserable'
c = b[0:1] + a[2:]
print (c)
mimsy
b [0:3:]
'mis'
s = 'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain'
s [22:27:]
'Humpt'
s [97:102:]
'Dumpt'
w = 'wF3GvJWvP231DAWc89AIA3NEQnw2417qVrsLaIWtbDZc6kiLHomalopsis5NDzN89Rsz81xsvYGOPYQ6V3INwI9np81dIeGR2YO3yjMNG4ggH4cQ4oJIjIZ8JmajormoU2E4x4t3P6HTncK1LXg2rI6tvezCDqLJBrqt2RlKz6wrxf19K'
w [51:60:]
'alopsis5N'
w [124:128:]
'ormo'
F = 'cbEgEIAxSFqVgaMvJCJGKnlfdDXUxAmbystomakWdp8rPOHvOtrigonopodus4muZQ7idPARUAbrFE3uctuOEXP3h0bfJ02neU5tYT5AsuVn8FIQn2bLnU1DLtDNjMwA6N00SevuW4TmkMP8d3OqrbCaqSVHE3mx.'
F [29:37]
'Ambystom'
F [49:60]
'trigonopodu'
a = 29
b = 37
c = 124
d = 128
print (s[a:b+1]),
print (s[c:d+1]
       
SyntaxError: multiple statements found while compiling a single statement
print s[a:b+1],; print s[c:d+1]
       
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print(s[a:b+1],; print s[c:d+1]
      
SyntaxError: invalid syntax
print f[a:b+1],; print f[c:d+1]
      
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print (F[a:b+1]),; print (F[c:d+1])
...       
Ambystoma
(None,)
jMwA6
>>> print (F[a:b+1]), print (F[c:d+1])
...       
Ambystoma
jMwA6
(None, None)
>>> print (F[a:b+1] end= ' ') print (F[c:d+1])
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print (F[a:b+1] end= ' '), print (F[c:d+1])
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print (F[a:b+1], end= ' ') print (F[c:d+1])
...       
SyntaxError: invalid syntax
>>> print (F[a:b+1], end= ' ') print (F[c:d+1])91(
...       
SyntaxError: invalid syntax
>>> print (F[a:b+1], end= ' ')
...       
Ambystoma 
>>> 0print (F[c:d+1])
...       
jMwA6
>>> m = 'vDI4rM5RJm11rirB3UJKjWE8OO2aAllobatesXrEAJkKyY0lKVkBelaphusWYah6RdqaIHlSqRtB6BoUfkIdKSst7sNGr5GQfB7v1ZY0O0XY2DYuKcsIvea9fB6NqRubiW2GNvajUwJ6hwsidSXT7tPsY75iQRY.
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> m =  'vDI4rM5RJm11rirB3UJKjWE8OO2aAllobatesXrEAJkKyY0lKVkBelaphusWYah6RdqaIHlSqRtB6BoUfkIdKSst7sNGr5GQfB7v1ZY0O0XY2DYuKcsIvea9fB6NqRubiW2GNvajUwJ6hwsidSXT7tPsY75iQRY.'
...       
>>> m[28:36+1] + " " m[52:58+1]
...       
SyntaxError: invalid syntax
>>> m[28:36+1] + " " + m[52:58+1]
...       
'Allobates elaphus'





>>> print ('corrections')
...
    corrections
>>> speed = 23
>>> time = 120
>>> velocity = speed * time
>>> print(velocity)
...
    2760







