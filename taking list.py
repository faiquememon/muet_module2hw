list = []
n = int(input("Enter the number of elements in list : "))
for i in range(n):
    print("enter number to add to list : ")
    list.append(int(input()))
print(list)
total = sum(list)
print("The total sum of the list is " , total)