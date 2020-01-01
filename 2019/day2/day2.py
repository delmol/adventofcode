

def program():
	intProgram = [
			1,12,2,3,1,1,2,3,1,3,
			4,3,1,5,0,3,2,1,10,19,
			1,6,19,23,1,10,23,27,2,27,
			13,31,1,31,6,35,2,6,35,39,
			1,39,5,43,1,6,43,47,2,6,
			47,51,1,51,5,55,2,55,9,59,
			1,6,59,63,1,9,63,67,1,67,
			10,71,2,9,71,75,1,6,75,79,
			1,5,79,83,2,83,10,87,1,87,
			5,91,1,91,9,95,1,6,95,99,
			2,99,10,103,1,103,5,107,2,107,
			6,111,1,111,5,115,1,9,115,119,
			2,119,10,123,1,6,123,127,2,13,
			127,131,1,131,6,135,1,135,10,139,
			1,13,139,143,1,143,13,147,1,5,
			147,151,1,151,2,155,1,155,5,0,
			99,2,0,14,0
			]
	
	return intProgram

def runIntcode(intProgram):
	
	memory = intProgram
	
	if memory[0] not in [1, 2, 99]:
		print("Program invalid")
		
		return
	
	position = 0
	
	while position <= len(memory) - 1:
		intCode = memory[position]
		
		if intCode == 1:
			memory = add(position, memory)
			position += 4
		
		if intCode == 2:
			memory = multiply(position, memory)
			position += 4
		
		if intCode == 99:
			print("Execution complete")
			output = memory[0]
			return output
		
	
	return

def add(position, memory):
	x = memory[position + 1]
	y = memory[position + 2]
	z = memory[position + 3]
	output = memory[x] + memory[y]
	memory[z] = output
	
	return memory

def multiply(position, memory):
	x = memory[position + 1]
	y = memory[position + 2]
	z = memory[position + 3]
	output = memory[x] * memory[y]
	memory[z] = output
	
	return memory

def runProgram(noun, verb):
	xProgram = program()
	xProgram[1] = noun
	xProgram[2] = verb
	x = runIntcode(xProgram)
	return x


def bruteForce():
	noun = 0
	verb = 0
	output = 0
	
	while noun <= 99:
		while verb <= 99:
			output = runProgram(noun, verb)
			
			if output == 19690720:
				print("Solution found!")
				print("Noun: " + str(noun))
				print("Verb: " + str(verb))
				return
			
			verb += 1
			
		noun += 1
		verb = 0
	
	return

				
bruteForce()
