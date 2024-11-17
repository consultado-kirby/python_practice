user_dict = {}

print("Enter key-value pairs for the dictionary.")
print("Type 'done' when you are finished.")

while True:
    key = input("Enter key (or type 'done' to finish): ")
    if key.lower() == 'done':
        break
    
    value = input(f"Enter value for '{key}': ")
    
    user_dict[key] = value

print("\nYour final dictionary is:")
print(user_dict)
#---------------------------------------
# def calculate(**kwargs):
#     for key, value in kwargs.items():
#         print(f"key={key}, value={value}")

# calculate(num_1=3, num_2=5, operator="+")

# def calculate(**kwargs):
#     print(kwargs)

# calculate(num_1=3, num_2=5, operator="+")