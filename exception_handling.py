'''print("start")

try:
    a=10
    print(b)
    x=0
    y=10
    print(y/x)
    a={"name":"Mounika"}
    print(a["age"])
except NameError as n:
    print("That Particular variable is not defined")
except ZeroDivisionError as z:
    print("Not possible to divide")
except KeyError as k:
    print("There is no key")
except Exception as e:
    print("There is a exception raised")
    
print("end")
a=5
assert a==50
print(a)
#Syntax: assert expression1,expression2
a=5
assert a==50,'a is equal to 5'
print(a)'''
a=3
b=0
if b!=0:
    raise ZeroDivisionError("This error is made by me  ")
c=a+b
d=a-b
#e=a/b
try:
    print(c,d,e)
except Exception as e:
    print(e)
finally:
    print("bye")
