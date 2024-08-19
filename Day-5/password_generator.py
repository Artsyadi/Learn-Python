import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','+']

num_let = int(input("How many letters would you like in your password?\n"))
num_num = int(input("How many numbers would you like in your password?\n"))
num_sym = int(input("How many symbols would you like in your password?\n"))
'''
# Easy level
password = ""
for i in range(num_let):
    password += random.choice(letters)
for i in range(num_num):
    password += random.choice(numbers)
for i in range(num_sym):
    password += random.choice(symbols)
print(password)
'''

# Hard level
password = []
new_pass = ""
for i in range(num_let):
    password.append(random.choice(letters))
for i in range(num_num):
    password.append(random.choice(numbers))
for i in range(num_sym):
    password.append(random.choice(symbols))

print(password)
random.shuffle(password)
print(password)

for char in password:
    new_pass += char
print(f"Your password is {new_pass}")

'''
for i in range(len(password)):
    x = random.choice(password)
    new_pass += x
    password.remove(x)
print(new_pass)
'''