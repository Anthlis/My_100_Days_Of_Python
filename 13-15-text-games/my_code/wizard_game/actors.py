import random


class Creature:

    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return f"Creature {self.name} of level {self.level}"

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):

    def __init__(self, name, the_level):
        super().__init__(name, the_level)


    def attack(self, creature):
        print(f'The wizard {self.name} attacks {creature.name}!')

        # my_roll = random.randint(1, 12) * self.level
        my_roll = creature.get_defensive_roll()
        # creature_roll = random.randint(1, 12) * self.level
        creature_roll = creature.get_defensive_roll()

        print(f'You roll {my_roll}')
        print(f'{creature.name} rolls {creature_roll}')

        if my_roll >= creature_roll:
            print(f'The Wizard has handily triumphed over {creature.name}')
            print()
            return True
        else:
            print(f'The Wizard has been DEFEATED')
            print()


class SmallAnimal(Creature):

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2

class Dragon(Creature):

    def __init__(self, name, level, scaliness, breathes_fire):
        super().__init__(name, level)
        self.breathes_fire = breathes_fire
        self.scaliness = scaliness

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breathes_fire else 1
        scale_modifier = self.scaliness / 10

        return base_roll * fire_modifier * scale_modifier





