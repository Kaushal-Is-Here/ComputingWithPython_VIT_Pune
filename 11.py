#Write a Python program to filter a list of integers using Lambda. even,odd

list_A = [33, 35, 36, 39, 40, 42]

res = []

for n in list_A:
   if n % 2 == 0:
      res.append(n)
print(res)

#***************************************************** Output **************************************************************************/

#[36, 40, 42]