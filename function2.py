# function with default argument

# x and y is default argument

def sum(x=0,y=0):
    print(x)
    print(y)
    z=x+y
    print("the sum is :",z)
sum()   #without getting the values can call the function
print("-------------")
sum(100)
print("------------------------")
sum(y=29)
print("---------------")
sum("wagh ","bhushan")
print("-------------------")