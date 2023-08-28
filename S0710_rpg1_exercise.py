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
import random


class Character:
    def __init__(self, name, max_hp, _current_hp, attackpower, is_alive):
        self.name = name
        self.max_hp = max_hp
        self._current_hp = _current_hp
        self.attackpower = attackpower
        self.is_alive = is_alive

    def __repr__(self):
        return f"Your stats for {self.name} are:\nMax HP: {self.max_hp}\nCurrent HP: {self._current_hp}\nAttack Power: {self.attackpower}"

    def hit(self, character):
        if random.randint(1, 10) != 1:
            print(f"{self.name} attacked {character.name}")
            character.get_hit(self.attackpower)
        else:
            print(f"{self.name} attacked {character.name}, but missed")

    def crit_hit(self, chararcter):
        chararcter.get_hit(self.attackpower * 2)

    def get_hit(self, attackpower):
        self._current_hp -= attackpower
        self.am_i_dead()

    def magic_get_hit(self, magicpower):
        self._current_hp -= magicpower
        self.am_i_dead()

    def get_healed(self, healpower):
        self._current_hp += healpower

    @staticmethod
    def fireball_hit(character, magicpower):
        if random.randint(1, 10) != 1:
            character.magic_get_hit(magicpower * 2)
        else:
            print("A Critical hit")
            character.magic_get_hit(magicpower * 3)

    def common_action(self, character):
        if random.randint(1, 10) != 1:
            print(f"{self.name} attacked {character.name}")
            self.hit(character)
        else:
            print(f"{self.name} attacked {character.name}, but missed")

    def am_i_dead(self):
        if self._current_hp <= 0:
            self.is_alive = False
            print(f"{self.name} has been killed")
        else:
            print(f"{self.name} current hp is: {self._current_hp}")


class Healer(Character):
    def __init__(self, name, max_hp, _current_hp, attackpower, is_alive, healingpower, mana):
        self.healingpower = healingpower
        self.mana = mana
        Character.__init__(self, name, max_hp, _current_hp, attackpower, is_alive)
        self.attackpower = 0

    def __repr__(self):
        return f"Your stats for {self.name} are:\nMax HP: {self.max_hp}\nCurrent HP: {self._current_hp}\nAttack Power: {self.attackpower}\nHealing Power: {self.healingpower}\nMana: {self.mana}"

    def heal(self, character):
        character.get_healed(self.healingpower)

    def pray(self):
        self.mana += 25
        print(f"{self.name} recovered 25 mana by praying")

    def grand_heal(self, character):
        if self.mana >= 50:
            self.mana -= 50
            character.get_healed(self.healingpower * 2.5)
        else:
            print(f"{self.name} tried to use 'grand heal', but had insuffecient mana: {self.mana}")

    def action(self, character):
        if self.mana >= 25:
            character.get_healed(self.healingpower)
        else:
            self.pray()


class Rogue(Character):
    def __init__(self, name, max_hp, _current_hp, attackpower, is_alive, unseen):
        self.unseen = unseen
        Character.__init__(self, name, max_hp, _current_hp, attackpower, is_alive)

    def __repr__(self):
        return f"Your stats for {self.name} are:\nMax HP: {self.max_hp}\nCurrent HP: {self._current_hp}\nAttack Power: {self.attackpower}"

    def ambush(self, character, unseen):
        if unseen:
            print(f"{self.name} ambushed {character.name}")
            self.unseen = False
            self.crit_hit(character)
        else:
            print(f"{self.name} tried to ambush {character.name} but failed")

    def action(self, character):
        if self.unseen:
            self.ambush(character, True)
        else:
            self.common_action(character)


class Mage(Character):
    def __init__(self, name, max_hp, _current_hp, attackpower, is_alive, mana, magicpower):
        self.mana = mana
        self.magicpower = magicpower
        self.attackpower = attackpower
        attackpower = self.attackpower * 0.5
        Character.__init__(self, name, max_hp, _current_hp, attackpower, is_alive)

    def __repr__(self):
        return f"Your stats for {self.name} are:\nMax HP: {self.max_hp}\nCurrent HP: {self._current_hp}\nAttack Power: {self.attackpower}\nMagic Power: {self.magicpower}\nMana: {self.mana}"

    def fireball(self, character):
        if self.mana >= 25:
            self.mana -= 25
            if random.randint(1, 10) != 1:
                print(f"{self.name} used Fireball on {character.name}")
                self.fireball_hit(character, self.magicpower)
            else:
                print(f"{self.name} used Fireball on {character.name}, but missed")
        else:
            print(f"{self.name} tried to cast fireball but had insuffecient mana: {self.mana}")

    def action(self, character):
        if self.mana >= 25:
            self.fireball(character)
        else:
            self.common_action(character)


Riko = Rogue("Riko", 90, 90, 15, True, True)
Flanders = Mage("Flanders", 90, 90, 10, True, 100, 10)
print(Riko)
print()
print(Flanders)
print()

flanders_wins = 0
riko_wins = 0
for i in range(100):
    Riko = Rogue("Riko", 90, 90, 15, True, True)
    Flanders = Mage("Flanders", 90, 90, 10, True, 100, 10)
    if random.randint(1, 2) == 1:
        Riko.unseen = True
        while True:
            Riko.action(Flanders)
            if not Flanders.is_alive:
                riko_wins += 1
                break
            Flanders.action(Riko)
            if not Riko.is_alive:
                flanders_wins += 1
                break
    else:
        Riko.unseen = False
        while True:
            Flanders.action(Riko)
            if not Riko.is_alive:
                flanders_wins += 1
                break
            Riko.action(Flanders)
            if not Flanders.is_alive:
                riko_wins += 1
                break
print(f"Flanders won: {flanders_wins} out of 100")
print(f"Riko won: {riko_wins} out of 100")