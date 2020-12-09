import random
import json
import datetime
current_time = datetime.datetime.now()
Geheimzahl = random.randint(0, 30)
attempts = 0

print("Errate die Geheimzahl")

user_name = input("Bitte gib deinen Namen ein: ")

print(f"Hallo {user_name}! Schön, dass du mitspielst!")
print("Du sollst eine Zahl zwischen 0 und 30 erraten.")

with open("ergebnis.txt", "r") as ergebnis_file:
    ergebnis = json.loads(ergebnis_file.read())

print("Beste Ergebnisse: ")
ergebnis_sortiert = sorted(ergebnis, key=lambda k: k['Versuche'])[:3]

for ergebnis_dict in ergebnis_sortiert:
    print(ergebnis_dict["SpielerIn"] + ", " + str(ergebnis_dict["Versuche"]) + " Versuche, Datum: " + ergebnis_dict["Datum"])


while True:
    tipp = int(input("Dein Tipp: "))
    attempts += 1

    if tipp == Geheimzahl:
        ergebnis.append({"SpielerIn": user_name, "Versuche": attempts, "Datum": str(datetime.datetime.now())})
        with open("ergebnis.txt", "w") as ergebnis_file:
            ergebnis_file.write(json.dumps(ergebnis))

        print(f"Super gemacht, {user_name}! Die Geheimzahl ist {Geheimzahl}! Gratuliere!")
        print("Versuche: " + str(attempts))

        break
    elif tipp > Geheimzahl:
        print(f"{tipp} ist leider zu hoch. Probier' es noch einmal! ")
    elif tipp < Geheimzahl:
        print("Diese Zahl ist leider zu niedrig. Probier' es noch einmal! ")
    else:
        print(f"Tut mir leid, {user_name}, dieser Tipp ist ungültig.")