# Create a function showEmployee() in such a way that it should accept employee name, and its salary and display both. If the salary is missing in the function call assign default value 9000 to salary

def showEmployee(name, salary=9000):
    print("Employee", name, "salary is:", salary)

showEmployee("SIR", 9000)
showEmployee("SIR")


#***************************************************** Output **************************************************************************/



#Employee SIR salary is: 9000
#Employee SIR salary is: 9000
