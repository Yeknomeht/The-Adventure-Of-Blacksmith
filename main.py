from config import *
from items import *
from enemies import *
from exitgame import *
import time
import os

#def __init__(self, Health_Max, Health, Weapon, Breastplate, Greaves, Vials, SwordMold, DaggerMold, LanceMold, BowMold, AxeMold BackpackBurdenCapacity, Inventory, Level, Experience, Name):
#Para hacer guardado y cargado, usar string para hacer split con espacios y usar *Inventory para que se guarde como lista con asignacion multiple

print("#############################################################################")
print("Trapped in towers, the adventure of the Blacksmith trying save his Son")
print("By: Yeknomeht")
print("2019")
print("#############################################################################\n")

while True:
	while True:
		Flag=True
		try:
			r=int(input("1. New game\n2. Load Game\n3. Options\n4. Exit\n\n"))
			print("")
		except:
			print("\nInput Error\n")
			Flag=False
		if Flag:
			break
	if r == 1:
		os.system("cls")
		print("A Blacksmith have a Son.")
		time.sleep(1)
		print("One day, a Monster Kidnapp the Son of the Blacksmith")
		time.sleep(1)
		print("The monsters want the secrets of the Blacksmith")
		time.sleep(1)
		print("The Blacksmith go to rescue his Son")
		time.sleep(1)
		print("His best friend tells to go to a tower")
		time.sleep(1)
		print("The Blacksmith take five Vials, a Backpack and start to rescue his Son")
		time.sleep(1)
		Character=Characters(3, 3, copy(Hand), copy(LeatherBreastplate), copy(LeatherGreaves), 5, 0, 0, 0, 0, 0, None, 1, 0, Name=input("Enter the name of the Blacksmith: "))
		Tower=Towers("First", 1, 0)#Tower, Floor, Steps
		Events=Events(1)#ForgeArmament,
		break
	elif r == 2:
		r=int(input("1. First Slot\n2. Second Slot\n3. Third Slot\n\n"))
		print("")
		if r == 1: #Read Character
			Registry = open("slot1character.txt", "r")
			StringSaveCharacter=Registry.read()
			LenStringSaveCharacter=len(StringSaveCharacter)
			Registry.close()
			#Read Events
			Registry = open("slot1events.txt", "r")
			StringSaveEvents=Registry.read()
			LenStringSaveEvents=len(StringSaveEvents)
			Registry.close()
			#Read Tower
			Registry = open("slot1tower.txt", "r")
			StringSaveTower=Registry.read()
			LenStringSaveTower=len(StringSaveTower)
			Registry.close()
		elif r == 2: #Read Character
			Registry = open("slot2character.txt", "r")
			StringSaveCharacter=Registry.read()
			LenStringSaveCharacter=len(StringSaveCharacter)
			Registry.close()
			#Read Events
			Registry = open("slot2events.txt", "r")
			StringSaveEvents=Registry.read()
			LenStringSaveEvents=len(StringSaveEvents)
			Registry.close()
			#Read Tower
			Registry = open("slot2tower.txt", "r")
			StringSaveTower=Registry.read()
			LenStringSaveTower=len(StringSaveTower)
			Registry.close()
		elif r == 3: #Read Character
			Registry = open("slot3character.txt", "r")
			StringSaveCharacter=Registry.read()
			LenStringSaveCharacter=len(StringSaveCharacter)
			Registry.close()
			#Read Events
			Registry = open("slot3events.txt", "r")
			StringSaveEvents=Registry.read()
			LenStringSaveEvents=len(StringSaveEvents)
			Registry.close()
			#Read Tower
			Registry = open("slot3tower.txt", "r")
			StringSaveTower=Registry.read()
			LenStringSaveTower=len(StringSaveTower)
			Registry.close()
		if LenStringSaveCharacter == 0 or LenStringSaveEvents == 0 or LenStringSaveTower == 0:
			print("Saved game not found\n")
			continue
		#Character
		CharacterList=StringSaveCharacter.split(" ")
		WeaponName, BreastplateName, GreavesName=CharacterList[2], CharacterList[3], CharacterList[4]
		del(CharacterList[4])
		del(CharacterList[3])
		del(CharacterList[2])
		if CharacterList[8] == "None":
			Inventory=None
			del(CharacterList[8])
		else:
			for i in range(0, len(CharacterList)-8):
				Inventory.append(CharacterList[8])
				del(CharacterList[8])
			for i in range(0, len(Inventory)):
				for j in range(0, len(List)):
					if Inventory[i] == List[j].Name:
						Inventory[i]=copy(List[j])
						break
			if len(Inventory) == 4:
				Inventory.append(None)
			elif len(Inventory) == 3:
				Inventory.append(None)
				Inventory.append(None)
			elif len(Inventory) == 2:
				Inventory.append(None)
				Inventory.append(None)
				Inventory.append(None)
			elif len(Inventory) == 1:
				Inventory.append(None)
				Inventory.append(None)
				Inventory.append(None)
				Inventory.append(None)
		for i in range(0, len(List)):
			if WeaponName == List[i].Name:
				Weapon=copy(List[i])
				break
		for i in range(0, len(List)):
			if BreastplateName == List[i].Name:
				Breastplates=copy(List[i])
				break
		for i in range(0, len(List)):
			if GreavesName == List[i].Name:
				Greaves=copy(List[i])
				break
		Name=CharacterList[len(CharacterList)-1]
		del(CharacterList[len(CharacterList)-1])
		CharacterList=map(float, CharacterList)
		CharacterList=list(CharacterList)
		Health_Max, Health, Vials, SwordMold, DaggerMold, LanceMold, BowMold, AxeMold, Level, Experience=CharacterList
		Character=Characters(Health_Max, Health, Weapon, Breastplates, Greaves, Vials, SwordMold, DaggerMold, LanceMold, BowMold, AxeMold, Inventory, Level, Experience, Name)
		#Events
		ForgeArmament=int(StringSaveEvents)
		Events=Events(ForgeArmament)
		#Tower
		TowerData=StringSaveTower.split(" ")
		Tower, Floor, Step=TowerData
		Floor=int(Floor)
		Step=int(Step)
		Tower=Towers(Tower, Floor, Step)
		break

	elif r == 3:
		r=int(input("1. Languague\n2. Music\n\n"))
		if r == 1:
			print("Coming soon")
		elif r == 2:
			r=int(input("1. Turn on the music\n2. Turn of the music\n\n"))
			if r == 1:
				print("Music has turned on\n\n")
				Music=True
			elif r == 2:
				print("Music has turned off\n\n")
				Music=False
	else:
		os.system("cls")
		ExitGame.Exit=1
		break

