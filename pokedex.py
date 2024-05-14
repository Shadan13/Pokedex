from random import randint # Random library to generate random numbers

pokedex = []
with open("Pokemon.csv", "r",  encoding = "UTF-8") as file: # Read Pokemon data from CSV file and writes it to list pokedex
	for line in file:
		pokemonData = line.strip().split(",")
		pokedex.append(pokemonData)

pokedexHeader = {
	"No"         : 0,
	"Name"       : 1,
	"Type 1"     : 2,
	"Type 2"     : 3,
	"Total"      : 4,
	"HP"         : 5,
	"Attack"     : 6,
	"Defense"    : 7,
	"Sp. Atk"    : 8,
	"Sp. Def"    : 9,
	"Speed"      : 10,
	"Generation" : 11,
	"Legendary"  : 12	
} # List of header names for each column in the CSV file, to make later code more readable


def mainMenu(): # Lists options for the main menu
	"""
	Lists options for the main menu of the Pokemon Super Search Engine.

	Displays a menu with various options for interacting with the Pokemon database.

	Options:
	1. Display a selected number of Pokemon with their types and statistics
	2. Display the first Pokemon of a Type of your choice
	3. Display all the Pokemon with a Total Base stat of your choice
	4. Display all Pokemon with a minimum set of stats
	5. Display all legendary Pokemon of specific Type1 and Type2
	6. Create a team of 10 random Pokemon
	0. Quit

	Returns:
	None: This function does not return any value. It prints the menu directly.
	"""
	print("Pokemon Super Search Engine")
	print("1. Display a selected number of Pokemon with their types and statistics")
	print("2. Display the first Pokemon of a Type of your choice")
	print("3. Display all the Pokemon with a Total Base stat of your choice")
	print("4. Display all Pokemon with a minimum set of stats")
	print("5. Display all legendary Pokemon of specific Type1 and Type2")
	print("6. Create a team of 10 random Pokemon")
	print("0. Quit")


def formatAndPrint(pokemonPrint): # Function to format and print list pokemonPrint in "table" form
	"""
	Formats and prints the provided list of Pokemon data in a tabular format.

	Args: 
		pokemonPrint (list): A list containing lists of Pokemon data, where each inner list represents a Pokemon.

	Returns: 
		None: This function does not return any value. It prints the formatted table directly.

	Example: 
		Suppose we have the following list of Pokemon data:

		header = "No,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary"
		pokemonPrint = [
			[1, "Bulbasaur", "Grass", "Poison", 318, 45, 49, 49, 65, 65, 45, 1, False],
			[2, "Ivysaur", "Grass", "Poison", 405, 60, 62, 63, 80, 80, 60, 1, False],
			[3, "Venusaur", "Grass", "Poison", 525, 80, 82, 83, 100, 100, 80, 1, False]
		]

		Calling formatAndPrint(pokemonPrint) will print the data in a formatted table like this:

		No  Name       Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary 
		1   Bulbasaur  Grass   Poison  318    45  49      49       65       65       45     1           False     
		2   Ivysaur    Grass   Poison  405    60  62      63       80       80       60     1           False     
		3   Venusaur   Grass   Poison  525    80  82      83       100      100      80     1           False     

		Each column is adjusted to fit the maximum length of its elements.
	"""
	maxLengths = [max(len(str(pokemonData[i])) + 2 for pokemonData in pokedex[0:1]) for i in range(len(pokedex[0]))]
	# Calculates maximum length of element in one column of the table for each column to be printed
	# By default, the first row is the header, so the length of the header is added to the maxLengths list
	for number in pokemonPrint:
		maxLengthsNew = [len(number[i]) + 2 for i in range(len(pokedex[0]))]
		# Assigns new length of element in one column of the table for each column to be printed, and adds 2 whitespaces for padding
		# This is based on the actual length of the element in the list (i.e. the item to be printed)
		for element in range(len(maxLengthsNew)):
			if maxLengthsNew[element] > maxLengths[element]:
				# If the new length of element in one column of the table is greater than the maximum length of that column,
				maxLengths[element] = maxLengthsNew[element]
				# Reassigns the maximum length of that column to the new length of element in one column of the table
	header = pokedex[0]
	headerFormat = ''.join([f'{{{i}:<{maxLengths[i]}}}' for i in range(len(header))])
	# Creates a format string for the header of the table, using the maxLengths list to determine the maximum length of each column
	print("\n" + headerFormat.format(*header)) # Prints header using the format
	for number in pokemonPrint:
		print(headerFormat.format(*number)) # Prints remaining rows using the same table format
	input("\nPress enter to continue...")
	print("\n")

