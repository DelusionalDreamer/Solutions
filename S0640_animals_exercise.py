"""
Opgave "Animals"

Som altid skal du læse hele øpgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Alt, hvad du har brug for at vide for at løse denne opgave, finder du i cars_oop-filerne.

Definer en klasse ved navn Animal.
Hvert objekt i denne klasse skal have attributterne name (str), sound (str), height (float),
weight (float), legs (int), female (bool).
I parentes står data typerne, dette attributterne typisk har.

Tilføj til klassen meningsfulde metoder __init__ og __repr__.
Kald disse metoder for at oprette objekter af klassen Animal og for at udskrive dem i hovedprogrammet.

Skriv en klassemetode ved navn make_noise, som udskriver dyrets lyd i konsollen.
Kald denne metode i hovedprogrammet.

Definer en anden klasse Dog, som arver fra Animal.
Hvert objekt af denne klasse skal have attributterne tail_length (int eller float)
og hunts_sheep (typisk bool).

Tilføj til klassen meningsfulde metoder __init__ og __repr__.
Ved skrivning af konstruktoren for Dog skal du forsøge at genbruge kode fra klassen Animal.
Kald disse metoder for at oprette objekter af klassen Hund og for at udskrive dem i hovedprogrammet.

Kald metoden make_noise på Dog-objekter i hovedprogrammet.

Skriv en klassemetode ved navn wag_tail for Dog.
Denne metode udskriver i konsollen noget i stil med
"Hunden Snoopy vifter med sin 32 cm lange hale"
Kald denne metode i hovedprogrammet.

Skriv en funktion mate(mother, father). Begge parametre er af typen Dog.
Denne funktion skal returnere et nyt objekt af typen Dog.
I denne funktion skal du lave meningsfulde regler for den nye hunds attributter.
Hvis du har lyst, brug random numbers så mate() producerer tilfældige hunde.
Sørg for, at denne funktion kun accepterer hunde med det korrekte køn som argumenter.

I hovedprogrammet kalder du denne metode og udskriver den nye hund.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
import random

random.seed(1, 2)
class Animal:
    def __init__(self, name, sound, height, weight, legs, female):
        self.name = name
        self.sound = sound
        self.height = height
        self.weight = weight
        self.legs = legs
        self.female = female

    def __repr__(self):
        return f"{self.name} has {self.legs} legs, a weight of {self.weight}kg and a height of {self.height}cm.\nIt makes the sound {self.sound}. Is it a Female: {self.female}\n"

    def make_noise(self):
        print(f"{self.sound}, {self.sound}")


class Dog(Animal):

    def __init__(self, name, sound, height, weight, legs, female, tail_length, hunts_sheep):
        self.tail_length = tail_length
        self.hunts_sheep = hunts_sheep
        Animal.__init__(self, name, sound, height, weight, legs, female)

    def __repr__(self):
        return (f"{self.name} has {self.legs} legs, a weight of {self.weight}kg and a height of {self.height}cm.\nIt makes the sound {self.sound}. Is it a Female: {self.female}\n"
                f"It´s tail is {self.tail_length}cm long. does it hunt sheep?: {self.hunts_sheep}\n")

    def wag_tail(self):
        return print(f"{self.name} wags it´s {self.tail_length}cm long tail, it appears to be happy\n")

    @staticmethod
    def mate(mother, father):
        if mother.female and not father.female:
            if father.height < mother.height:
                child_height = random.randint(father.height, mother.height)
            else:
                child_height = random.randint(mother.height, father.height)
            if father.weight < mother.weight:
                child_weight = random.randint(father.weight, mother.weight)
            else:
                child_weight = random.randint(mother.weight, father.weight)
            if father.tail_length < mother.tail_length:
                child_tail_length = random.randint(father.tail_length, mother.tail_length)
            else:
                child_tail_length = random.randint(mother.tail_length, father.tail_length)
            if random.randint(0, 1) == 0:
                child_female = True
            else:
                child_female = False
            if random.randint(0, 1) == 0:
                child_hunts_sheep = True
            else:
                child_hunts_sheep = False
            return Dog("not named", "Woof", child_height, child_weight, 4, child_female, child_tail_length, child_hunts_sheep)
        else:
            return f"There isn´t a mother and father"


cat = Animal("balter", "Meow", 80, 35, 4, False)
print(cat)
cat.make_noise()

dog1 = Dog("Bjef", "woof", 50, 20, 4, False, 50, True)
dog2 = Dog("Bjaf", "woof", 20, 5, 4, True, 20, False)
print(dog1)
print(dog2)
dog1.make_noise()
dog1.wag_tail()
print(Dog.mate(dog2, dog1))
