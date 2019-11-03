from copy import copy
from random import randint
import time
import os

class Weapon:
	"""docstring for Weapon"""
	def __init__(self, Damage, Recoil, DiceAttackMin, Durability, Subtype, Name):
		self.Damage=Damage
		self.Recoil=Recoil#To Character
		self.DiceAttackMin=DiceAttackMin
		self.Durability=Durability
		self.Durability_Max=Durability
		self.Type="Weapon"
		self.Subtype=Subtype
		self.Name=Name
		
class Food:
	"""docstring for Food"""
	def __init__(self, Health_Property, Property, Name):
		self.Health_Recovery=Health_Property
		self.Property=Property
		self.Type="Food"
		self.Name=Name


class Armor:
	"""docstring for Armor"""
	def __init__(self, Armor, Recoil, DiceAttackEvasive, Durability, Type, Name):
		self.Armor=Armor#How much protect (Int)
		self.Recoil=Recoil#To enemy
		self.DiceAttackEvasive=DiceAttackEvasive
		self.Durability=Durability
		self.Durability_Max=Durability
		self.Type=Type
		self.Name=Name

class RawMaterial:
	"""docstring for RawMaterial"""
	def __init__(self, Name, Description):
		self.Name=Name
		self.Description=Description

class CharacterStatus:
	def __init__(self, Name, Description):
		self.Name=Name
		self.Type="Status"
		self.Description=Description
		
