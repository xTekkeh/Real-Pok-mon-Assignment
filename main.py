import string
import itertools
a = 0

pokémon = [ "Pikachu", "Charizard", "Eevie", "MissingNo", "Mewtwo", "Ditto"]
  
attacks = [ "Thunderbolt", "Break Burn", "Growl", "✌︎⧫︎⧫︎♋︎♍︎🙵", "Breakburn", "Shapeshifter"]

inpu = input("Hello, Please State Your Name!\n")
print("Hello, %s! Now Here is your party!" % inpu)

print("Pikachu", "Charizard", "Eevie", 
"MissingNo", "Mewtwo", "Ditto")

party = input("Do You Accept This Party?\n")
if party == ("Yes"):
  print("Ok, Good Luck Out There!")
else:
  print("Well, Too Bad, Good Luck Out There!")

flag = 0
while flag == 0:
  inpuu = input("What Pokémons' stats would you like to learn about? To stop displaying stats, type 'stop'.")
  if(inpuu==pokémon[0]):
    print("Pikachu uses attack name Thunderbolt!")
  elif(inpuu==pokémon[1]):
    print("Charizard uses attack name Break Brun!")
  elif(inpuu==pokémon[2]):
    print("Eevie uses attack name Growl!")
  elif(inpuu==pokémon[3]):
    print("MissingNo uses attack name ✌︎⧫︎⧫︎♋︎♍︎🙵!")
  elif(inpuu==pokémon[4]):
    print("MewTwo uses attack name Psycho Cut!")
  elif(inpuu==pokémon[5]):
    print("Ditto uses attack name Shapeshifter!")
  elif(inpuu=="stop"):
    print("Shutting Down, Goodbye Now! ")
    keepLooping=1
  else:
    print("That's not a thing, Try asking again...")

  
print("Here are the stats, Anything else you want to learn?")

print("Currently in your backpack, you have: Pikachu, Charizard, Eevie,MissingNo, and Ditto!")













