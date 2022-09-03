import random

a = True
n = 1

print("Dies ist ein Programm welches es Ihnen einfach machen soll Entscheidungen zu treffen.")
print("Geben Sie die Entscheidung bitte ein.")

antlist = []

while a:
    print("Entscheidung " + str(n) + ": ")          
    antwort = input()                           # Eingabe der Entscheidung als String
    antlist.append(antwort)                     # Hinzufügen der Entscheidung zur Entscheidungs-Liste
    i = input("Weitere Entscheidung? J/N: ")    # Abfrage ob weitere Entscheidungen hinzugefügt werden sollen
    n += 1                                      # Erhöhen des Zählers für Entscheidungsanzahl
    if i == "N":                                # Check ob bei Abfrage (Zeile 15) die zweite Option gewählt wurde -> Programm While-Schleife stoppt bei in diesem Fall     
        break

antwort = random.choice(antlist)                # Pseudozufälliges auswählen einer Entscheidung aus der Liste

print("Entscheidung fiel auf: " + antwort)      # Ausgeben dieser Entscheidung


 
