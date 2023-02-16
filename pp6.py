#import PySimpleGUI as sg
import arcade
import random

#https://www.w3schools.com/python/default.asp
#https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises%20for%20Python%203.md
#https://github.com/practical-tutorials/project-based-learning#python

"""
def ci():
    x = input("enter commands\n")
    return x
class rc():
    def __init__(self, commands):
        self.c = commands
        self.x = 0
        self.y = 0
        self.l = []
        self.i = None
    def ci1(self):
        self.c = input("enter commands\n")
        rc.cp(self)
    def cp(self):
        c = self.c
        c = str(c)
        l = self.l
        l = c.split()
        for item in l:
            if item.isalpha():
                if item == "right":
                    num = l.index(item)
                    self.x += int(l[num + 1])
                elif item == "left":
                    num = l.index(item)
                    self.x -= int(l[num + 1])
                elif item == "up":
                    num = l.index(item)
                    self.y += int(l[num + 1])
                elif item == "down":
                    num = l.index(item)
                    self.y -= int(l[num + 1])
        print(f"x pos: {self.x}\ny pos: {self.y}")
        rc.ci1(self)
cm = ci()
r = rc(cm)
r.cp()
"""

"""
class pi():
    def password_input():
        x = input("At least 1 letter between [a-z]\nAt least 1 number between [0-9]\nAt least 1 letter between [A-Z]\nAt least 1 character from [$#@]\nMinimum length of transaction password: 6\nMaximum length of transaction password: 12\n")
        return x
class pc():
    def __init__(self, password):
        self.p = password
    def password_checker(self):
        a = []
        d = []
        for x in pin:
            if x.isalpha():
                a.append(x)
            elif x.isdigit():
                d.append(x)
        if len(a) != 0 and len(d) != 0:
            print("good password")
        else:
            print("the entered password isn't strong enough")
        #print(self.p)
pin = pi.password_input()
pinc = pc(pin)
pinc.password_checker()
"""

"""
class hello():
    def __init__(self, i):
        self.y = i
        self.x = None
        self.z = None
    def d(self):
        self.y += int(self.z[1])
        hello.bank(self)
    def w(self):
        self.y -= int(self.z[1])
        hello.bank(self)
    def v(self):
        print(self.y)
        hello.bank(self)

    def bank(self):
        self.x = input("deposit or withdraw or view (d ###/w ###/v)\n")
        for char in self.x:
            if char == "d":
                a = self.x
                self.z = a.split()
                print(self.z)
                hello.d(self)
            elif char == "w":
                a = self.x
                self.z = a.split()
                hello.w(self)
            elif char == "v":
                hello.v(self)
            else:
                pass
hellov = hello(0)
hellov.bank()
"""


"""
l = []
x = "helloworld"
x.split()
" ".join(x)
l.append(x)
l.index("")
x.find("")
x.count("")
l.sort()
sorted(x)
x.upper()
x.lower()
x.strip()
x.replace()
"""

"""
list = [
    "addition",
    "subtraction",
    "multiplication",
    "division"
]
class arith():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def setup(self):
        x = input("what operation do you want to do?\n")
        return x
    def addition(self):
        self.num1 = float(input("enter first number"))
        self.num2 = float(input("enter second number"))
        return (self.num1 + self.num2)# * 3#bedmas
    def subtraction(self):
        self.num1 = float(input("enter first number"))
        self.num2 = float(input("enter second number"))
        return self.num1 - self.num2
    def multiplication(self):
        self.num1 = float(input("enter first number"))
        self.num2 = float(input("enter second number"))
        return self.num1 * self.num2
    def division(self):
        self.num1 = float(input("enter first number"))
        self.num2 = float(input("enter second number"))
        return self.num1 / self.num2
a = arith(None, None)
setup = a.setup()
if setup == "division":
    print("helloworld1")
    print(a.division())
    exit()
elif setup == "addition":
    print("helloworld2")
    print(a.addition())
    exit()
elif setup == "subtraction":
    print("3")
    print(a.subtraction())
    exit()
elif setup == "multiplication":
    print("4")
    print(a.multiplication())
    exit()
"""

#https://realpython.com/python-strings/
"""
import time
fridge = False
opened = False
class room():
    def table():
        print("table moved!")
    def chair():
        print("chair moved!")
    def open_fridge():
        print("fridge opened!")
        x = input("what do you want to get from the fridge?\n")
        print(f"you have retrieved {x}!")
        opened = True
y = input("what do you want to do?\n")
while True:
    if y == "fridge":
        room.open_fridge()
    if y == "table" and opened:
        print(f"you have put {x} on the table!")
"""
#list = [
#    room.table(),
#    room.chair()
#]
#room.table()
#room.chair()

"""
sg.theme("Dark Amber")
#layout = [
#    [sg.Text("Helloworld!", (20, 20))]
#]
layout = [
    [sg.Text("helloworld")],
    [sg.Text("fdjsa;kl")]
]
sgwin = sg.Window("Room", layout)
while True:
    event, values = sgwin.read()
"""
"""
dict  = {
    "a":"hello",
    "b":"bye"
}
if "a" in dict and "a" == "hello":
    print("fdjasl;")
"""
"""
x = 1
while True:
    print("helloworld", x)
    x += 1
    time.sleep(0.2)
"""
"""

class table():
    def move_table():
        print("table moved!")
    def destroy_table():
        print("table destroyed!")
table.move_table()
table.destroy_table()

"""

"""
class house():
    def move_table():
        print("table moved!")
    def move_chair():
        print("chair moved!")

house.move_table()
house.move_chair()

dictionary = {
    "1" : "one",
    "2" : "two"
}
print(dictionary["1"], dictionary["2"])
for dictionary in dictionary:
    if "1" in dictionary:
        print("hello")
tuple = ("a", "b")
for tuple in tuple:
    print("1")
if int(dictionary["1"]) == int(dictionary["1"]):
    print("fjdka;sl")
"""