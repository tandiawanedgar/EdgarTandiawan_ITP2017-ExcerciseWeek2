list=[]
def insert():
    list.append(input("Please input the data:"))
    print(list)
    continue_function()

def delete():
    list.pop()
    print(list)
    continue_function()

def update():
    print(list)
    index = int(input("Which index you want to update? (Must be numbers, start from 0"))
    change = input ("What do you want to be updated?")
    list[index] =change
    print(list)
    continue_function()

def show_list():
    print("Here is the list:")
    print(list)
    continue_function()

def continue_function():
    z = input("Do you want to continue?? (yes/no)")
    if z.lower() == "yes":
        input_function()
    elif z.lower() == "no":
        print("Thank you for using inputer :)")
    else:
        print("Error, please try again!")
        continue_function()

def main():
    print("Welcome to inputer, please input the command:")
    input_function()

def input_function():
    x = input("insert/delete/update/list")
    if x.lower() == "insert":
        insert()
    elif x.lower() == "delete":
        delete()
    elif x.lower() == "update":
        update()
    elif x.lower() == "list":
        show_list()
    else: input_function()

# play main
main()