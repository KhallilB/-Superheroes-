class Hero:
    def __init__(self, name, startingHealth = 100):
        '''
        Initalize Superhero class properties
        '''
        pass
            
    def addAbility(self, ability):
        '''Adds Abilities to List'''
        pass
        
    def attack(self):
        ''' 
        Calculates damage from list of abilities.

        This method should call Ability.attack() 
        on every ability in self.abilities and
        return the total.
        '''
        pass
        
    def takeDamage(self, damage):
        ''' 
        This method should update self.current_health 
        with the damage that is passed in.
        '''
        pass
        
    def isAlive(self):
        '''
        This function will 
        return true if the hero is alive 
        or false if they are not. 
        '''
        pass
        
    def fight(self, opponent):
        '''
        Runs a loop to attack the opponent until someone dies.
        '''
        pass

class Ability:
    def __init__(self, name, maxDamage):
        ''' 
        Initialize the values passed into this 
        method as instance variables.
        '''
        pass

    def attack(self):
        ''' 
        Return a random attack value 
        between 0 and max_damage.
        '''
        pass
    
if __name__ == "__main__":
    # If you run this file from the terminal 
    # this block is executed.
    pass