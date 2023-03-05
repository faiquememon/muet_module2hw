my_list = []
print("Enter the number of elements in the list")
n = int(input())
for i in range(n):
    print("Enter the number for list")
    x=int(input())
    my_list.append(x)
print("the list you entered is " , my_list)
print("Do you want to append the list 1= yes and 2= no")
y = int(input())
if  y == 1 :
    print("enter any integer to append")
    z = int(input())
    if z in my_list:
        print("the entered number is already in the list")
    else:
        my_list.append(z)
        print("the new list is " , my_list)
else:
    print("no changes made to the list")
    print(my_list)
print("Do you want to remove any element from the list yes = 1 and no = 2")
y = int(input())
if y== 1 :
    print(my_list)
    print("enter integer to remove from the list")
    r = int(input())
    if r in my_list:
        my_list.remove(r)
        print("The modified list is" , my_list)
else:
    print("you didnot removed any elements from the list")
    print(my_list)
print("Do you want to insert element in the list yes = 1 and no = 2")
y = int(input())
if y == 1:
    print("enter the position to enter ")
    pos = int(input())
    print("enter the integer to insert")
    int1 = int(input())
    my_list.insert(pos,int1)
    print("the updated list is " , my_list)
else:
    print("you didnot inserted any new integers")


