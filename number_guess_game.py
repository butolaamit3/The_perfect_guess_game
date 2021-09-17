#no,guess game


n=19
number_of_gusses=1
print("you have 9 number of gusses" )
while number_of_gusses<=9:
  number=int(input("Enter your number:"))
  if number<n:
    print("your guess is too low")
  elif number >n:
    print("your guess is too high")
  else:
    print("you exactly guess the number")
    print(number_of_gusses, "no. of guesses you took to finish")
    break
  print(9-number_of_gusses, "number_of_guesses_left")
  number_of_gusses=number_of_gusses+1

if number_of_gusses>9:
  print("game over")
