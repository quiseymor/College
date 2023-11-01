import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

password_length = int(input("Enter the number of characters in the password: "))

password = ""

while len(password) < password_length:
    password += random.choice(chars)

print("Generated password:", password)
