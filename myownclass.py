#Aidan Isom - Assignment 10.1 - Your Own Class
#The purpose of this assigment is to implement a class based on a real world object. In this case, I made a class to made an extremley simple model of magic cards, from the trading card game magic the gathering.

#Here I define the class MagicCard. I hope I did this according to convention. I know the first letter should be capitalized, but I dont know about the card. Should it be Magiccard or Magic_card or Magic_Card?
class MagicCard:
    #I created some simple identifying features of a magic card. These are the cost (what it costs to play the card from the players hand) and the color of the card. 
    def __init__(self,cost,color = "Colorless"):
        #cardtype should always be magic card. the card will never become a pokemon card or anything
        self._cardtype = "Magic Card"
        self._cost = cost
        self._color = color

    def get_cost(self):
        #This is a simple get method to get the cost of the card
        return str(self._cost)
    def get_type(self):
        #Same as get cost, simple method to get the cardtype
        return self._cardtype
    def get_color(self):
        #Same as get cost, simple method to get the color
        return self._color

#Here I create the creature class. This inherits from magiccard.        
class Creature(MagicCard):
    #This takes in two additional inputs of power and toughness, which is basicly the attack and defense of the creature. 
    def __init__(self,cost,color,power,tough):
        super().__init__(cost,color)
        self._power = power
        self._tough = tough
    #This is a simple method to get the stats of the creature. It presents them in the form of power/toughness, which is the form that they are presented as on the magic card
    def get_stats(self):
        return str(self._power)+"/"+str(self._tough)
    #Simple method to get the power of the create
    def get_power(self):
        return self._power
    #simple method to get the toughness of the creature
    def get_tough(self):
        return self._tough
    #Simple set method to increase the power and toughness of the creature. 
    def buff(self,amount):
        self._power += amount
        self._tough += amount
    #Simple set method to decrease the power and toughness of the creature. I created seperate methods to increase and decrease the power and toughness of the creature because it fits more into the way you would do that in the card game.
    def debuff(self, amount):
        self._power -= amount
        self._tough -= amount
    #Here is the fight command. It has the selected creature fight another selected creature. It outputs a string which tells some of the details of the fight and the final results.
    def fight(self, enemyname):
        enemyhealth = str(enemyname.get_power()-self.get_power())
        myhealth = str(self.get_power() - enemyname.get_power())
        output = "I am a "+str(self.get_stats())+" and my enemy is a "+str(enemyname.get_stats()) + ". "
        output = output + "I do "+str(self.get_power()) + " damage to my enemy, leaving them at " + enemyhealth + " health."
        if int(enemyhealth) <= 0:
            output = output + " This kills the enemy."
        output = output + " The enemy does " + str(enemyname.get_power()) + " damage to me, leaving me at " + myhealth + " health."
        if int(myhealth) <= 0:
            output = output + " This kills me. I am very sad."
        return output

#Here is another class, which is spell. The spell in this case does just damage to a creature. It also inherets from magic card. the only additional argument is damage.
class Spell(MagicCard):
    def __init__(self,cost,color,damage):
        super().__init__(cost,color)
        self._damage = damage
    #simple get method to get the damage of the spell
    def get_damage(self):
        return self._damage
    #This is the cast function. It simply casts the spell onto a creature. It returns a string which contains the result of the spell.
    def cast(self, targetname):
        targethealth = targetname.get_tough() - self.get_damage()
        output = "The spell does " + str(self._damage) + " damage to the target, leaving it at " + str(targethealth) + " health."
        if targethealth <=0:
            output = output + " This kills the target." 
        return output


#I know it said for the demo code to not just print a list of strings, but that is kind of the main point of my class, is to tell how the fights go by returning strings.
def main():
    #Here, I create a goblin. It costs 2 mana, it is a magic card, it is red, and it has 3 power and 2 defense
    goblin = Creature(2,"Red",3,2)
    #Here, I create a wolf. It is a 4 mana green creature with 4 power and toughness
    wolf = Creature(5,"Green",5,5)
    #Here, I have the goblin fight the wolf. This outputs a string that tells me about the fight. The goblin loses
    print(goblin.fight(wolf))
    #Here, I create a fireball. It is a 1 mana red spell that does 2 damage 
    fireball = Spell(1,"Red",2)
    #Here, I cast the fireball on the goblin. This also kills the goblin
    print(fireball.cast(goblin))
    #I feel like the goblin has been getting killed too much, so here I buff the goblin by 2. This increases the goblins power and toughness by 2. Here, I show the goblins stats before and after the buff.
    print("The goblin was a " + str(goblin.get_stats()))
    goblin.buff(2)
    print("Now it is a " + str(goblin.get_stats()))
    #I cast the fireball on the goblin again. This time the goblin lives.
    print(fireball.cast(goblin))
    #The goblin is still not strong enough to fight the wolf. I will debuf the wolf so that the goblin can win. Here are the stats of the wolf before and after it is debuffed.
    print("The wolf was a " + str(wolf.get_stats()))
    wolf.debuff(2)
    print("Now it is a " + str(wolf.get_stats()))
    #Here I have the goblin fight the wolf again. This time, the goblin wins, since he is buffed and the wolf is debuffed.
    print(goblin.fight(wolf))


#Here I run the main
if __name__ == "__main__":
    main()