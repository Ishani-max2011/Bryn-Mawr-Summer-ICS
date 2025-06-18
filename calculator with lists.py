menu = ["addition", "subtraction", "multiplication", "division", "modular division"]
print(menu)
nums = []

#addition
option = input("Choose an operation: ") # Display the menu and prompt for an operation")
if option.lower().strip() == menu[0]:
    num1 = int(input("Type in a number: "))
    num2 = int(input("Type in another number: "))
    nums.append(num1)
    nums.append(num2)
    sum = nums[0] + nums[1]
    print(f"The sum of {nums[0]} and {nums[1]} is {sum}")
elif option.lower().strip() == menu[1]:
    num1 = int(input("Type in a number: "))
    num2 = int(input("Type in another number: "))
    nums.append(num1)
    nums.append(num2)
    difference = nums[0] - nums[1]
    print(f"The difference of {nums[0]} and {nums[1]} is {difference}")
elif option.lower().strip() == menu[2]:
    num1 = int(input("Type in a number: "))
    num2 = int(input("Type in another number: "))
    nums.append(num1)
    nums.append(num2)
    product = nums[0] * nums[1]
    print(f"The product of {nums[0]} and {nums[1]} is {product}")
elif option.lower().strip() == menu[3]:
    num1 = int(input("Type in a number: "))
    num2 = int(input("Type in another number: "))
    nums.append(num1)
    nums.append(num2)
    quotient = nums[0] / nums[1]
    print(f"The quotient of {nums[0]} and {nums[1]} is {quotient}")
elif option.lower().strip() == menu[4]:
    num1 = int(input("Type in a number: "))
    num2 = int(input("Type in another number: "))
    nums.append(num1)
    nums.append(num2)
    remainder = nums[0] % nums[1]
    print(f"The remainder of {nums[0]} and {nums[1]} is {remainder}")
else:
    print("Invalid option. Please choose a valid operation from the menu.")
