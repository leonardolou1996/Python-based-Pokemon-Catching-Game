import random

#Function Definition with Default Parameters and Function Call
def route():
   return input('(G)o capture a Pokémon!\n(S)how me the Pokémon I have right now\n(D)isplay the number of balls I have right now\n(B)uy more balls\n(E)xit\n')


def main():

   #lists
   pokemonList = []
   valueList = []

   #print statements
   print("Welcome to the Pokémon world!")
   userName = input("What's your name? ")
   print(userName + ", You are a Pokémon trainer now!")
   print("Congratulations! " + userName + ", You have 20 balls!")
   print()
   print(userName + ", what do you want to do now?")

   #A list that contains lists
   aList = [["Bulbasaur",10],["Caterpie",3],["Charmander",10],["Ditto",25],["Eevee",25],["Mew",100],["Nidoran",3],["Paras",3],["Pidgey",3],["Pikachu",10],["Rattata",3],["Sandshrew",3],["Snorlax",25],["Squirtle",10],["Zubat",3]]
   my_Pokemon_List = []

   #assignment statement
   ballNum = 20
   usedBall = 0
   flag = True

   #while loop
   while flag:
       # Function Definition with Default Parameters and Function Call
       option = route().strip().lower()

       #tuple
       valid_tuple = ("g", "s", "d", "b", "e")

       #if statement
       if option in valid_tuple[0]:
           flag1 = True

           #while loop
           while flag1:
               print()
               print("Go catch some Pokémon!")

               #random number generator
               #Function Definition with Parameters and Function Call
               pokemon = random.choice(aList)
               value = pokemon[1]
               pokemon = pokemon[0]
               print("There is a wild " + pokemon + "!")
               flag2 = True

               #while loop
               while flag2:
                   option1 = input("1.Throw a ball!(T/t)\n2.Not Interested(I/i)\n")

                   #list
                   valid_option1_list = ["T", "t", "I", "i"]

                   #if statement
                   if option1 not in valid_option1_list:
                       print("That is not a valid input")
                   if option1 == "I" or option1 == "i":
                       flag1 = False
                       break
                   if option1 == "T" or option1 == "t":
                       if ballNum <= 0:
                           print("no balls left")
                           flag1 = False
                           break

                       #Using +=, -+
                       ballNum -= 1
                       usedBall += 1
                       probability = random.randint(1,100)
                       success = False

                       #nested if statement
                       if pokemon == "Bulbasaur" or pokemon == "Charmander" or pokemon == "Eevee" or pokemon == "Pikachu" or pokemon == "Squirtle":
                           if probability <=30:
                               success = True
                               print("You caught it!")
                               valueList.append(value)
                               #Using build-in List (or other data structure) functionality
                               my_Pokemon_List.append(pokemon)

                               #my_Pokemon_List = (my_Pokemon_List)
                               flag3 = True

                               #Nested Loops
                               while flag3:
                                   option3 = input("Move on to the next Pokemon challenge(O/o)\nView the description(V/v)\n")
                                   selection2 = option3.upper()
                                   valid_option3_list = ["O", "o", "V", "v"]
                                   if option3 not in valid_option3_list:
                                       print("That is not a valid input")
                                   if selection2 == "O":
                                       flag2 = False
                                       flag1 = True
                                       break
                                   if selection2 == "V":
                                       result = viewTheDescription(pokemon)
                                       print(result)
                                       print()
                                       flag4 = True
                                       while flag4:
                                           option4 = input("Move on to the next Pokémon challenge(O/o)\nI'm good, take me back to the menu.(G/g)\n")
                                           selection3 = option4.upper()
                                           valid_option4_list = ["O", "o", "G", "g"]
                                           if option4 not in valid_option4_list:
                                               print("That is not a valid input")
                                           if selection3 == "O":
                                               flag3 = False
                                               flag2 = False
                                               flag1 = True
                                               break
                                           if selection3 == "G":
                                               flag3 = False
                                               flag2 = False
                                               flag1 = False
                                               break

                       # nested if statement
                       if pokemon == "Caterpie" or pokemon == "Nidoran" or pokemon == "Paras" or pokemon == "Pidgey" or pokemon == "Rattata" or pokemon == "Sansdshrew" or pokemon == "Zubat":
                           if probability > 30 and probability <=80:
                               success = True
                               print("You caught it!")
                               valueList.append(value)
                               my_Pokemon_List.append(pokemon)
                               #my_Pokemon_List = sorted(my_Pokemon_List)
                               flag3 = True
                               while flag3:
                                   option3 = input("Move on to the next Pokemon challenge(O/o)\nView the description(V/v)\n")
                                   selection2 = option3.upper()
                                   valid_option3_list = ["O", "o", "V", "v"]
                                   if option3 not in valid_option3_list:
                                       print("That is not a valid input")
                                   if selection2 == "O":
                                       flag2 = False
                                       flag1 = True
                                       break
                                   if selection2 == "V":
                                       result = viewTheDescription(pokemon)
                                       print(result)
                                       print()
                                       flag4 = True
                                       while flag4:
                                           option4 = input("Move on to the next Pokémon challenge(O/o)\nI'm good, take me back to the menu.(G/g)\n")
                                           selection3 = option4.upper()
                                           valid_option4_list = ["O", "o", "G", "g"]
                                           if option4 not in valid_option4_list:
                                               print("That is not a valid input")
                                           if selection3 == "O":
                                               flag3 = False
                                               flag2 = False
                                               flag1 = True
                                               break
                                           if selection3 == "G":
                                               flag3 = False
                                               flag2 = False
                                               flag1 = False
                                               break

                       # nested if statement
                       if pokemon == "Ditto" or pokemon == "Snorlax":
                           if probability > 80 and probability <= 95:
                               success = True
                               print("You caught it!")
                               valueList.append(value)
                               my_Pokemon_List.append(pokemon)
                               #my_Pokemon_List = sorted(my_Pokemon_List)
                               flag3 = True
                               while flag3:
                                   option3 = input("Move on to the next Pokemon challenge(O/o)\nView the description(V/v)\n")
                                   selection2 = option3.upper()
                                   valid_option3_list = ["O", "o", "V", "v"]
                                   if option3 not in valid_option3_list:
                                       print("That is not a valid input")
                                   if selection2 == "O":
                                       flag2 = False
                                       flag1 = True
                                       break
                                   if selection2 == "V":
                                       result = viewTheDescription(pokemon)
                                       print(result)
                                       print()
                                       flag4 = True
                                       while flag4:
                                           option4 = input("Move on to the next Pokémon challenge(O/o)\nI'm good, take me back to the menu.(G/g)\n")
                                           selection3 = option4.upper()
                                           valid_option4_list = ["O", "o", "G", "g"]
                                           if option4 not in valid_option4_list:
                                               print("That is not a valid input")
                                           if selection3 == "O":
                                               flag3 = False
                                               flag2 = False
                                               flag1 = True
                                               break
                                           if selection3 == "G":
                                               flag3 = False
                                               flag2 = False
                                               flag1 = False
                                               break

                       # nested if statement
                       if pokemon == "Mew":
                           if probability > 95 and probability <= 100:
                               success = True
                               print("You caught it!")
                               valueList.append(value)
                               my_Pokemon_List.append(pokemon)
                               #my_Pokemon_List = sorted(my_Pokemon_List)
                               flag3 = True
                               while flag3:
                                   option3 = input("Move on to the next Pokemon challenge(O/o)\nView the description(V/v)\n")
                                   selection2 = option3.upper()
                                   valid_option3_list = ["O", "o", "V", "v"]
                                   if option3 not in valid_option3_list:
                                       print("That is not a valid input")
                                   if selection2 == "O":
                                       flag2 = False
                                       flag1 = True
                                       break
                                   if selection2 == "V":
                                       result = viewTheDescription(pokemon)
                                       print(result)
                                       print()
                                       flag4 = True
                                       while flag4:
                                           option4 = input("Move on to the next Pokémon challenge(O/o)\nI'm good, take me back to the menu.(G/g)\n")
                                           selection3 = option4.upper()
                                           valid_option4_list = ["O", "o", "G", "g"]
                                           if option4 not in valid_option4_list:
                                               print("That is not a valid input")
                                           if selection3 == "O":
                                               flag3 = False
                                               flag2 = False
                                               flag1 = True
                                               break
                                           if selection3 == "G":
                                               flag3 = False
                                               flag2 = False
                                               flag1 = False
                                               break

                       if success == False:
                           print("The Pokémon escapes!")
                           flag5 = True

                           while flag5:
                               option2 = input("Give it another try(A/a)\nI want to move on. Take me back to Menu(M/m)\n")
                               selection = option2.upper()
                               valid_option2_list = ["A", "a", "M", "m"]
                               if selection not in valid_option2_list:
                                   print("That is not a valid input")
                               if selection == "A":
                                   flag1 = True
                                   break
                               if selection == "M":
                                   flag2 = False
                                   flag1 = False
                                   break


       elif option == valid_tuple[1]:
           print("These are the Pokemon you have right now")
          #Sorting of the contents of an List (not the built-in sort)
           temp = []
           #for loop
           for x in aList:
               temp.append(x[0])
           string = ''
           for i in my_Pokemon_List:
               string += i + ':' + str(aList[temp.index(i)][1]) + ' '

           print(string)
           while True:
               #try/except block
               try:
                   option5 = input("I want to trade my Pokémon for more balls(B/b)\nI'm good. Take me back to th menu.(G/g)")
                   selection4 = option5.upper()
                   if selection4 == "B":
                       output = tradeForPokemon(ballNum, my_Pokemon_List, valueList)
                       if type(output) == str:
                           print(output)
                       elif type(output) == int:
                           ballNum = output
                           if len(my_Pokemon_List) == 0:
                               print("You do not have any Pokemon")
                           else:
                               print("You now have the following Pokemon(s):")
                               print(my_Pokemon_List)
                               print("You have " + str(ballNum) + " Balls.")

                   elif selection4 == "G":
                       flag1 = False
                       break
                   else:
                       print("Enter a valid letter to continue the game: ")
               except:
                   print("Enter a valid letter to continue the game: ")



       elif option in valid_tuple[2]:
           print("You have " + str(ballNum) + " balls.")
           while True:
               try:
                   option6 = input("I want to add more balls.(M/m)\nI'm good. Take me back to th menu.(G/g)")
                   selection5 = option6.upper()
                   if selection5 == "M":
                       output = tradeForPokemon(ballNum, my_Pokemon_List, valueList)
                       if type(output) == str:
                           print(output)
                       elif type(output) == int:
                           ballNum = output
                           if len(my_Pokemon_List) == 0:
                               print("You do not have any Pokemon")
                           else:
                               print("You now have the following Pokemon(s):")
                               print(my_Pokemon_List)
                               print("You have " + str(ballNum) + " Balls.")

                   elif selection5 == "G":
                       flag1 = False
                       break
                   else:
                       print("Enter a valid letter to continue the game: ")
               except:
                   print("Enter a valid letter to continue the game: ")



       elif option in valid_tuple[3]:
           ##Function Definition with Parameters and Function Call
           output = tradeForPokemon(ballNum, my_Pokemon_List, valueList)
           if type(output) == str:
               print(output)
           elif type(output) == int:
               ballNum = output
               if len(my_Pokemon_List) == 0:
                   print("You do not have any Pokemon")
               else:
                   print("You now have the following Pokemon(s):")
                   print(my_Pokemon_List)
                   print("You have " + str(ballNum) + " Balls.")



       elif option in valid_tuple[4]:
           print("You have exited the game")
           print("These are the Pokemon you have at the end of the game: ")
           print(my_Pokemon_List)
           print("You have used " + str(usedBall) + " Balls.")
           print("You have " + str(ballNum) + " Balls.")
           break
       else:
           print()
           print("That's not a valid input")
           flag2 = True