def selectedNumber(numberShown): # Shows a selected number (input by user) of Pokemon with their types and statistics
	"""
	Shows a selected number of Pokemon with their types and statistics.

	Retrieves Pokemon data from the Pokedex and displays information for the specified number of Pokemon.

	Args:
		numberShown (int): The number of Pokemon to display.

	Returns:
		None: This function does not return any value. It prints the Pokemon data directly.

	Data validation:
		- The function checks if the specified number of Pokemon is within the range of available Pokemon in the Pokedex.
		- The function checks if the specified number is not zero. If it is, it prints an error message and prompts the user to enter a valid number.

	Example:
		Suppose we have the following Pokedex data:

		pokedex = [
			["No", "Name", "Type 1", "Type 2", "Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Generation", "Legendary"],
			[1, "Bulbasaur", "Grass", "Poison", 318, 45, 49, 49, 65, 65, 45, 1, False],
			[2, "Ivysaur", "Grass", "Poison", 405, 60, 62, 63, 80, 80, 60, 1, False],
			[3, "Venusaur", "Grass", "Poison", 525, 80, 82, 83, 100, 100, 80, 1, False]
		]

		Calling selectedNumber(2) will print the data of the first two Pokemon:

		No  Name       Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary 
		1   Bulbasaur  Grass   Poison  318    45  49      49       65       65       45     1           False     
		2   Ivysaur    Grass   Poison  405    60  62      63       80       80       60     1           False

	"""
	pokemonPrint = []
	if numberShown <= len(pokedex) - 1: # Validates the number input by user is within the range of available Pokemon in the Pokedex
		for num in range(numberShown):
			pokemonPrint.append(pokedex[num + 1])
		if pokemonPrint:
			formatAndPrint(pokemonPrint) # Calls formatAndPrint function to format and print the Pokemon data in a table
		else: # This block runs when user inputs a number that is 0 or lower
			print("Input a number greater than 0.\n")
			input("Press enter to continue...")
			print("\n")
	else: # This block runs when user inputs a number that is greater than the number of Pokemon in the Pokedex
		print("Number of Pokemon to be displayed exceeds the number of Pokemon in the Pokedex. Try again.\n")
		input("Press enter to continue...")
		print("\n")

def selectedType(pokemonType): # Shows the first Pokemon of the type entered by the user
	"""
	Shows the first Pokemon of the specified type entered by the user.

	Retrieves the first Pokemon from the Pokedex that matches the given type.

	Args:
		pokemonType (str): The type of Pokemon to display.

	Returns:
		None: This function does not return any value. It prints the Pokemon data directly.

	Notes:
		- The function searches for the specified type in both Type 1 and Type 2 fields of the Pokemon data.
		- The function validates that a pokemon of specified type exists. If not, it prints an error message.

	Example:
		Suppose we have the following Pokedex data:

		pokedex = [
			["No", "Name", "Type 1", "Type 2", "Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Generation", "Legendary"],
			[1, "Bulbasaur", "Grass", "Poison", 318, 45, 49, 49, 65, 65, 45, 1, False],
			[2, "Ivysaur", "Grass", "Poison", 405, 60, 62, 63, 80, 80, 60, 1, False],
			[3, "Venusaur", "Grass", "Poison", 525, 80, 82, 83, 100, 100, 80, 1, False]
		]

		Calling selectedType("Grass") will print the data of the first Grass type Pokemon:

		No  Name       Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary 
		1   Bulbasaur  Grass   Poison  318    45  49      49       65       65       45     1           False

	"""
	pokemonPrint = []
	for pokemon in pokedex:
		if pokemonType in (pokemon[pokedexHeader['Type 1']], pokemon[pokedexHeader['Type 2']]):
			# Validates that a pokemon of specified type exists, and then searches for that type
			pokemonPrint.append(pokemon)
			break # To ensure only the first is printed, breaks the loop once the first pokemon is found
	if pokemonPrint:
		formatAndPrint(pokemonPrint)
	else: # This block will run when the type entered does not exist in the Pokedex
		print("No pokemon of this type.\n")
		input("Press enter to continue...")
		print("\n")

