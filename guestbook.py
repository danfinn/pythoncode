import users

def display_menu():
    print('1: Login')
    print('2: Register')
    if users.is_logged_in == True:
        print('3: Post Comment')
    print('9: Exit')
    choice = input('Enter the number of where you want to go: ')
    check_choice(choice)
    
def check_choice(choice):
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            users.login()
            display_menu()
        elif choice == 2:
            users.register()
            display_menu()
        elif choice == 3:
            pass
        elif choice == 9:
            pass
        else:
            print('Please choose a correct option')
            display_menu()
    else:
        print('Please choose a correct option')
        display_menu()
display_menu()