class States:
	"""docstring for States"""
	def AttackValidate(self, Weapon_Equipped):
		Luck=randint(1, 100)
		if Luck < Weapon_Equipped.DiceAttackMin:
			return True
		else:
			return False

	def Loot(self):
		Loot_Item=randint(1, 100)
		if Loot_Item < 50:
			return copy(Hamburguer)
		else:
			return copy(LeatherBreastplate)

	def Eat(self, Character):
		InventoryFood=[]
		for i in range(0, Character.InventoryCapacity):
			if Character.Inventory[i] == None:
				continue
			if Character.Inventory[i].Type == "Food":
				InventoryFood.append(Character.Inventory[i].Name)
		if len(InventoryFood) != 0:
			print("{} HP: {}/{}".format(Character.Name, Character.Health, Character.Health_Max))
			print("")
			for i in range(0, len(InventoryFood)):
				print("{}. {}".format(i+1, InventoryFood[i]))
			print("")
			r=int(input(""))
			print("")
			SelectedFood=InventoryFood[r-1]
			for i in range(0, Character.InventoryCapacity):
				if Character.Inventory[i].Name == SelectedFood:
					if Character.Inventory[i].Property == "Restore":
						if Character.Health < Character.Health_Max:
							print("Your Health has recovered in ", Character.Inventory[i].Health_Recovery, "\n")
							Character.Health+=Character.Inventory[i].Health_Recovery
							Character.Inventory[i]=None
							if Character.Health > Character.Health_Max:
								Character.Health=Character.Health_Max
							if i == Character.InventoryCapacity-1:
								break
							else:
								del(Character.Inventory[i])
								Character.Inventory.append(None)
								break
						else:
							print("You have Health in max\n")
							break
					else:
						if Character.Inventory[i].Property == "Up":
							print("Your Health Max has increased in ", Character.Inventory[i].Health_Recovery, "\n")
							Character.Health_Max+=Character.Inventory[i].Health_Recovery
							Character.Inventory[i]=None
							if i == Character.InventoryCapacity-1:
								break
							else:
								del(Character.Inventory[i])
								Character.Inventory.append(None)
								break
						else:
							print("Your Health Max has decreased in ", Character.Inventory[i].Health_Recovery, "\n")
							Character.Health_Max-=Character.Inventory[i].Health_Recovery
							Character.Inventory[i]=None		
							if i == Character.InventoryCapacity-1:
								break
							else:
								del(Character.Inventory[i])
								Character.Inventory.append(None)
								break
		else:
			print("You don't have food\n")

	def ThrowOut(self, Character):
		InventoryItems=[]
		for i in range(0, Character.InventoryCapacity):
			if Character.Inventory[i] != None:
				InventoryItems.append(Character.Inventory[i].Name)
		if len(InventoryItems) != 0:
			for i in range(0, len(InventoryItems)):
				print("{}. {}".format(i+1, InventoryItems[i]))
			print("")
			r=int(input(""))
			print("")
			SelectedItem=InventoryItems[r-1]
			for i in range(0, Character.InventoryCapacity):
				if Character.Inventory[i].Name == SelectedItem:
					Character.Inventory[i]=None
					print("Object thrown succesfully\n")
					if i == Character.InventoryCapacity-1:
						break
					else:
						del(Character.Inventory[i])
						Character.Inventory.append(None)
						break
		else:
			print("You don't have objects\n")

	def EquipWeapon(self, Character):
		InventoryWeapon=[]
		for i in range(0, Character.InventoryCapacity):
			if Character.Inventory[i] == None:
				continue
			if Character.Inventory[i].Type == "Weapon":
				InventoryWeapon.append(Character.Inventory[i].Name)
		if len(InventoryWeapon) != 0:
			for i in range(0, len(InventoryWeapon)):
				print("{}. {}".format(i+1, InventoryWeapon[i]))
			print("")
			r=int(input(""))
			print("")
			SelectedWeapon=InventoryWeapon[r-1]
			for i in range(0, Character.InventoryCapacity):
				if Character.Inventory[i].Name == SelectedWeapon:
					if Character.Weapon.Name == "Hand":
						Character.Weapon, Character.Inventory[i]=copy(Character.Inventory[i]), None
						print(Character.Weapon.Name)
						print(Character.Weapon.Name, " equip succesfully\n")
						if i == Character.InventoryCapacity-1:
							break
						else:
							del(Character.Inventory[i])
							Character.Inventory.append(None)
							break
					else:
						Character.Weapon, Character.Inventory[i]=Character.Inventory[i], Character.Weapon
						print(Character.Weapon.Name, " equip succesfully\n")
						break
		else:
			print("You don't have more weapons")

	def EquipBreastplate(self, Character):
		InventoryBreastplate=[]
		for i in range(0, Character.InventoryCapacity):
			if Character.Inventory[i] == None:
				continue
			if Character.Inventory[i].Type == "Breastplate":
				InventoryBreastplate.append(Character.Inventory[i].Name)
		if len(InventoryBreastplate) != 0:
			for i in range(0, len(InventoryBreastplate)):
				print("{}. {}".format(i+1, InventoryBreastplate[i]))
			print("")
			r=int(input(""))
			print("")
			SelectedBreastplate=InventoryBreastplate[r-1]
			for i in range(0, Character.InventoryCapacity):
				if Character.Inventory[i].Name == SelectedBreastplate:
					if Character.Breastplate.Name == "NudeBreastplate":
						Character.Breastplate, Character.Inventory[i]=copy(Character.Inventory[i]), None
						print(Character.Breastplate.Name, " equip succesfully\n")
						if i == Character.InventoryCapacity-1:
							break
						else:
							del(Character.Inventory[i])
							Character.Inventory.append(None)
							break
					else:
						Character.Breastplate, Character.Inventory[i]=Character.Inventory[i], Character.Breastplate
						print(Character.Breastplate.Name, " equip succesfully\n")
						break
		else:
			print("You don't have more breastplate")

	def EquipGreaves(self, Character):
		InventoryGreaves=[]
		for i in range(0, Character.InventoryCapacity):
			if Character.Inventory[i] == None:
				continue
			if Character.Inventory[i].Type == "Greaves":
				InventoryGreaves.append(Character.Inventory[i].Name)
		if len(InventoryGreaves) != 0:
			for i in range(0, len(InventoryGreaves)):
				print("{}. {}".format(i+1, InventoryGreaves[i]))
			print("")
			r=int(input(""))
			print("")
			SelectedGreaves=InventoryGreaves[r-1]
			for i in range(0, Character.InventoryCapacity):
				if Character.Inventory[i].Name == SelectedGreaves:
					if Character.Greaves.Name == "NudeGreaves":
						Character.Greaves, Character.Inventory[i]=copy(Character.Inventory[i]), None
						print(Character.Greaves.Name, " equip succesfully\n")
						if i == Character.InventoryCapacity-1:
							break
						else:
							del(Character.Inventory[i])
							Character.Inventory.append(None)
							break
					else:
						Character.Greaves, Character.Inventory[i]=Character.Inventory[i], Character.Greaves
						print(Character.Greaves.Name, " equip succesfully\n")
						break
		else:
			print("You don't have more greaves")

	def FirstTowerFirstFloor(self, Tower, Floor):
		Enemies=DefineEnemies(Tower, Floor)
		FleaMan, Spyder, Hobgoblins, RatMan=Enemies[0], Enemies[1], Enemies[2], Enemies[3]
		Luck=randint(1, 100)
		if Luck < 30:
			Enemy=copy(FleaMan)
		elif Luck < 60:
			Enemy=copy(Spyder)
		elif Luck < 80:
			Enemy=copy(Hobgoblins)
		else:
			Enemy=copy(RatMan)
		return Enemy

	def FirstTowerSecondFloor(self, Tower, Floor):
		Enemies=DefineEnemies(Tower, Floor)
		Gargola, Grifo, Quimera=Enemies[4], Enemies[5], Enemies[6]
		Luck=randint(1, 100)
		if Luck < 40:
			Enemy=copy(Gargola)
		elif Luck < 70:
			Enemy=copy(Grifo)
		else:
			Enemy=copy(Quimera)
		return Enemy

	def FirstTowerThirdFloor(self, Tower, Floor):
		Enemies=DefineEnemies(Tower, Floor)
		Kitsune, Quetzalcoatl, Hipogrifo, Saeton=Enemies[7], Enemies[8], Enemies[9], Enemies[10]
		Luck=randint(1, 100)
		if Luck < 30:
			Enemy=copy(Kitsune)
		elif Luck < 60:
			Enemy=copy(Quetzalcoatl)
		elif Luck < 80:
			Enemy=copy(Hipogrifo)
		else:
			Enemy=copy(Saeton)
		return Enemy

	def FirstTowerFourthFloor(self, Tower, Floor):
		Enemies=DefineEnemies(Tower, Floor)
		Unicorn, Roc, Hydra, Lion=Enemies[11], Enemies[12], Enemies[13], Enemies[14]
		Luck=randint(1, 100)
		if Luck < 30:
			Enemy=copy(Unicorn)
		elif Luck < 60:
			Enemy=copy(Roc)
		elif Luck < 80:
			Enemy=copy(Hydra)
		else:
			Enemy=copy(Lion)
		return Enemy

	def FirstTower(self, Character, Tower, Floor):
		DefineEnemies(Tower, Floor)
		Luck=randint(1, 100)
		if Luck < 50:
			Luck=randint(1, 100)
			if Luck < 50:
				Luck=randint(1, 100)
				if Luck < 50:
					Character.FirstTowerFirstFloor(Tower, Floor)
				else:
					Character.FirstTowerSecondFloor(Tower, Floor)
			else:
				Character.FirstTowerThirdFloor(Tower, Floor)
		else:
			Character.FirstTowerFourthFloor(Tower, Floor)
		return Enemy

	def EnemyAppears(self, Character, Tower, Floor):
		DefineEnemies(Tower, Floor)
		if Tower == "First":
			if Floor == 1:
				Enemy=Character.FirstTowerFirstFloor(Tower, Floor)
			elif Floor == 2:
				Luck=randint(1, 100)
				if Luck < 50:
					Enemy=Character.FirstTowerFirstFloor(Tower, Floor)
				else:
					Enemy=Character.FirstTowerSecondFloor(Tower, Floor)
			elif Floor == 3:
				Luck=randint(1, 100)
				if Luck < 50:
					Luck=randint(1, 100)
					if Luck < 50:
						Enemy=Character.FirstTowerFirstFloor(Tower, Floor)
					else:
						Enemy=Character.FirstTowerSecondFloor(Tower, Floor)
				else:
					Enemy=Character.FirstTowerThirdFloor(Tower, Floor)
			else:
				Enemy=Character.FirstTower(Character)
		elif Tower == "Second":
			pass
		return Enemy


	def EventAppears(self, Character, Tower, Floor, Steps, TowerObj, Events):
		if Tower == "First":
			if Floor == 1:
				Luck=randint(1, 100)
				if Luck > 20+Steps:
					Enemy=Character.EnemyAppears(Character, Tower, Floor)
					os.system("cls")
					print("Have you been stopped by a ", Enemy.Name, "\n")
					Battle(Character, Enemy, Tower, Floor, TowerObj)
				elif Luck < 10+Steps:
					print("You found the Ladder")
					TowerObj.Floor+=1
					print("???: Eyy ", Character.Name)
					print(Character.Name+": ", "Hefesto?")
					print("Hefesto: Take a give, good luck\n")
					input("Press enter to continue.\n")
					os.system("cls")
					print("You know can Forge Armament\n")
					Character.SwordMold+=1
					Character.DaggerMold+=1
					Character.LanceMold+=1
					Character.BowMold+=1
					Character.AxeMold+=1
					Events.ForgeArmament=0
			elif Floor == 2:
				pass
	def MoveForward(self, Events, Character, Tower, Floor, Steps, TowerObj):
		Character.EventAppears(Character, Tower, Floor, Steps, TowerObj, Events)
		TowerObj.Steps+=1

	def ForgeArmament(self, Character):
		pass
