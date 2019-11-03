from config import *

#Weapon def __init__(self, Damage, Recoil, DiceAtackMin, Durability, Subtype, Name):
Hand=Weapon(0.5, 0, 80, -1, "HandToHand", "Hand")
#Swords
WoodenSword=Weapon(1, 0, 70, 10, "Sword", "WoodenSword")
IronSword=Weapon(1.5, 0, 60, 10, "Sword", "IronSword")
SteelSword=Weapon(1.5, 0, 70, 5, "Sword", "SteelSword")
SilverSword=Weapon(1.5, 0, 70, 10, "Sword", "SilverSword")
LeadSword=Weapon(1.5, 0, 70, 10, "Sword", "LeadSword")
GoldSword=Weapon(3, 0.5, 60, 15, "Sword", "GoldSword")
CobaltSword=Weapon(3, 0, 65, 15, "Sword", "CobaltSword")
TungstenSword=Weapon(2.5, 0.5, 65, 20, "Sword", "TungstenSword")
OrcSword=Weapon(1.5, 0, 70, 5, "Sword", "OrcSword")
DraculaSword=Weapon(1.5, -0.1, 65, -1, "Sword", "DraculaSword")
#Daggers
BrassDagger=Weapon(2, 0, 80, 10, "Dagger", "BrassDagger")
CopperDagger=Weapon(5, 0, 75, 10, "Dagger", "CopperDagger")
GoblinDagger=Weapon(3, 0, 80, 10, "Dagger", "GoblinDagger")
FleaManDagger=Weapon(3, 0, 85, 5, "Dagger", "FleaManDagger")
VampireDagger=Weapon(1, 0, 70, 10, "Dagger", "VampireDagger")
#Food
ChamomileSubstance=Food(1, "Restore", "ChamomileSubstance")
RatMeat=Food(0.5, "Restore", "RatMeat")
Hamburguer=Food(2, "Restore", "Hamburguer")
ElficBread=Food(1, "Up", "ElficBread")
#Armor
NudeBreastplate=Armor(0, 0, 0, -1, "Breastplate", "NudeBreastplate")
NudeGreaves=Armor(0, 0, 0, -1, "Greaves", "NudeGreaves")
LeatherBreastplate=Armor(0, 0, 0, 10, "Breastplate", "LeatherBreastplate")
LeatherGreaves=Armor(0, 0, 0, 10, "Greaves", "LeatherGreaves")
#Lista
###########################FALTAN PONER FOOD Y ARMOR
List=[Hand, WoodenSword, IronSword, SteelSword, SilverSword, LeadSword, GoldSword, CobaltSword, TungstenSword, OrcSword, DraculaSword, BrassDagger, CopperDagger, GoblinDagger, FleaManDagger, VampireDagger, ChamomileSubstance, RatMeat, Hamburguer, ElficBread, NudeBreastplate, NudeGreaves, LeatherBreastplate, LeatherGreaves]
#RawMaterial
DragonFlame=RawMaterial("DragonFlame", "To melt any metal... In a Vial")
Wood=RawMaterial("Wood", "Very useful")
#Begin Metals Raw Material
Steel=RawMaterial("Steel", "Not bad")
Iron=RawMaterial("Iron", "Well well")
Brass=RawMaterial('Brass', "Do you want bullets? Or what?") #Material of bullets (Only weapons)
Bronze=RawMaterial("Bronze", "Uck")
Gold=RawMaterial("Gold", "I'm millonaire")
Silver=RawMaterial("Silver", "Well, mititmiti")
Lead=RawMaterial("Lead", "Do you like fish?")
Zinc=RawMaterial("Zinc", "Jiji")
Copper=RawMaterial("Copper", "...")
Nickel=RawMaterial("Nickel", "EM...")
Aluminum=RawMaterial("Aluminum", "WUJU") #Only armor
Mitril=RawMaterial("Mitril", "Very resistent") #Only armor
Cobalt=RawMaterial("Cobalt", "It's beautiful")
Tungsten=RawMaterial("Tungsten", "It's very heavyyyy")
#End Metals Raw material
Chisel=RawMaterial("Chisel", "To make the Wood take any shape") #Cincel para tallar madera
RopeCord=RawMaterial("RopeCord", "Make bow? Maybe")
