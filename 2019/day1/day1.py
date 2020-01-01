import math

def parseFile():
	f = open("input.txt", "r")
	inp = f.readlines()
	
	modMass = []
	
	for line in inp:
		x = int(line)
		modMass.append(x)
		
	return modMass
	
def calcFuel(mass):
	fuel = mass / 3
	fuel = math.floor(fuel)
	fuel = int(fuel)
	fuel = fuel - 2
	
	return fuel
	
	
def totalModFuel(mass):
	fuel = calcFuel(mass)
	totalModFuel = fuel
	
	while fuel > 0:
		fuel = calcFuel(fuel)
		if fuel > 0:
			totalModFuel += fuel
	
	return totalModFuel
	

def totalFuel(modMass):
	fuel = 0
	
	for mod in modMass:
		modFuel = totalModFuel(mod)
		fuel += modFuel
	
	return fuel

modMass = parseFile()
fuel = totalFuel(modMass)
print(fuel)

