"""
Opgave "Cars":

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Definer en funktion drive_car(), der udskriver en bils motorlyd (f.eks. "roooaar")

I hovedprogrammet:
    Definer variabler, som repræsenterer antallet af hjul og den maksimale hastighed for 2 forskellige biler
    Udskriv disse egenskaber for begge biler
    Kald derefter funktionen motorlyd

Hvis du ikke har nogen idé om, hvordan du skal begynde, kan du åbne S0420_cars_help.py og starte derfra.
Hvis du går i stå, kan du spørge google, de andre elever eller læreren (i denne rækkefølge).
Hvis du stadig er gået i stå, skal du åbne S0430_cars_solution.py og sammenligne den med din løsning.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Team-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


def drive_car():
    print("VROOOM")


go_kart_wheels = 4
go_kart_max_speed = 80
motercykel_wheels = 2
motercykel_max_speed = 180

print(f"GoKart: Number of wheels: {go_kart_wheels} max speed: {go_kart_max_speed}km")
drive_car()
print(f"Motercykel: Number of wheels: {motercykel_wheels} max speed: {motercykel_max_speed}km")
drive_car()