def selectedTotal(baseTotal): #	Shows all Pokemon with the specified Total Base stat.
	"""
	Retrieves Pokemon from the Pokedex whose Total Base stat matches the given value.

	Args:
		baseTotal (str): The Total Base stat value to match.

	Returns:
		None: This function does not return any value. It prints the Pokemon data directly.

	Example:
		Suppose we have the following Pokedex data:

		pokemonData = [
			["No", "Name", "Type 1", "Type 2", "Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Generation", "Legendary"],
			[1, "Bulbasaur", "Grass", "Poison", 318, 45, 49, 49, 65, 65, 45, 1, False],
			[2, "Ivysaur", "Grass", "Poison", 405, 60, 62, 63, 80, 80, 60, 1, False],
			[3, "Venusaur", "Grass", "Poison", 525, 80, 82, 83, 100, 100, 80, 1, False]
		]

		Calling selectedTotal(405) will print the data of Pokemon with a Total Base stat of 405:

		No  Name       Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary 
		2   Ivysaur    Grass   Poison  405    60  62      63       80       80       60     1           False

	"""
	pokemonPrint = []
	for pokemon in pokedex:
		if pokemon[pokedexHeader["Total"]] == baseTotal: # Searches for pokemon with the exact Total stat as the user input
			pokemonPrint.append(pokemon)
	if pokemonPrint:
		formatAndPrint(pokemonPrint)
	else: # This block will run when no pokemon are found that have the exact Total stat as the user input
		print("No pokemon with this Total Base stat.\n")
		input("Press enter to continue...")
		print("\n")

def selectedStats(minSpAtk, minSpDef, minSpd): # Shows pokemon with minimum statistics as per user request
	"""
	Retrieves Pokemon from the Pokedex whose Special Attack (Sp. Atk), Special Defense (Sp. Def), and Speed stats
	are equal to or greater than the specified minimum values.

	Args:
		minSpAtk (int): The minimum Special Attack stat.
		minSpDef (int): The minimum Special Defense stat.
		minSpd (int): The minimum Speed stat.

	Returns:
		None: This function does not return any value. It prints the Pokemon data directly.

	Example:
		Suppose we have the following Pokedex data:

		pokemonData = [
			["No", "Name", "Type 1", "Type 2", "Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Generation", "Legendary"],
			[1, "Bulbasaur", "Grass", "Poison", 318, 45, 49, 49, 65, 65, 45, 1, False],
			[2, "Ivysaur", "Grass", "Poison", 405, 60, 62, 63, 80, 80, 60, 1, False],
			[3, "Venusaur", "Grass", "Poison", 525, 80, 82, 83, 100, 100, 80, 1, False]
		]

		Calling selectedStats(70, 70, 70) will print the data of Pokemon with Sp. Atk, Sp. Def, and Speed stats
		equal to or greater than 70:

		No  Name       Type 1  Type 2  Total  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary 
		3   Venusaur   Grass   Poison  525    80  82      83       100      100      80     1           False

	"""
	pokemonPrint = []
	for pokemon in pokedex[1:]:
		sp_atk = int(pokemon[pokedexHeader["Sp. Atk"]]) # Assigns the Sp. Atk stat of the pokemon to a variable
		sp_def = int(pokemon[pokedexHeader["Sp. Def"]]) # Assigns the Sp. Def stat of the pokemon to a variable
		speed = int(pokemon[pokedexHeader["Speed"]]) # Assigns the Speed stat of the pokemon to a variable
		if sp_atk >= minSpAtk and sp_def >= minSpDef and speed >= minSpd:
			# Validates that the pokemon has the minimum stats
			pokemonPrint.append(pokemon)
	if pokemonPrint:
		formatAndPrint(pokemonPrint)
	else: # This block will run when no pokemon are found that have the minimum stats
		print("No pokemon has such powerful stats.\n")
		input("Press enter to continue...")
		print("\n")

