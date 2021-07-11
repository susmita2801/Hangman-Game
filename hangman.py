
from random import choice

def word_generator():
  with open("untitled.txt" , "r") as f:
    lines = f.readlines()
  f.close()
  lines = [i.strip("\n") for i in lines]
  return choice(lines)


  word_generator()  

word = word_generator()
guessed = " "
turns = int(len(word)*1.5)
while(True):
  print("You are left with {} turns".format(turns))
  inp = input("\n Make a guess :")
  turns = turns - 1
  if inp in word:
    guessed = guessed + inp
  unguessed_char = 0
  for i in word:
    if i in guessed:
      print(i,end="")
    else:
      unguessed_char += 1
      print("*" ,end = "")
  if unguessed_char == 0:
    print("\nHurry !!! you won...")
    break
  if turns == 0:
    print("\n toin toin toin ........ you are out of attempts")
    break  