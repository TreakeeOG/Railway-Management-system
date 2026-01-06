# RAILWAY ADMIN CLI

import getpass

print("=" * 40)
print(" RAILWAY MANAGEMENT SYSTEM ")
print("        ADMIN CLI")
print("=" * 40)


# SIMPLE AUTH (OPTIONAL BUT FIRE)

while True:
    password = getpass.getpass("Enter admin password: ")
    if password == "admin123":
        print("Access granted ✅")
        break
    else:
        print("Access denied ❌")


print("Type 'help' to see commands\n")



# CLI LOOP

while True:
    command = input("RMS> ").strip().lower()

    if command == "help":
        print("""
Available Commands:
-------------------
view_trains        - View all trains
view_passengers    - View passenger list
clear              - Clear screen
exit               - Exit CLI
""")

    elif command == "view_trains":
        print("Fetching train data...")
        # later → connect MySQL here

    elif command == "view_passengers":
        print("Fetching passenger details...")
        # later → MySQL SELECT query here

    elif command == "clear":
        import os
        os.system("cls")

    elif command == "exit":
        print("Exiting CLI 👋")
        break

    else:
        print("Unknown command. Type 'help'")
