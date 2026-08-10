# Remove Repeated Consecutive Values
values = [10, 10, 20, 20, 20, 30, 10, 10, 40]
result=[]
j=0
for i in values:
    if not result or result[-1]!=i:

        result.append(i)

print("Original List:")
print(values)

print("Result:")
print(result)

# values = [10, 10, 20, 20, 20, 30, 10, 10, 40]
# 
# new_list = [values[0]]
# 
# for i in range(1, len(values)):
#     if values[i] != values[i - 1]:
#         new_list.append(values[i])
# 
# print("Original List:")
# print(values)
# 
# print("Result:")
# print(new_list)