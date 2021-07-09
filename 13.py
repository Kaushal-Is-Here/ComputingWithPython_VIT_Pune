#Find numbers divisible by nineteen or thirteen from a list of numbers using Lambda
#[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

list11=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

f=list(filter(lambda x:x%19==0 or x%13==0,list11))
print (f)

#***************************************************** Output **************************************************************************/

#[19, 65, 57, 39, 152, 190]