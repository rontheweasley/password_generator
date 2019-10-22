import time
import random
import sys
import pandas as pd

# Preparing lists for generate.

firstText = ['Program ','will ', 'generate ', 'a ', 'strong ', 'password ', 'according ', 'to ', 'your ', 'decision.']
lowerKeys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' 'y', 'z']
upperKeys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
characters = ['!', '#', '$', '%', '&', '/', '?', '*']

withoutCharacter = 0
passLengthControl = 0
password = []
convertPass = " "

print("\t\t\t\t\t Password Generator \n")

time.sleep(1)

for x in firstText:
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.2)

time.sleep(1)

print("\n\n\n(Attention! password needs to be min. 6, max. 15 characters long.)")

time.sleep(3)

passLength = int(input("\nLength of your password : "))

if passLength < 6 or passLength > 15:
    print("Error, try again.")
    sys.exit()

elif passLength >= 6 and passLength <= 15:
    pass

time.sleep(2)

passCharacter = input("\nDo you want characters in your password? : ")

if passCharacter == "yes":
    withoutCharacter = 1

elif passCharacter == "no":
    withoutCharacter = 2

else:
    print("Error, try again.")
    sys.exit()

time.sleep(2)

print("\nPassword generating..\n")

time.sleep(2.5)

# Start to generate password.

while True:

    if passLength == passLengthControl:

        print("Password generated.")
        time.sleep(1.5)
        print("\nYour Password : ",*password, sep="")
        str(password)
        for x in password:
            convertPass += x
        df = pd.DataFrame([convertPass])
        df.to_clipboard(index=False, header=False)
        print("\nAlso password is copied to your clipboard.")
        sys.exit()

    else:

        if withoutCharacter == 1:
            createPass = random.randint(1,4)

            if createPass == 1:
                lowerKey = random.choice(lowerKeys)
                password.append(lowerKey)

            elif createPass == 2:
                upperKey = random.choice(upperKeys)
                password.append(upperKey)

            elif createPass == 3:
                number = random.choice(numbers)
                password.append(number)

            elif createPass == 4:
                character = random.choice(characters)
                password.append(character)

        elif withoutCharacter == 2:

            createPass = random.randint(1, 3)

            if createPass == 1:
                lowerKey = random.choice(lowerKeys)
                password.append(lowerKey)

            elif createPass == 2:
                upperKey = random.choice(upperKeys)
                password.append(upperKey)

            elif createPass == 3:
                number = random.choice(numbers)
                password.append(number)

        else:
            print("Error, try again.")
            sys.exit()

    passLengthControl += 1































