print("testing")

print(type(54)) # Int
print(type(54.5)) # Float
print(type('Hello'))

snake_case = 'variabe names'
PI = 3.14 # Constants are not meant to change
a,b,c = 1,2,3

nums = '1234567'
# [start: stop: stepover]
print(nums[:5])
print(nums[2:])
print(nums[::1])
print(nums[::-1])

# birth_year = int(input("what is your birth year?: "))
# print(f"You are {2025 - birth_year} years old")

# user_name = input("Username: ")
# password = input("Password: ")
# password = "*" * len(password)
# print(f"{user_name}, your password {password} is {len(password)} letters long")

# using this list: 
basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
# access "Oranges" and print it:
print(basket[1][1][0])

# using this list,
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# 1. Remove the Banana from the list
basket.pop(0)
# 2. Remove "Blueberries" from the list.
basket.remove("Blueberries")
# 3. Put "Kiwi" at the end of the list.
basket.append('kiwi')
# 4. Add "Apples" at the beginning of the list
basket.insert(0, "apples")
# 5. Count how many apples in the basket
basket.count("Apples")
# 6. empty the basket
print(basket)
new_list = list(range(1, 20))
print(new_list)

# List unpacking, assigne variables to list items
a,b,c, *other = [1,2,3,4,5,6]
print(a,b,c)
print(other)