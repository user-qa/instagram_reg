import functions

while True:
    choice = input("""
    
    1. REGISTER
    2. LOGIN
    3. STOP CODE
    
    """)

    if choice == '1':
        functions.register()

    elif choice == '2':
        ans = functions.login()
        if ans is not None:
            print(ans)

    elif choice == '3':
        break