#Function Definition with Parameters and Function Call
def viewTheDescription(pokemon):
   if pokemon == "Bulbasaur":
       return "Name: Bulbasaur\nLevel: Rare (10)\nType: Grass\nDescription: Bulbasaur is a small, quadruped Pokémon that has blue-green skin with darker patches.\nIt has red eyes with white pupils, pointed, ear-like structures on top of its head, and a short, blunt snout with a wide mouth."
   if pokemon == "Caterpie":
       return "Name: Caterpie\nLevel: Common (3)\nType: Bug\nDescription: Caterpie is a Pokémon that resembles a green caterpillar with a yellow underside and teardrop-shaped tail."
   if pokemon == "Charmander":
       return "Name: Charmander\nLevle: Rare (10)\nType: Fire\nDescription: Charmander is a bipedal, reptilian Pokémon with a primarily orange body and blue eyes.\nA fire burns at the tip of this Pokémon's slender tail and has blazed there since Charmander's birth.\nThe flame can be used as an indication of Charmander's health and mood, burning brightly when the Pokémon is strong, weakly when it is exhausted, wavering when it is happy, and blazing when it is enraged."
   if pokemon == "Ditto":
       return "Name: Ditto\nLevel: Superior (25)\nType: Normal\nDescription: In its natural state, Ditto is a light purple or pink amorphous Pokémon with vestigial facial features.\nIt is capable of transforming into an exact replica of any physical object, including its form and abilities."
   if pokemon == "Eevee":
       return "Name: Eevee\nLevel: Rare (10)\nType: Normal\nDescription: Eevee is a mammalian, quadruped Pokémon with primarily brown fur.\nEevee is said to have an irregularly shaped genetic structure that is easily influenced by its environment.\nThis allows it to adapt to a variety of habitats by evolving."
   if pokemon == "Mew":
       return "Name: Mew\nLevel: Legendary (100)\nType: Psychic\nDescription: Mew is a pink, bipedal Pokémon with mammalian features.\nMew is said to have the DNA of every single Pokémon contained within its body,and as such is able to learn any attack."
   if pokemon == "Nidoran":
       return "Name: Nidoran\nLevel: Common (3)\nType: Poison\nDescription: Nidoran is a small, quadruped, rodent-like Pokémon.\nWhen angry, it extends its toxic spikes and charges, stabbing with its horn to inject poison. "
   if pokemon == "Paras":
       return "Name: Paras\nLevel: Common (3)\nType: Sand/Grass\nDescription: Paras is an orange, insectoid creature resembling the nymph stage of a cicada."
   if pokemon == "Pidgey":
       return "Name: Pidgey\nLevel: Common (3)\nType: Flying/Normal\nDescription: Pidgey is a small, plump-bodied avian Pokémon.\nIt is primarily brown with a cream-colored face, underside, and flight feathers. "
   if pokemon == "Pikachu":
       return "Name: Pikachu\nLevel: Rare (10)\nType: Electric\nDescription: Pikachu is a short, chubby rodent Pokémon.\nIt is covered in yellow fur with two horizontal brown stripes on its back.\nPikachu charges itself while sleeping overnight, though stress and a lack of sleep can affect this.\nIt is able to release electric discharges of varying intensity. "
   if pokemon == "Rattata":
       return "Name: Rattata\nLevel: Common (3)\nType: Normal\nDescription: Rattata is a small, quadruped rodent Pokémon.\nIt has purple fur with a cream-colored face, paws, and underbelly."
   if pokemon == "Sandshrew":
       return "Name: Sandshrew\nLevel: Common (3)\nType: Sand\nDescription: Sandshrew is a bipedal mammalian Pokémon, but runs on all fours in the anime.\nIts brick-patterned yellow hide is dry, tough, blends in with desert sand, and protects its soft white underbelly and muzzle."
   if pokemon == "Snorlax":
       return "Name: Snorlax\nLevel: Superior (25)\nType: Normal\nDescription: Snorlax is a huge, bipedal, dark blue-green Pokémon with a cream-colored face, belly, and feet.\nIts body is composed of mostly its belly, where most of its fat reserves accumulate.\nSnorlax can show awesome power when prompted. "
   if pokemon == "Squirtle":
       return "Name: Squirtle\nLevel: Rare (10)\nType: Water\nDescription: Squirtle is a small Pokémon that resembles a light blue turtle.\nSquirtle can spray foamy water from its mouth with great accuracy."
   if pokemon == "Zubat":
       return "Name: Zubat\nLevel: Common (3)\nType: Flying/Poison\nDescription: Zubat is a blue, bat-like Pokémon.\nWhile it lacks eyes, it has pointed ears with purple insides and a mouth with two sharp teeth on each jaw."


