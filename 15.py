#Write a Python program to remove all elements from a given list present in another list using lambda.

def index_on_inner_list(list1, list2):
    result = [x for x in list1 if x not in list2]
    return result

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [2,4,6,8]

print("Original lists:")
print("list1:", list1)
print("list2:", list2)

print(index_on_inner_list(list1, list2))


#***************************************************** Output **************************************************************************/

#list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#list2: [2, 4, 6, 8]
#[1, 3, 5, 7, 9, 10]