class Characters(States):
	"""docstring for Characters"""
	def __init__(self, Health_Max, Health, Weapon, Breastplate, Greaves, Vials, SwordMold, DaggerMold, LanceMold, BowMold, AxeMold, Inventory, Level, Experience, Name):
		self.Health_Max=Health_Max
		self.Health=float(Health)
		self.Weapon=copy(Weapon)
		self.Breastplate=copy(Breastplate)
		self.Greaves=copy(Greaves)
		self.Vials=Vials
		self.SwordMold=SwordMold
		self.DaggerMold=DaggerMold
		self.LanceMold=LanceMold
		self.BowMold=BowMold
		self.AxeMold=AxeMold
		self.InventoryCapacity=5
		if Inventory == None:
			self.Inventory=[None]*self.InventoryCapacity
		else:
			self.Inventory=Inventory
		self.Level=Level
		self.Experience=Experience
		self.Name=Name
		
class CharacterRawMaterialInventory():
	"""docstring for CharacterRawMaterialInventory"""
	def __init__(self):
		pass


class NPC(States):
	"""docstring for NPC"""
	def __init__(self):
		pass

class Enemy(States):
	"""docstring for Enemy"""
	def __init__(self, Health, Attack, Exp, Level, Type, Name):
		self.Health=Health
		self.Health_Max=Health
		self.Attack=Attack
		self.Exp=Exp
		self.Level=Level
		self.Type=Type
		self.Name=Name

