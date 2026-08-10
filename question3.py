#Character Category Counter

string = input("Enter a string:")

l_count = 0
u_count = 0
dig = 0
space = 0
o_char = 0

for i in string:
    if i >= 'a' and i <= 'z':
        l_count += 1
    elif i >= 'A' and i <= 'Z':
        u_count += 1
    elif i >= '0' and i <= '9':
        dig += 1
    elif i == ' ':
        space += 1
    else:
        o_char += 1

print(f"Uppercase Letters: {u_count}")
print(f"Lowercase Letters: {l_count}")
print(f"Digits: {dig}")
print(f"Spaces: {space}")
print(f"Other Characters: {o_char}")