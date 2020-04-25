Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=5
>>> num
5
>>> id(num)
140712520872320
>>> a=10
>>> b=a
>>> a
10
>>> b
10
>>> id(a)
140712520872480
>>> id(b)
140712520872480
>>> k=10
>>> id(k)
140712520872480
>>> a=9
>>> id(a)
140712520872448
>>> k=a
>>> id(k)
140712520872448
>>> b=8
>>> b
8
>>> id(b)
140712520872416
>>> type(num)
<class 'int'>
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,6,2))
[2, 4]
>>> bin(25)
'0b11001'
>>> hex(6)
'0x6'
>>> hex(56)
'0x38'
>>> ox6
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    ox6
NameError: name 'ox6' is not defined
>>> 0x6
6
>>> oct(34)
'0o42'
>>> 0xf
15
>>> 