#Function Definition with Parameters and Function Call
def tradeForPokemon(ballNum, my_Pokemon_List, valueList):
   if len(my_Pokemon_List) == 0:
       return "No Pokemon to trade"
   else:
       flag = True
       while flag:
           try:
               #Function Definition with Parameters and Function Call
               a = pokemonValue(ballNum, my_Pokemon_List, valueList, flag)
               if type(a) == int:
                   x = a
                   willTrade = input("Would you trade?\n(Y/N) ")
                   willTrade = willTrade.upper()
                   if willTrade == "Y":
                       del my_Pokemon_List[x]
                       ballNum += valueList[x]
                       del valueList[x]
                       additional = input("Will you trade more balls?\n(Y/N) ")
                       additional = additional.upper()
                       if additional == "Y":
                           flag = True
                       elif additional == "N":
                           flag = False
                           break
                       else:
                           print("Not valid. Try again.")
                           additional = input("Will you trade more balls?\n(Y/N) ")
                   elif willTrade == "N":
                       additional = input("Will you trade more balls?\n(Y/N) ")
                       additional = additional.upper()
                       if additional == "Y":
                           flag = True
                       elif additional == "N":
                           flag = False
                           break
                       else:
                           print("Not valid. Try again.")
                           additional = input("Will you trade more balls?\n(Y/N) ")
               else:
                   if a == "No more Pokemon to trade":
                       flag = False
                   else:
                       anotherTrade = a
                       if anotherTrade == "N":
                           flag = False
                           break
           except ValueError:
               new = route()
   return ballNum

#Function Definition with Parameters and Function Call
def pokemonValue(ballNum, my_Pokemon_List, valueList, flag):

   while True:
       #Using len with a purpose
       if len(my_Pokemon_List) == 0:
           return "No more Pokemon to trade"
       else:
           #myPokemon = ", ".join(my_Pokemon_List)
           print(my_Pokemon_List)
           pokemontrade = input("Which Pokémon would you like to trade? ")
           pokemontrade = pokemontrade.lower()
           pokemontrade = pokemontrade.capitalize()
           if pokemontrade in my_Pokemon_List:
               i = my_Pokemon_List.index(pokemontrade)
               valueForBalls = valueList[i]
               #Using the formatting for strings
               print("The value of this Pokémon is {0}".format(valueForBalls))
               return i
           else:
               print("Not found. Try again")
               additional = input("Will you trade more balls?\n(Y/N) ")
               additional = additional.upper()
               if additional == "Y":
                   #A function that calls another function (main not included)
                   tradeForPokemon(ballNum, my_Pokemon_List, valueList)
               elif additional == "N":
                   return "N"
                   break
               else:
                   print("Not valid. Try again.")
                   additional = input("Will you trade more balls?\n(Y/N) ")
               return additional


main()
