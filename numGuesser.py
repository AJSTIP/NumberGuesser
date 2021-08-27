import random

print(
    "\t \n If Computers are so good they should be able to easily guess a number right? I surly think so, the computer should Impress us."
)

tries = 1

correct_num = int(input("Human playing this pick a number 1-100 Please. "))

computer = random.randint(0, 100)

while correct_num > 100:
    correct_num = int(
        input(
            "We are suppose to be smarter than them! \n Please enter a different number... "
        )
    )

if correct_num <= 100:
    print("Ah, Perfect")

while computer != correct_num:
    if computer > correct_num:
        print(computer, "Not so high there magical computer")
    else:
        print(computer, "You need to go higher than that magical box full of componets")
        computer = int(random.randint(0, 100))
        tries += 1

print(
    "\t \n Woah Mr Computer finally got the number. The correct number was ",
    correct_num,
)
print("It only took the computer", tries, "tries to get the corrct answer........")
input("\n You may press the enter key to exit. Thank you for playing.")