from config import *
from items import *
from charstatus import *
from copy import copy
from random import randint
#Enemies
def DefineEnemies(Tower, Floor):
	if Tower == 'First':
		if Floor == 1:		#Level 1
			FleaMan=Enemy(1, 1, 1, 1, "Ground", "FleaMan") #Manticore
			Spyder=Enemy(1.5, 0.5, 1, 1, "Ground", "Spyder") #Manticore
			Hobgoblins=Enemy(2, 1, 1, 1, "Ground", "Hobgoblins") #Duendes Manticore
			RatMan=Enemy(3, 0.5, 2, 1, "Ground", "Ratman") #Manticore
			return [FleaMan, Spyder, Hobgoblins, RatMan]
		elif Floor == 2:	#Level 2
			FleaMan=Enemy(2, 2, 2, 1, "Ground", "FleaMan") #Manticore
			Spyder=Enemy(3, 1, 2, 1, "Ground", "Spyder") #Manticore
			Hobgoblins=Enemy(4, 2, 2, 1, "Ground", "Hobgoblins") #Duendes Manticore
			RatMan=Enemy(6, 1, 4, 1, "Ground", "Ratman") #Manticore
			Gargola=Enemy(4, 1, 3, 2, "Fly", "Gargola") #Manticore	
			Grifo=Enemy(5, 1.5, 5, 2, "Fly", "Grifo") #Manticore
			Quimera=Enemy(6, 1, 4, 2, "Ground", "Quimera") #Manticore
			return [FleaMan, Spyder, Hobgoblins, RatMan, Gargola, Grifo, Quimera]
		elif Floor == 3:	#Level 3
			FleaMan=Enemy(3, 6, 5, 1, "Ground", "FleaMan") #Manticore
			Spyder=Enemy(4, 2, 3, 1, "Ground", "Spyder") #Manticore
			Hobgoblins=Enemy(5, 2, 3, 1, "Ground", "Hobgoblins") #Duendes Manticore
			RatMan=Enemy(6, 1.5, 5, 1, "Ground", "Ratman") #Manticore
			Gargola=Enemy(4, 1.5, 4, 2, "Fly", "Gargola") #Manticore	
			Grifo=Enemy(5, 1.5, 5, 2, "Fly", "Grifo") #Manticore
			Quimera=Enemy(6, 2, 5, 2, "Ground", "Quimera") #Manticore
			Kitsune=Enemy(7, 2, 7, 3, "Ground", "Kitsune") #Manticore
			Quetzalcoatl=Enemy(7, 1.5, 8, 3, "Fly", "Quetzalcoatl") #Serpiente Alada Manticore
			Hipogrifo=Enemy(10, 2.5, 10, 3, "Fly", "Hipogrifo") #Grifo y Caballo Manticore
			Saeton=Enemy(15, 4, 15, 3, "Ground", "Saeton") #Serpiente muy larga Manticore
			return [FleaMan, Spyder, Hobgoblins, RatMan, Gargola, Grifo, Quimera, Kitsune, Quetzalcoatl, Hipogrifo, Saeton]
		else:
			FleaMan=Enemy(5, 12, 1, 1, "Ground", "FleaMan") #Manticore
			Spyder=Enemy(5, 3, 5, 1, "Ground", "Spyder") #Manticore
			Hobgoblins=Enemy(7, 5, 3, 1, "Ground", "Hobgoblins") #Duendes Manticore
			RatMan=Enemy(8, 2, 7, 1, "Ground", "Ratman") #Manticore
			Gargola=Enemy(6, 2, 5, 2, "Fly", "Gargola") #Manticore	
			Grifo=Enemy(7, 2, 7, 2, "Fly", "Grifo") #Manticore
			Quimera=Enemy(8, 2, 10, 2, "Ground", "Quimera") #Manticore
			Kitsune=Enemy(10, 3, 10, 3, "Ground", "Kitsune") #Manticore
			Quetzalcoatl=Enemy(10, 2, 10, 3, "Fly", "Quetzalcoatl") #Serpiente Alada Manticore
			Hipogrifo=Enemy(15, 2.5, 15, 3, "Fly", "Hipogrifo") #Grifo y Caballo Manticore
			Saeton=Enemy(20, 4, 15, 3, "Ground", "Saeton") #Serpiente muy larga Manticore
			Unicorn=Enemy(20, 4.5, 22, 4, "Ground", "Unicorn") #Manticore
			Roc=Enemy(25, 5, 27, 4, "Fly", "Roc") #Ave gigante Manticore
			Hydra=Enemy(30, 5.5, 35, 4, "Ground", "Hydra") #Manticore
			Lion=Enemy(40, 8, 50, 4, "Ground", "Lion") #Manticore
			return [FleaMan, Spyder, Hobgoblins, RatMan, Gargola, Grifo, Quimera, Kitsune, Quetzalcoatl, Hipogrifo, Saeton, Unicorn, Roc, Hydra, Lion]
	elif Tower == "Second":
		pass
