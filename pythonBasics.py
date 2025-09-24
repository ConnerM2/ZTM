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

birth_year = int(input("what is your birth year?: "))
print(f"You are {2025 - birth_year} years old")

user_name = input("Username: ")
password = input("Password: ")
password = "*" * len(password)
print(f"{user_name}, your password {password} is {len(password)} letters long")