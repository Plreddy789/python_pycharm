for i in range(1,101):
    if i%3==0 and i%5==0:
        print("fizz buzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)


# PASSWORD GENERATOR
import random
import string
letters=int(input("how many letter do you want in your password :"))
symbols=int(input("how many symbols do you want :"))
numbers=int(input("how many numbers do you want :"))
password_length=int(letters+symbols+numbers)
password=""
characters=string.ascii_letters+string.digits+string.punctuation

for i in range(password_length):
    password+=''.join(random.choice(characters))

print(password)
