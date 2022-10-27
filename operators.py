a = 3 + 2       # Add
a += 10
m1 = 2 * 3      # Multiply

# Strings can be concatenated (glued together) with the + operator, and repeated with *
s = "12" + "35" # Concatenation
m2 = "2" * 3    # String repetition

b = 4 - 1       # Subtract
d1 = 17 / 3     # Divide
d2 = 17 // 3    # Divide - floor division discards the fractional part
e = 2 ** 10     # Exponent
f = 5 % 2       # Modulo - remainder after a division

print(f"{a=} {s=} {b=} {m1=} {m2=} {d1=} {d2=} {e=} {f=}") # a=15 s='1235' b=3 m1=6 m2='222' d1=5.666667 d2=5 e=1024 f=1

print(type(6 / 3))    # <class 'float'>