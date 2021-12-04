github link: https://github.com/aisom1/Assignment-10.1-Your-Own-Class

This class is a very simple approximation of magic cards. Magic Cards are from the trading card game magic the gathering, and their whole point is to fight with eachother. 
As magic is an incredibly complicated game, I just wanted to embody the most important ideas in the code. With this Magic Card class, you can create different cards, buff and debuff them, and have them fight eachother. 
There are two child classes that inherit from the magic card class, which are the creature and the spell class. The creature class represents a creature, and it has attack and defense. It can deal damage and take damage.
A spell is just a card that causes an effect. In this case, I just had the spells do damage. The spells cannot take damage, as they are spells and not creatures.

CLASS VARIABLES AND DATA VARIABLES

The 1 class variable for the magic card is simply the card type. This is always equal to magic card, as it is always a magic card, never a pokemon card or something
There are 2 data variables for magic card. They are cost and color. All magic cards have a cost in mana. You have to pay that cost to play them from your hand and into the game. The cost variable stores that mana cost.
All magic cards have a color as well. This usualy represents what mana can be used to play that card. The possible colors are red, green, white, blue, and black. There are also colorless cards, and that is what the color variable defaults to. Color should always be a string
You can get all of these values with the get_(name of the value) command. For example, get_cost() will return the cost.
For creature, there are two new class variables. These are power and toughness. They represent how much damage and health the creature has. They should always be stored as ints.
For spell, there is one new class variable, which is damage. This is how much damage the spell does. It should always be an int.

METHODS

get_cost(): This takes no arguments. All it does is reutrn the mana cost of the card. 
get_color(): This takes no arguments. All it does is reutrn the color of the card. 
get_stats(): This takes no arguments. This returns the combination of power and tougness, formated as power/toughness.
get_power(): This takes no arguments. This simply returns the power of the creature. 
get_tough(): This takes no arguments. This simply returns the toughness of the creature.
get_damage(): This takes no arguments. This simply returns the damage of the spell.
buff(x): This takes 1 argument, which should be an int. This increases the power and toughness of the creature it is being used on by x.
debuff(x): This takes 1 argument, which should be an int. This decreases the power and toughness of the creature it is being used on by x.
fight(x): This takes 1 argument, which should be the name of a creature. This has the two creatures fight, in which essentialy each creature deals damage equal to its power to the other creature. If the creatures health is below zero it dies. This returns a string that tells the details and results of a fight.
cast(x): This takes 1 argument, which should be the name of a creature. This casts whatever spell it is being used on to attack creature x. It deals damage equal to its damage value to the creature. If the creatures health is below zero it dies. This returns a string that tells the details of the spell cast.

DEMO PROGRAM

The demo program is a simple list of print statements that demonstrates the ways that the above methods can be used. 
In the demo program, the first thing that happens are a goblin creature and a wolf creature are created. They have different colors, mana costs, power, and toughness.
The next thing that happens is they fight eachother. In this case, the wolf wins because it had better stats.
Next, a spell is demonstrated. A spell is created. The spell also has mana, color, and damage.
The spell is cast on the goblin, which kills it. This is shown through printing the spell method.
Finaly, buff and debuff are demonstrated. The goblin is buffed so that it can survive the spell.
This is done through goblin.buff(2). The wolf is then debuffed so that the goblin can win against it. This is done through wolf.debuff(2)
There are print statements throughout the whole thing to explain what is happening.

INSTRUCTIONS

There are no extra steps that must be taken to run this demo program. It has nothing that needs to be downloaded, or modules that need to be imported.