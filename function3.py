#function with default arguments

def fun(IdNo=0,name="Not Given",salary=0.0):
    print("Employee ID :",IdNo)
    print("Employee Name :",name)
    print("Employee Salary :",salary)
fun()
print("-----------")
fun(1001)
print("----------")
fun(name="bhushan")
print("-------------")
fun(salary=24500.0)
print("----------")
fun(101,"bhushan",25009.0)