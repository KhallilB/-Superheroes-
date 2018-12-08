import random


class Ability:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = int(attack_power)

    def attack(self):
        min_attack = self.attack_power // 2
        # Use random.randint(a, b) to select a random attack value.
        attack = random.randint(min_attack, self.attack_power)
        # Return attack value between 0 and the full attack.
        return attack

    def update_attack(self, attack_power):
        self.attack_power = attack_power


class Hero:
    def __init__(self, name, health=100):
        self.abilities = list()
        self.name = name
        self.weapons = list()
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        # Append ability to self.abilities
        self.abilities.append(ability)

    def add_armor(self, armor):
        # Append ability to self.abilities
        self.armors.append(armor)

    def add_weapons(self, weapon):
        # Append ability to self.abilities
        self.weapons.append(weapon)

    def attack(self):
        # Call the attack method on every ability in our ability list
        # Add up and return the total of all attacks
        all_attacks = 0

        for ability in self.abilities:

            all_attacks += ability.attack()

        return all_attacks

    def defend(self):
        """
        This method should run the defend method on each piece of armor and calculate the total defense. 
        If the hero's health is 0, the hero is out of play and should return 0 defense points.
        """

        defense = 0

        if len(self.armors) != 0:
            for armor in self.armors:

                defense += armor.defend()
        else:
            return defense

        if self.health == 0:
            defense = 0
            return defense
        else:
            return defense

    def take_damage(self, damage_points):
        """
        This method should subtract the damage amount from the 
        hero's health. 
        If the hero dies update number of deaths.
        """

        self.health -= damage_points

        if self.health <= 0:
            self.deaths += 1

    def add_kill(self, kills):
        """
        This method should add the number of kills to self.kills
        """
        self.kills += kills


class Weapon(Ability):
    def attack(self):
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        Hint: The attack power is inherited.
        """
        attack = random.randint(0, self.attack_power)
        return attack


class Team:
    def __init__(self, team_name):
        """Instantiate resources."""
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        """Add Hero object to heroes list."""
        self.heroes.append(Hero)

    def remove_Hero(self, name):
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        if len(self.heroes) == 0:
            return 0

        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
            else:
                return 0

    def find_Hero(self, name):
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """
        if len(self.heroes) == 0:
            return 0

        for hero in self.heroes:
            if name == hero.name:
                return hero
            else:
                return 0

    def see_Heroes(self):
        """Print out all heroes to the console."""
        for hero in self.heroes:
            print(hero.name)

    def attack(self, otherTeam):
        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.
        It should call add_kill() on each hero with the number of kills made.
        """
        total_team_power = 0

        for heros in self.heroes:
            total_team_power += heros.attack()

        kills = otherTeam.defend(total_team_power)

        for heros in self.heroes:
            heros.add_kill(kills)

    def defend(self, damage_amt):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.
        Return number of heroes killed in attack.
        """
        total_team_defense = 0

        for hero in self.heroes:
            total_team_defense += hero.defend()

        ex_damage = damage_amt - total_team_defense

        if ex_damage > 0:
            kill_amt = self.deal_damage(ex_damage)
            return kill_amt
        else:
            return 0

    def deal_damage(self, damage):
        """
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack.
        """

        died = 0

        if len(self.heroes) == 0:
            even = damage
        else:
            even = damage // len(self.heroes)

        for hero in self.heroes:
            hero.take_damage(even)
            if hero.health <= 0:
                died += 1
        return died

    def revive_heroes(self, health=100):
        """
        This method should reset all heroes health to their
        original starting value.
        """
        for hero in self.heroes:
            hero.health = health

    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen. 
        This data must be output to the terminal.
        """

        for hero in self.heroes:
            print("Team: {}\n".format(self.name))
            print("{} kills:{} death: {} ".format(
                hero.name, hero.kills, hero.deaths))

    def update_kills(self):
        """
        This method should update each hero when there is a team kill.
        """
        for hero in self.heroes:
            if hero.health <= 0:
                hero.add_kill()


class Armor:
    def __init__(self, name, defense):
        """Instantiate name and defense strength."""
        self.name = name
        self.defense = defense

    def defend(self):
        """
        Return a random value between 0 and the 
        initialized defend strength.
        """
        defend_strength = random.randint(0, int(self.defense))

        return defend_strength


class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """
        team_one_name = input("Enter a name for Team One: \n")
        self.team_one = Team(team_one_name)

        team_one = True
        index = 0

        while team_one:
            self.team_one.add_hero(
                Hero(input("Create A Name for a New Hero: \n")))
            self.team_one.heroes[index].add_ability(Ability(input(
                "Name your Heros ability: "), input("How powerful? 200(weak)- 600(strong): \n")))
            self.team_one.heroes[index].add_armor(Armor(input("Name your new armor:"), input(
                "How strong is it? 50(weak)- 200(strong): \n")))

            end = input(
                "To add more heros type \"NEW\" else type any key and press enter: \n")

            if end == "NEW":
                team_one = True
            else:
                team_one = False

            index += 1

    def build_team_two(self):
        """
        This method should allow user to build team two.
        """
        team_two_name = input("\nEnter a name for Team Two: \n")
        self.team_two = Team(team_two_name)

        team_two = True
        index = 0

        while team_two:
            self.team_two.add_hero(
                Hero(input("Create A Name for a New Hero: \n")))
            self.team_two.heroes[index].add_ability(Ability(input(
                "Name your Heros ability: "), input("How powerful? 200(meh)- 600(crazy powerful): \n")))
            self.team_two.heroes[index].add_armor(Armor(input("Name your new armor: "), input(
                "How strong is it? 50(meh)- 200(crazy strong): \n")))

            end = input(
                "To add more heros type \"NEW\" else type any key and press enter: \n")

            if end == "NEW":
                team_two = True
            else:
                team_two = False

            index += 1

    def team_battle(self):
        """
        This method should continue to battle teams until 
        one or both teams are dead.
        """
        self.team_one.attack(self.team_two)
        self.team_two.attack(self.team_one)

    def show_stats(self):
        """
        This method should print out the battle statistics 
        including each heroes kill/death ratio.
        """
        self.team_one.stats()
        self.team_two.stats()


if __name__ == "__main__":
    game_is_running = True

    arena = Arena()

    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        playAgain = input("\nPlay Again? Y or N: ")

        # Check for Player Input
        if playAgain.lower() == "n":
            game_is_running = False

        else:
            # Revive heroes to play again
            arena.team_one.revive_heroes()