def typeLegendary(type1, type2): # Shows legendary pokemon with types that match the user request
	"""
	Shows legendary Pokemon with types that match the user request.

	Retrieves legendary Pokemon from the Pokedex whose types match the specified Type 1 and Type 2.

	Args:
		type1 (str): The primary type of the Pokemon.
		type2 (str): The secondary type of the Pokemon.

	Returns:
		None: This function does not return any value. It prints the Pokemon data directly.

	Example:
		Suppose we have the following Pokedex data:

		pokemonData = [
			["No", "Name", "Type 1", "Type 2", "Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "Generation", "Legendary"],
			[157, "Articuno", "Ice", "Flying", 580, 90, 85, 100, 95, 125, 85, 1, True],
			[158, "Zapdos", "Electric", "Flying", 580, 90, 90, 85, 125, 90, 100, 1, True],
			[159, "Moltres", "Fire", "Flying", 580, 90, 100, 90, 125, 85, 90, 1, True]
		]

		Calling typeLegendary("Electric", "Flying") will print the data of legendary Pokemon with types Electric and Flying:

		No   Name    Type 1    Type 2  Total  HP  Attack  Defense  Sp. Atk  Sp. Def  Speed  Generation  Legendary
		158  Zapdos  Electric  Flying  580    90  90      85       125      90       100    1           True     

	"""
	pokemonPrint = []
	for pokemon in pokedex[1:]:
		legendary = pokemon[pokedexHeader["Legendary"]] == "TRUE"
		# Assigns a boolean value to the variable legendary
		# If pokemon is legendary, it is True, otherwise it is False
		type_1 = pokemon[pokedexHeader["Type 1"]] # Assigns the Type 1 of the pokemon to a variable
		type_2 = pokemon[pokedexHeader["Type 2"]] # Assigns the Type 2 of the pokemon to a variable
		if legendary and ((type_1 == type1 and type_2 == type2) or (type_2 == type1 and type_1 == type2)):
			# Validates that the pokemon is legendary and has the types that match the user request
			pokemonPrint.append(pokemon)
	if pokemonPrint:
		formatAndPrint(pokemonPrint)
	else: # This block will run when no pokemon are found that match the user request
		print("No such legendary Pokemon.\n")
		input("Press enter to continue...")
		print("\n")

def surpriseMe(): # Generates a team of 10 random Pokemon
	"""
	Generates a team of 10 random Pokemon.

	Randomly selects 10 Pokemon from the Pokedex to form a team.

	Returns:
		None: This function does not return any value. It prints the team of Pokemon directly.

	Example:
		Calling surpriseMe() will print a team of 10 randomly selected Pokemon:

		Your team is...
		(Formatted table of 10 pokemon will be printed here)

	"""
	pokemonPrint = []
	for number in [randint(1, len(pokedex) - 1) for x in range(10)]:
		# Selects 10 random pokemon from the pokedex
		pokemonPrint.append(pokedex[number])
	print("\nYour team is...")
	formatAndPrint(pokemonPrint)


while True: # Infinite loop till user quits
	while True: # Prints main menu
		mainMenu()
		try:
			choice = int(input("\nEnter Option: "))
			if choice in [0, 1, 2, 3, 4, 5, 6]: break # Checks if input is valid
			print("Not implemented yet? Please choose a valid option.\n")
			input("Press enter to continue...")
			print("\n")
		except ValueError: # This block will run when user inputs a non-integer value
			print("Not implemented yet? Please choose a valid option.\n")
			input("Press enter to continue...")
			print("\n")

	if choice == 0:
		print("Thank you for using the Pokemon Super Search Engine.")
		break # Quit

	elif choice == 1: 
		try:
			numberShown = int(input("\nEnter number of Pokemon to be displayed: ")) 
			selectedNumber(numberShown) # Displays selected number of Pokemon
		except ValueError: # Throws error if user inputs a non-integer value
			print("Invalid input. Please enter a valid number.\n")

	elif choice == 2: 
		pokemonType = input("\nEnter Type: ").title().strip()
		# String formatting using .title() and .strip() to match format in CSV file
		selectedType(pokemonType) # Displays first Pokemon of a Type

	elif choice == 3: 
		baseTotal = input("\nEnter Total Base stat: ")
		selectedTotal(baseTotal) # Displays Pokemon with Total Base stat of choice

	elif choice == 4: 
		try:
			minSpAtk = int(input("\nEnter min special attack stat: "))
			minSpDef = int(input("Enter min special defense stat: "))
			minSpd = int(input("Enter min speed stat: "))
			selectedStats(minSpAtk, minSpDef, minSpd)  # Displays Pokemon with minimum set of stats
		except ValueError:
			print("Invalid input. Please enter a valid number.\n")

	elif choice == 5:
		type1 = input("\nEnter Type1: ").title().strip()
		type2 = input("Enter Type2: ").title().strip()
		typeLegendary(type1, type2) # Displays legendary pokemon with types that match the user input

	elif choice == 6:
		surpriseMe() # Displays a team of 10 random Pokemon