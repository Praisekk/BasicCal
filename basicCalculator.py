"""
Basic calculator done with functions using python 3
****PRAISEkk****
"""
print("\t Welcome! \n\t we are gonna work some basic maths here... \n\t fist we need about two numbers from you to do this *smiles")
first_number = int(input("First number from you: > "))
print("\t remember i said two numbers!!! didn\'t i?? \n\t LOL!! kidding my bad i\'m just a computer dumb as fuck")
print("Hit retun to continue")
input()
second_number = int(input("okay the second number... still from you lol: > "))
print("\t Okay that\'s gonna do the job lol")
print("\t basically what we wanna do with this is just to: \n\t\t ADD, SUBTRACT, MULTIPLY, DIVIDE \n\t\t *wait what else \n\t\t *thinking.... \n\t\t oh nothing lol")


def Add_number():
    answer = first_number + second_number
    print("Heres your answer: %d"%answer)

def SUBTRACT_numbers():
    answer = first_number - second_number
    print("Heres your answer: %d"%answer)
    
def MULTIPLY_numbers():
    answer = first_number * second_number
    print("Heres your answer: %d"%answer)
    
def DIVIDE_numbers():
    answer = first_number / seconf_number
    print("Heres your answer: %d"%answer)

print("\t so i cant do anything if you don\'t tell me what to do")
print("\t hit: \n\t\t 1 for adding them both \n\t\t 2 for subtracting the numbers \n\t\t 3 for multiplying it \n\t\t 4 for dividing them \n\t\t or just hit 0 for quiting")

reply = int(input("Your choice > "))

if reply == 1:
    Add_numbers()
elif reply == 2:
    SUBTRACT_numbers()
elif reply == 3:
    MULTIPLY_numbers()
elif reply == 4:
    DIVIDE_numbers()
elif reply == 0:
    exit(0)
else:
    print("who\'s dumb now lol simple instruction you never follow.")
    