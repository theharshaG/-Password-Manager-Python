while True:
    print("\n1. Add Account")
    print("2. View Accounts")
    print("3. Search Password")
    print("4. Delete Account")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter account name: ").strip()
        pas = input("Enter password: ").strip()

        with open("passwords.txt", "a") as file:
            file.write(name + "," + pas + "\n")

        print("Account added successfully")

  
    elif choice == "2":
        try:
            with open("passwords.txt", "r") as file:
                data = file.readlines()

                if not data:
                    print("No accounts found")

                for i, line in enumerate(data, start=1):
                    name, pas = line.strip().split(",")
                    print(f"{i}. {name} -> {pas}")

        except FileNotFoundError:
            print("No data file found")
    elif choice == "3":
        name1 = input("Enter account name to search: ").strip().lower()
        found = False

        try:
            with open("passwords.txt", "r") as file:
                for line in file:
                    name, pas = line.strip().split(",")

                    if name.lower() == name1:
                        print("Password:", pas)
                        found = True
                        break

            if not found:
                print("Account not found")

        except FileNotFoundError:
            print("No data file found")

    elif choice == "4":
        name1 = input("Enter account name to delete: ").strip().lower()
        new_data = []
        found = False

        try:
            with open("passwords.txt", "r") as file:
                for line in file:
                    name, pas = line.strip().split(",")

                    if name.lower() != name1:
                        new_data.append(line)
                    else:
                        found = True

            with open("passwords.txt", "w") as file:
                file.writelines(new_data)

            if found:
                print("Account deleted successfully")
            else:
                print("Account not found")

        except FileNotFoundError:
            print("No data file found")

    elif choice == "5":
        print("Goodbye ")
        break

    else:
        print("Invalid choice")
