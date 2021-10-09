#!/usr/bin/env python
# coding: utf-8

# In[1]:


txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

x = txt.casefold()
print(x)

txt = "banana"
x = txt.center(20, "x")
print(x)

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
x = txt.count("apple", 10, 24)
print(x)

txt = "My name is Ståle"
x = txt.encode()
print(x)

print('utf-8 encoding: ', txt.encode(encoding="UTF-8",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

txt = "Hello, welcome to my world."
x = txt.endswith("my world.")
print(x)
x = txt.endswith("my world.", 5, 11)
print(x)

txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

txt = "Hello, welcome to my world."
print(txt.find("e"))
print(txt.find("e",5,10))
print(txt.find("q"))
#print(txt.index("q")) # produce error

txt0 = "For only {price:.2f} dollars!".format(price=49.123)
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt0)
print(txt1)
print(txt2)
print(txt3)

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a.isdecimal())
print(b.isdecimal())

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
print(a.isdigit())
print(b.isdigit())

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())


# In[93]:


# S.ljust
a = "Hello Python"
print(a.ljust(20,"k"))

# S.lower()
a = "Hello Python"
print(a.lower())

# S.lstrip
a = "Hello Python"
print(a.lstrip("H"))

# S.maketrans
a = "Hello Python"
b = "Python"
c = "012345"
print(a.maketrans(b,c))

# S.partition
a = "Hello Python"
print(a.partition("o"))

# S.replace
a = "Hello Python"
b = "Python"
c = "Inha"
print(a.replace(b,c))

# S.rfind, 없는값이면 -1
a = "Hello Python"
print(a.rfind("H"))  

# S.rindex, 없는값이면 오류
a = "Hello Python"
print(a.rindex("H"))

# S.rjust
a = "Hello Python"
print(a.rjust(20,"k"))

# S.rpartiton
a = "Hello Python"
print(a.rpartition("o"))

# S.rsplit
a = "Hello Python"
print(a.rsplit("o"))

# S.rstrip
a = "Hello Python"
print(a.lstrip("H"))

# S.split
a = "Hello Python"
print(a.split("o"))

# S.splitlines
a = "Hello \n Python"
print(a.splitlines())

# S.startswith
a = "Hello Python"
print(a.startswith("Hello"))
print(a.startswith("Python"))


# In[166]:


# S.islower()
a = "abc"; b = "ABC"
print(a.islower(), b.islower())

# S.isnumeric()
a = "1"
print(a.isnumeric())

# isprintable
a = "printable?"
print(a.isprintable())

# S.isspace
a = " "
print(a.isspace())

# S.istitle
a = "Hello Python"
b = "hello python"
print(a.istitle(), b.istitle())

# S.isupper
a = "ABC"
print(a.isupper())

# S.join
a = "Hello"
print(a.join("123"))

# S.strip
a = "     Hello Python     "
print(a.strip())

# S.swapcase
a = "Hello Python"
print(a.swapcase())

# S.title
a = "hello python"
print(a.title())

# S.translate
a = "Hello Python"
b = a.maketrans("P", "Q")
print(a.translate(b))

# S.upper
a = "abc"
print(a.upper())

# S.zfill
a = "abc  "
print(a.zfill(10))


# In[148]:





# In[ ]:




