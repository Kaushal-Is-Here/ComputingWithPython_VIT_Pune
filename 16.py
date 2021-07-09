#Write a recursive function to generate Fibonacci sequence (0, 1, 1, 2, 3, 5, 8....)

def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))

#***************************************************** Output **************************************************************************/
#Enter number of terms:2
#Fibonacci sequence:
#0
#1