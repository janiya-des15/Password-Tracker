# Password Manager 
import random
import string


def store_password():
  username = str(input("Your username: "))
#website
  website = str(input("Website: "))
#generate random Password
  digit = int(input("How many digit do you want? (integer only)"))
  password = ""
  for i in range(digit):
    char = random.choice(string.ascii_letters)
    password += char 
  #hash the password
  #generate a salt
  #store the password into a file

  f = open("password.txt", "a")
  f.write(f"{username}-{website}-{str(password)}\n")
  f.close()
  

  print(f"Here's ypur password: {password}")

######
def look_up():
  username_or_website = str(input("Do you want to look up the username or website?"))
  value = str(input("What value? "))
  #look_up by username
  f = open("password.txt", "r")
  for line in f:
    if username_or_website == "username":
      info = line.split("-")
      if value == info[0]:
        return info[2]
    else:
      #look_up by website
      if value == info[1]:
        return info[2]
      


# store_password()
result = look_up()

if result == None:
  print("No result found")
else:
  print(f" Here's your password: {result}")

""""
Salt: made up of random bits(0,1) added to each password instance before its hashing.(auth0.com)

"""