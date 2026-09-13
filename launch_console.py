name = input("What's your name? ")
print("Welcome to " + name + "'s Launch Console!")
running = True
while running:
    print("1) About me")
    print("2) My goals")
    print("3) Desired Project")
    print("4) Exit")
    choice = input("Pick 1-4: ")
    if choice == "1":
        print('Im a high school coder at Code2College.')
    elif choice == "2":
        print('Build my first project.')
    elif choice == "3":
        print("StudySmart App")
    elif choice == "4":
        print('Goodbye!')
        running = False
    else:
        print("Please pick 1, 2, 3, or 4.")
        
