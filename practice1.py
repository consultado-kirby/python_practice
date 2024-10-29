import os
os.system('cls')
print("Enter Admin ID: ")
admin_id = input(" | ")

admins = ["admin0001", "admin0002", "admin0003"]
while admin_id in admins:
    print("ADMIN")
    print("\nEnter Admin ID: ")
    admin_id = input(" | ")
    if admin_id not in admins:
        print("NOT ADMIN")
        break
    
print("\nProgram end.")