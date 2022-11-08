# Arithmetic Operators
# --------------------

a = 3 + 2       # Add
a += 10
# a++           # SyntaxError

# Coercion
# If you have an operation involving two numerics, coercion generally does the right thing. 

# For operations involving an integer and a float, the integer is coerced to a float. 
# int + float -> float
x = 10
y = 0.5
z = x + y
print(f"{x=} type: {type(x)}")
print(f"{y=} type: {type(y)}")
print(f"{z=} type: {type(z)}")


# Strings can be concatenated (glued together) with the + operator, and repeated with *
# str + str -> concat str
s1 = "Jordan"
s2 = "Michael"
print(s1 + ", " + s2)   # Jordan, Michael

s = "12" + "34"         # 1234

# err = "Sum is: " + 100  
# err = "100" + 100     #TypeError: can only concatenate str (not "int") to str

# list + list -> concat list
weekdays = ["MON", "TUE", "WED", "THU", "FRI"]
weekend = ["SAT", "SUN"]
print(weekdays+weekend)     # ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']


m1 = 2 * 3      # Multiply

# If the left operand is a string and you use the multiplication operator, *, Python performs repetition
# str * int -> str
x = "money"
print(3 * x)



b = 4 - 1       # Subtract
d1 = 17 / 3     # Divide
d2 = 17 // 3    # Divide - floor division discards the fractional part
e = 2 ** 10     # Exponent
f = 5 % 2       # Modulo - remainder after a division

print(f"{a=} {s=} {b=} {m1=} {d1=} {d2=} {e=} {f=}") # a=15 s='1235' b=3 m1=6 d1=5.666667 d2=5 e=1024 f=1

print(type(6 / 3))    # <class 'float'>


# comparison operators
# --------------------

x, y, z = 100, 200, 100

c1 = x == z         # True
c2 = x >= y         # False
c3 = 85 <= x <=100  # True

print(c1, c2, c3)

# logical operators
# ------------------

c4 = x < 1000 and y > 1000  # False
c5 = x < 1000 or y > 1000   # True

print(c4, c5)


# Membership Operators
# ---------------------
fruits = ["apple", "banana", "strawberry"]
c6 = "banana" in fruits     # True
c7 = "orange" not in fruits # True

print(c6, c7)