class Towers:
	"""docstring for Tower"""
	def __init__(self, Tower, Floor, Steps):
		self.Tower=Tower
		self.Floor=Floor
		self.Steps=Steps

class Events(object):
	"""docstring for Events"""
	def __init__(self, ForgeArmament):
		self.ForgeArmament=ForgeArmament

class Exits():
	def __init__(self, Exit):
		self.Exit=Exit

def SeeInventory(Character):
	InventoryItems=[]
	for i in range(0, Character.InventoryCapacity):
		if Character.Inventory[i] != None:
			InventoryItems.append(Character.Inventory[i].Name)
	print(InventoryItems)

def SeeIndexInventory(Character):
	for i in range(0, Character.InventoryCapacity):
		if Character.Inventory[i] == None:
			return i
	return None

def Battle(Character, Enemy, Tower, Floor, TowerObj):
	while True:
		if Enemy.Health <= 0:
			os.system("cls")
			print("You deafeted the ", Enemy.Name, "\n")
			Loot=LootFightEnemies(Tower, Floor, Enemy)
			if Loot != None:
				if Loot.Type != "Status":
					Index=SeeIndexInventory(Character)
					print("You found", Loot.Name, "\n")
					time.sleep(2)
					if Index == None:
						print("Inventory is full\n")
						r=int(input("Do you want throw out an item?\n1. Yes\n2. No"))
						if r == 1:
							Character.ThrowOut(Character)
					Index=SeeIndexInventory(Character)
					if Index != None:
						Character.Inventory[Index]=copy(Loot)
			break
		elif Character.Health <= 0:
			os.system("cls")
			print("You are dead\n")
			ExitGame.Exit=1
			break
		"""if Character.Weapon.Durability <= 0:
			Character.Weapon=copy(Hand)
		if Character.Breastplate.Durability <= 0:
			Character.Breastplate=copy(NudeBreastplate)
		if Character.Greaves.Durability <= 0:
			Character.Greaves=copy(NudeGreaves)"""
		print("{} HP: {}/{}".format(Enemy.Name, Enemy.Health, Enemy.Health_Max))
		print("")
		print("{} HP: {}/{}".format(Character.Name, Character.Health, Character.Health_Max))
		print("")
		r=int(input("1. Attack\n2. Loot\n3. Change Equip\n4. Eat\n5. Throw out an object\n6. Escape\n7. Wait\n\n"))
		print("")
		if r == 1:
			if Enemy.Type == "Fly":
				if Character.Weapon.Subtype == "Sword" or Character.Weapon.Subtype == "HandToHand" or Character.Weapon.Subtype == "Dagger" or Character.Weapon.Subtype == "Axe":
					print("Your weapon can't reach the enemy\n")
			else:
				if Character.AttackValidate(Character.Weapon):
					print("You hit succesfully\n")
					Character.Weapon.Durability-=1
					Enemy.Health-=(Character.Weapon.Damage)+(0.5*(Character.Level-1))
					Character.Health-=Character.Weapon.Recoil
				else:
					print("Enemy dodges the attack\n")
		elif r == 2:
			Index=SeeIndexInventory(Character)
			if Index == None:
				print("Inventory is full\n")
				continue	
			Character.Inventory[Index]=copy(Character.Loot())
			if Character.Inventory[Index] != None:
				print("Has encontrado, ", Character.Inventory[Index].Name)
				if Character.Inventory[Index].Type == "Food":
					r=int(input("Do you want eat them?\n1. Yes\n2.No\n\n"))
					print("")
					if r == 1:
						if Character.Inventory[Index].Property == "Restore":
							if Character.Health < Character.Health_Max:
								print("Your Health has recovered in ", Character.Inventory[Index].Health_Recovery, "\n")
								Character.Health+=Character.Inventory[Index].Health_Recovery
								Character.Inventory[Index]=None
								if Character.Health > Character.Health_Max:
									Character.Health=Character.Health_Max
							else:
								print("You have Health in max\n")
						else:
							if Character.Inventory[Index].Property == "Up":
								print("Your Health Max has increased in ", Character.Inventory[Index].Health_Recovery, "\n")
								Character.Health_Max+=Character.Inventory[Index].Health_Recovery
								Character.Inventory[Index]=None
				else:
					r=int(input("Do you want equip them?\n1. Yes\n2. No\n\n"))
					print("")
					if r == 1:
						if Character.Inventory[Index].Type == "Weapon":
							if Character.Weapon.Name == "Hand":
								Character.Weapon=Character.Inventory[Index]
							else:
								Character.Weapon, Character.Inventory[Index]=Character.Inventory[Index], Character.Weapon
						elif Character.Inventory[Index].Type == "Breastplate":
							Character.Breastplate, Character.Inventory[Index]=Character.Inventory[Index], Character.Breastplate
						else:
							Character.Greaves, Character.Inventory[Index]=Character.Inventory[Index], Character.Greaves
			else:
				print("You did not find anything\n")
		elif r == 3:
			r=int(input("What do you want change?\n1. Weapon\n2. Breastplate\n3. Greaves\n\n"))
			print("")
			if r == 1:
				Character.EquipWeapon(Character)
			elif r == 2:
				Character.EquipBreastplate(Character)
			else:
				Character.EquipGreaves(Character)
		elif r == 4:
			Character.Eat(Character)
		elif r == 5:
			Character.ThrowOut(Character)
		elif r == 6:
			if Enemy.Type == "Fly":
				Luck=randint(1, 100)
				if Luck < 50:
					print("You failed\n")
				else:
					print("You run out succesfully")
					print("You run out three steps backward\n")
					TowerObj.Steps-=4
					if TowerObj.Steps < 0:
						TowerObj.Steps=-1
					break
			else:
				Luck=randint(1, 100)
				if Luck < 25:
					print("You failed\n")
				else:
					print("You run out succesfully")
					print("You run out three steps backward\n")
					TowerObj.Steps-=4
					if TowerObj.Steps < 0:
						TowerObj.Steps=-1
					break
		else:
			print("You stand still\n")
		if Enemy.Health > 0:
			print(Enemy.Name, "Attacks\n")
			time.sleep(1)
			Armor=Character.Breastplate.DiceAttackEvasive+Character.Greaves.DiceAttackEvasive
			Luck=randint(1, 100)
			if Luck > Armor:
				print("Enemy hits succesfully\n")
				Character.Health-=Enemy.Attack
				ArmorRecoil=Character.Breastplate.Recoil+Character.Greaves.Recoil
				Enemy.Health-=ArmorRecoil
				Character.Breastplate.Durability-=1
				Character.Greaves.Durability-=1
			else:
				print("You dodge the attack\n")


from items import *
from enemies import *
from exitgame import *
from charstatus import *