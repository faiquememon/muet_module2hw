my_list = []
print("Enter a list of Integers separated by space")
user_input = input()
my_list = [int(x) for x in user_input.split( )]
print(my_list)
