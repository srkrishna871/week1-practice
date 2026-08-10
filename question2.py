# Multiplication Pattern Analyzer

n=int(input("Enter a number:"))
e_count=0
o_count=0
for i in range(1,11):
    if((n*i)%2==0):
        print(f"{n}x{i}={i*n}-Even")
        e_count+=1
    else:
        print(f"{n}x{i}={i*n}-Odd")
        o_count+=1
print("Even Results:",e_count)
print("Odd Results:",o_count)