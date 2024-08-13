#You own an online shop where you sell rings with custom engravings. You offer both gold plated and solid gold rings.

#Gold plated rings have a base cost of $50, and you charge $7 per engraved unit.
#Solid gold rings have a base cost of $100, and you charge $10 per engraved unit.
#Spaces and punctuation are counted as engraved units.
#Write a function cost_of_project() that takes two arguments:

#engraving - a Python string with the text of the engraving
#solid_gold - a Boolean that indicates whether the ring is solid gold

def cost_of_project(solid_gold, engraving):
    cost = 50 + (50 * solid_gold) + (7 + (3 * solid_gold)) * len(engraving)
    return str(cost)

engraving = input("what do you want to engrave on the ring:")
gold = input("what type of rings do you want (gold plated or solid gold):")

if gold.lower() is "solid gold":
    gold = True
else:
    gold = False

print("the cost of your ring is: " + cost_of_project(gold, engraving) + "$")
