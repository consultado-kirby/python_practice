import os
os.system('cls')

list = []
occurence = int(input("Enter the range of the list: "))

ctr = 0
for i in range(occurence):
    list.append(int(input(f"Enter number {ctr + 1} value: ")))
    ctr += 1
    
print(list)

ctr2 = 0
for lists in list:
    print(f"{ctr2 + 1}. {lists}")
    ctr2 += 1