"""#Kraken
Shark #Kraken
Kelpie #Kraken
Cecaelia #Mitad mujer mitad tentaculos Kraken
Afang #Kraken
Escila #Monstruo marino, parte superior mujer mitad inferior serpiente o dragon Kraken
Crab #Cangrejo Kraken
YamatanoOrochi #Serpiente gigante con 8 cabezas y lol #Kraken
Leviatan #Gran Serpiente marina Kraken
Piranha #Pirana Kraken
Jellyfish #Jellyfish Kraken
HungarianColacorn #Dragon Kraken
Gargoulle #Dragon Kraken
Triton #Kraken
Kappa #Kraken
Asrai #Hada de agua Kraken
#Frankenstein
Zombie #Frankenstein
Mummy #Momia Frankenstein
Centaurus #Frankenstein
Cerbero #Perro 3 cabezas Frankenstein
Giant #Frankenstein
Slime #Frankenstein
Minotaur #Frankenstein
Warg #Frankenstein
Esfinge #Frankenstein
Sleipnir #Frankenstein
#Dracula
Medusa #Dracula
Vampire #Dracula
Werewolf #Dracula
Ghost #Dracula
TinyDemon #Dracula
Succubus #Dracula
Valkyrie #Dracula
Ghouls #Dracula
Hellhound #Perro Dracula
Gnoll #Criatura bipeda Dracula
Estringe #seres voladores que succionan sangre Dracula
#Yeti
Ent #Yeti
IceGiant #Yeti
Dryad #Duende de Arboles Forma Femenina Yeti
Golem #Yeti
Troll #Yeti
Ogres=Enemy() #Yeti
Orcs=Enemy() #Yeti
Goblins=Enemy() #Yeti
Glaistings #Hada Yeti
Fairy #Yeti
Silfos #Sabiduria Yeti 
#Lucifer
Ninfa #Lucifer
Silfide #Junta ninfa dryad Lucifer
Demon #Lucifer
Witch #Lucifer
AngelOfDeath #Lucifer
Basilisk#Lucifer
Necromancer #Lucifer
Skeleton #Lucifer
LizardsMen #Lucifer
Wyerns #Dragones Lucifer
Banshee #Hadas oscuras Lucifer
Salamander #Lucifer
Imp #Lucifer
#Boss
Manticore=Enemy(100, 8, 100, 5, "Ground")
Kraken
Frankenstein
Dracula
Yeti
Lucifer"""

def LootFightEnemies(Tower, Floor, Enemy):
	if Tower == 'First':
		if Floor == 1:		#Level 1	
			if Enemy.Name == "FleaMan":
				Luck=randint(1, 10)
				if Luck < 4:
					return(copy(ChamomileSubstance))
				elif Luck < 6:
					return(copy(FleaManDagger))
				else:
					return None
			elif Enemy.Name == "Spyder":
				Luck=randint(1, 10)
				if Luck < 3:
					return(copy(Poison))
				else:
					return None
			elif Enemy.Name == "Hobgoblins":
				Luck=randint(1, 10)
				if Luck < 5:
					return(copy(ChamomileSubstance))
				else:
					return None
			elif Enemy.Name == "Ratman":
				Luck=randint(1, 10)
				if Luck < 5:
					return(copy(ChamomileSubstance))
				elif Luck < 7:
					return(copy(RatMeat))
				else:
					return None
		elif Floor == 2:	#Level 2
			pass
		elif Floor == 3:	#Level 3
			pass
		else:               #Level 4
			pass
	elif Tower == "Second":
		pass