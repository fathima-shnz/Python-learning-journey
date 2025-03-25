#Python lists
# To store expenses as list
# To calculate total, maximum and minimum expenses

exp = []
stopped = False

while not stopped:
    e = int(input("Enter expense(Type 0 to stop): "))
    if e != 0:
        exp.append(e)
    else:
        stopped = True

print(exp)
print("Total expense is ", sum(exp))
print("Maximum expense is ", max(exp))
print("Minimum expense is ", min(exp))


#OUTPUT
#Enter expense(Type 0 to stop): 65
#Enter expense(Type 0 to stop): 150
#Enter expense(Type 0 to stop): 270
#Enter expense(Type 0 to stop): 15
#Enter expense(Type 0 to stop): 0
#[65, 150, 270, 15]
#Total expense is  500
#Maximum expense is  270
#Minimum expense is  15
