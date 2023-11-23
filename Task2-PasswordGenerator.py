import random as rd

print("\t\t\t ---------------- Password Generator ----------------\n")
size = int(input("Enter the desired size of the password: "))
complexity = input("Enter the complexity level (low or medium or high): ")
pattern = list()
if complexity == "low":
    pattern += list("abcdefghijklmnopqrstuvwxyz")
elif complexity == "medium":
    pattern += list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
elif complexity == "high":
    pattern += list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")

if complexity != "low" and complexity != "medium":
    sp_symbol = rd.choice('@$#*:')
    sp_pos = rd.randint(1, size - 1)
else:
    sp_symbol = ""
    sp_pos = -1

password = [rd.choice(pattern) for i in range(size)]
if sp_pos > 0:
    password[sp_pos] = sp_symbol
password = ''.join(password)
print()
print("Generated Password is: ", password)


