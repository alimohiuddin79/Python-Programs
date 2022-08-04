#Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print('''
 /$$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$      /$$  /$$$$$$  /$$$$$$$  /$$$$$$$         /$$$$$$  /$$$$$$$$ /$$   /$$ /$$$$$$$$ /$$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$  /$$$$$$$ 
| $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$  /$ | $$ /$$__  $$| $$__  $$| $$__  $$       /$$__  $$| $$_____/| $$$ | $$| $$_____/| $$__  $$ /$$__  $$|__  $$__//$$__  $$| $$__  $$
| $$  \ $$| $$  \ $$| $$  \__/| $$  \__/| $$ /$$$| $$| $$  \ $$| $$  \ $$| $$  \ $$      | $$  \__/| $$      | $$$$| $$| $$      | $$  \ $$| $$  \ $$   | $$  | $$  \ $$| $$  \ $$
| $$$$$$$/| $$$$$$$$|  $$$$$$ |  $$$$$$ | $$/$$ $$ $$| $$  | $$| $$$$$$$/| $$  | $$      | $$ /$$$$| $$$$$   | $$ $$ $$| $$$$$   | $$$$$$$/| $$$$$$$$   | $$  | $$  | $$| $$$$$$$/
| $$____/ | $$__  $$ \____  $$ \____  $$| $$$$_  $$$$| $$  | $$| $$__  $$| $$  | $$      | $$|_  $$| $$__/   | $$  $$$$| $$__/   | $$__  $$| $$__  $$   | $$  | $$  | $$| $$__  $$
| $$      | $$  | $$ /$$  \ $$ /$$  \ $$| $$$/ \  $$$| $$  | $$| $$  \ $$| $$  | $$      | $$  \ $$| $$      | $$\  $$$| $$      | $$  \ $$| $$  | $$   | $$  | $$  | $$| $$  \ $$
| $$      | $$  | $$|  $$$$$$/|  $$$$$$/| $$/   \  $$|  $$$$$$/| $$  | $$| $$$$$$$/      |  $$$$$$/| $$$$$$$$| $$ \  $$| $$$$$$$$| $$  | $$| $$  | $$   | $$  |  $$$$$$/| $$  | $$
|__/      |__/  |__/ \______/  \______/ |__/     \__/ \______/ |__/  |__/|_______/        \______/ |________/|__/  \__/|________/|__/  |__/|__/  |__/   |__/   \______/ |__/  |__/
                                                                                                                                                                                  
                                                                                                                                                                                  
                                                                                                                                                                                  
''')

nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#letters
sum_letters = ""       
for x in range(0,nr_letters):
  random_letters = random.randint(0,len(letters)-1)
  select_letters = letters[random_letters]
  sum_letters += select_letters
# print(sum_letters)

#symbols
sum_symbols = ""      
for x in range(0,nr_symbols):
  random_symbols = random.randint(0,len(symbols)-1)
  select_symbols = symbols[random_symbols]
  sum_symbols += select_symbols
# print(sum_symbols)

#numbers
sum_numbers = ""      
for x in range(0,nr_numbers):
  random_numbers = random.randint(0,len(numbers)-1)
  select_numbers = numbers[random_numbers]
  sum_numbers += select_numbers

password = sum_letters+sum_symbols+sum_numbers
# Easy Method password
# print(f"Here is your password: {password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
list = []
for x in range(0,len(password)):
  list.append(password[x])

random.shuffle(list)

new_password = ""
for x in range(0,len(password)):
  temp = list[x]
  new_password += temp
  

print(f"Here is your password: {new_password}")
input("Press Enter to Close")