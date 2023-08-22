"""Opgave: Objektorienteret rollespil, del 1 :

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Definer en klasse "Character" med attributterne "name", "max_health", "_current_health", "attackpower".
_current_health skal være en protected attribut, det er ikke meningen at den skal kunne ændres udefra i klassen.

Tilføj en konstruktor (__init__), der accepterer klassens attributter som parametre.
Tilføj en metode til udskrivning af klasseobjekter (__repr__).

Tilføj en metode "hit", som reducerer _current_health af en anden karakter med attackpower.
Eksempel: _current_health=80 og attackpower=10: et hit reducerer _current_health til 70.

Metoden hit må ikke ændre den private attribut _current_health i en (potentielt) fremmed klasse.
Derfor definerer vi en anden metode get_hit, som reducerer _current_health for det objekt, som den tilhører, med attackpower.

Tilføj en klasse "Healer", som arver fra klassen Character.
En healer har attackpower=0 men den har en ekstra attribut "healpower".

Tilføj en metode "heal" til "Healer", som fungerer som "hit" men forbedrer sundheden med healpower.
For at undgå at "heal" forandrer den protected attribut "_current_health" direkte,
tilføj en metode get_healed til klassen Character, som fungerer lige som get_hit.

Hvis du er gået i stå, kan du spørge google, de andre elever eller læreren (i denne rækkefølge).
Hvis du ikke aner, hvordan du skal begynde, kan du åbne S0720_rpg1_help.py og starte derfra.

Når dit program er færdigt, skal du skubbe det til dit github-repository
og sammenlign det med lærerens løsning i S0730_rpg1_solution.py

Send derefter denne Teams-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


class Character:
    def __init__(self, name, max_hp, _current_hp, attackpower):
        self.name = name
        self.max_hp = max_hp
        self._current_hp = _current_hp
        self.attackpower = attackpower

    def __repr__(self):
        return f"Your stats for {self.name} are:\nMax HP: {self.max_hp}\nCurrent HP: {self._current_hp}\nAttack Power: {self.attackpower}"

    def hit(self, character):
        character.get_hit(self.attackpower)

    def crit_hit(self, chararcter):
        chararcter.get_hit(self.attackpower*2)

    def get_hit(self, attackpower):
        self._current_hp -= attackpower

    def magic_get_hit(self, magicpower):
        self._current_hp -= magicpower

    def get_healed(self, healpower):
        self._current_hp += healpower

    def fireball_hit(self, character, magicpower):
        character.magic_get_hit(magicpower*2)

class Healer(Character):
    def __init__(self, name, max_hp, _current_hp, attackpower, healingpower, mana):
        self.healingpower = healingpower
        self.mana = mana
        Character.__init__(self, name, max_hp, _current_hp, attackpower)
        self.attackpower = 0

    def heal(self, character):
        character.get_healed(self.healingpower)

    def grand_heal(self, character):
        if self.mana >= 50:
            self.mana -= 50
            character.get_healed(self.healingpower*2.5)
        else:
            print(f"{self.name} tried to use 'grand heal', but had insuffecient mana: {self.mana}")

class Rogue(Character):
    def __init__(self, name, max_hp, _current_hp, attackpower, unseen):
        self.unseen = unseen
        Character.__init__(self, name, max_hp, _current_hp, attackpower)

    def ambush(self, character, unseen):
        if unseen:
            self.unseen = False
            self.crit_hit(character)
        else:
            print(f"{self.name} tried to ambush {character.name} but failed")

class Mage(Character):
    def __init__(self, name, max_hp, _current_hp, attackpower, mana, magicpower):
        self.mana = mana
        self.magicpower = magicpower
        self.attackpower = self.attackpower * 0.5
        Character.__init__(self, name, max_hp, _current_hp, attackpower)

    def fireball(self, character):
        if self.mana >= 25:
            self.mana -= 25
            self.fireball_hit(character, self.magicpower)
        else:
            print(f"{self.name} tried to cast fireball but had insuffecient mana: {self.mana}")



Riko = Character("Riko", 100, 100, 10)
Flanders = Character("Flanders", 100, 100, 10)
Marie = Healer("Marie", 80, 80, 1000, 10, 100)
Flanders.hit(Riko)
Flanders.hit(Riko)
print(Riko)
Marie.heal(Riko)
print(Riko)
print(Marie)
