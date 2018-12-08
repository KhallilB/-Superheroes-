import random


class Ability:
    def __init__(self, name, attackPower):
        self.name = name
        self.attackPower = int(attackPower)

    def attack(self):
        minAttack = self.attackPower // 2
        # Use random.randint(a, b) to select a random attack value.
        attack = random.randint(minAttack, self.attackPower)
        # Return attack value between 0 and the full attack.
        return attack

    def updateAttack(self, attackPower):
        self.attackPower = attackPower


class Hero:
    def __init__(self, name, health=100):
        self.abilities = list()
        self.name = name
        self.weapons = list()
        self.armors = list()
        self.startHealth = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def addAbility(self, ability):
        # Append ability to self.abilities
        self.abilities.append(ability)

    def addArmor(self, armor):
        # Append ability to self.abilities
        self.armors.append(armor)

    def addWeapons(self, weapon):
        # Append ability to self.abilities
        self.weapons.append(weapon)

    def attack(self):
        # Call the attack method on every ability in our ability list
        # Add up and return the total of all attacks
        allAttacks = 0

        for ability in self.abilities:

            allAttacks += ability.attack()

        return allAttacks

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

    def takeDamage(self, damagePoints):
        """
        This method should subtract the damage amount from the 
        hero's health. 
        If the hero dies update number of deaths.
        """

        self.health -= damagePoints

        if self.health <= 0:
            self.deaths += 1

    def addKill(self, kills):
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
        attack = random.randint(0, self.attackPower)
        return attack


class Team:
    def __init__(self, teamName):
        """Instantiate resources."""
        self.name = teamName
        self.heroes = list()

    def addHero(self, Hero):
        """Add Hero object to heroes list."""
        self.heroes.append(Hero)

    def removeHero(self, name):
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

    def findHero(self, name):
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

    def seeHeroes(self):
        """Print out all heroes to the console."""
        for hero in self.heroes:
            print(hero.name)

    def attack(self, otherTeam):
        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.
        It should call add_kill() on each hero with the number of kills made.
        """
        totalTeamPower = 0

        for heros in self.heroes:
            totalTeamPower += heros.attack()

        kills = otherTeam.defend(totalTeamPower)

        for heros in self.heroes:
            heros.addKill(kills)

    def defend(self, damageAmt):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.
        Return number of heroes killed in attack.
        """
        totalTeamDefense = 0

        for hero in self.heroes:
            totalTeamDefense += hero.defend()

        extraDamage = damageAmt - totalTeamDefense

        if extraDamage > 0:
            killAmount = self.dealDamage(extraDamage)
            return killAmount
        else:
            return 0

    def dealDamage(self, damage):
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
            hero.takeDamage(even)
            if hero.health <= 0:
                died += 1
        return died

    def reviveHeroes(self, health=100):
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

    def updateKills(self):
        """
        This method should update each hero when there is a team kill.
        """
        for hero in self.heroes:
            if hero.health <= 0:
                hero.addKill()


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
        defendStrength = random.randint(0, int(self.defense))

        return defendStrength


class Arena:
    def __init__(self):
        self.teamOne = None
        self.teamTwo = None

    def buildTeamOne(self):
        """
        This method should allow a user to build team one.
        """
        teamOneName = input("Enter a name for Team One: \n")
        self.teamOne = Team(teamOneName)

        teamOne = True
        index = 0

        while teamOne:
            self.teamOne.addHero(
                Hero(input("Create A Name for a New Hero: \n")))
            self.teamOne.heroes[index].addAbility(Ability(input(
                "Name your Heros ability: "), input("How powerful? 200(weak)- 600(strong): \n")))
            self.teamOne.heroes[index].addArmor(Armor(input("Name your new armor:"), input(
                "How strong is it? 50(weak)- 200(strong): \n")))

            end = input(
                "To add more heros type \"NEW\" else type any key and press enter: \n")

            if end == "NEW":
                teamOne = True
            else:
                teamOne = False

            index += 1

    def buildTeamTwo(self):
        """
        This method should allow user to build team two.
        """
        teamTwoName = input("\nEnter a name for Team Two: \n")
        self.teamTwo = Team(teamTwoName)

        teamTwo = True
        index = 0

        while teamTwo:
            self.teamTwo.addHero(
                Hero(input("Create A Name for a New Hero: \n")))
            self.teamTwo.heroes[index].addAbility(Ability(input(
                "Name your Heros ability: "), input("How powerful? 200(meh)- 600(crazy powerful): \n")))
            self.teamTwo.heroes[index].addArmor(Armor(input("Name your new armor: "), input(
                "How strong is it? 50(meh)- 200(crazy strong): \n")))

            end = input(
                "To add more heros type \"NEW\" else type any key and press enter: \n")

            if end == "NEW":
                teamTwo = True
            else:
                teamTwo = False

            index += 1

    def teamBattle(self):
        """
        This method should continue to battle teams until 
        one or both teams are dead.
        """
        self.teamOne.attack(self.teamTwo)
        self.teamTwo.attack(self.teamOne)

    def showStats(self):
        """
        This method should print out the battle statistics 
        including each heroes kill/death ratio.
        """
        self.teamOne.stats()
        self.teamTwo.stats()


if __name__ == "__main__":
    gameIsRunning = True

    arena = Arena()

    arena.buildTeamOne()
    arena.buildTeamTwo()

    while gameIsRunning:

        arena.teamBattle()
        arena.showStats()
        playAgain = input("\nPlay Again? Y or N: ")

        # Check for Player Input
        if playAgain.lower() == "n":
            gameIsRunning = False

        else:
            # Revive heroes to play again
            arena.teamOne.reviveHeroes()