os.system("cls")

while True:
	print("{} HP: {}/{}".format(Character.Name, Character.Health, Character.Health_Max))
	print("")
	print("Tower: {}".format(Tower.Tower))
	print("Floor: {}".format(Tower.Floor))
	print("Steps: {}".format(Tower.Steps))
	print("")
	if bool(ExitGame.Exit) == True:
		break
	r=int(input("1. Move forward\n2. Change Equip\n3. Eat\n4. Forge Armament\n5. Throw out an object\n6. Save\n7. Exit\n\n"))
	print("")
	if r == 1:
		Character.MoveForward(Events, Character, Tower.Tower, Tower.Floor, Tower.Steps, Tower)
	elif r == 2:
		r=int(input("What do you want change?\n1. Weapon\n2. Breastplate\n3. Greaves\n\n"))
		print("")
		if r == 1:
			Character.EquipWeapon(Character)
		elif r == 2:
			Character.EquipBreastplate(Character)
		else:
			Character.EquipGreaves(Character)
	elif r == 3:
		Character.Eat(Character)
	elif r == 4:
		if bool(Events.ForgeArmament):
			print("You can't forge armament yet\n")
		else:
			Character.ForgeArmament(Character)
	elif r == 5:
		Character.ThrowOut(Character)
	elif r == 6:
		r=int(input("1. First Slot\n2. Second Slot\n3. Third Slot\n\n"))
		print("")
		#Save Character
		CountInventoryNotNone=0
		StringSaveCharacter=str(Character.Health_Max)+" "+str(Character.Health)+" "+Character.Weapon.Name+" "+Character.Breastplate.Name+" "+Character.Greaves.Name+" "+str(Character.Vials)+" "+str(Character.SwordMold)+" "+str(Character.DaggerMold)+" "+str(Character.LanceMold)+" "+str(Character.BowMold)+" "+str(Character.AxeMold)+" "
		for i in range(0, Character.InventoryCapacity):
			if Character.Inventory[i] != None:
				CountInventoryNotNone+=1
				StringSaveCharacter+=Character.Inventory[i].Name+" "
		if CountInventoryNotNone == 0:
			StringSaveCharacter+="None "
		StringSaveCharacter+=str(Character.Level)+" "+str(Character.Experience)+" "+str(Character.Name)
		#Save Events
		StringSaveEvents=str(Events.ForgeArmament)
		#Save Tower
		StringSaveTower=Tower.Tower+" "+str(Tower.Floor)+" "+str(Tower.Steps)
		if r == 1:
			Registry=open("slot1character.txt", "w")
			Registry.write(StringSaveCharacter)
			Registry.close() 
			Registry=open("slot1events.txt", "w")
			Registry.write(StringSaveEvents)
			Registry.close() 
			Registry=open("slot1tower.txt", "w")
			Registry.write(StringSaveTower)
			Registry.close() 
		elif r == 2:
			Registry=open("slot2character.txt", "w")
			Registry.write(StringSaveCharacter)
			Registry.close() 
			Registry=open("slot2events.txt", "w")
			Registry.write(StringSaveEvents)
			Registry.close() 
			Registry=open("slot2tower.txt", "w")
			Registry.write(StringSaveTower)
			Registry.close() 
		elif r == 3:
			Registry=open("slot3character.txt", "w")
			Registry.write(StringSaveCharacter)
			Registry.close() 
			Registry=open("slot3events.txt", "w")
			Registry.write(StringSaveEvents)
			Registry.close() 
			Registry=open("slot3tower.txt", "w")
			Registry.write(StringSaveTower)
			Registry.close() 
			

	elif r == 7:
		ExitGame.Exit=1
print("See you next time")