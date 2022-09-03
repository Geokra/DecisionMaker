import random

a = True
n = 1

print("Dies ist ein Programm welches es Ihnen einfach machen soll Entscheidungen zu treffen.")
print("Geben Sie Ihre möglichen Entscheidungen bitte mit ',' getrennt ein")

antlist = []

while a:
    print("Entscheidung " + str(n) + ": ")
    antwort = input()
    antlist.append(antwort)
    i = input("Weitere Entscheidung? J/N: ")
    n += 1
    if i == "N":
        break

antwort = random.choice(antlist)

print("Entscheidung fiel auf: " + antwort)


 