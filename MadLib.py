#MadLib.py
#Name: Levi Woockman
#Date: 8/30/24
#Assignment: Lab 1

def main():
  print("Madlib")
  #Ask user for words
  noun1=input("Enter place: ")
  noun2=input("Enter animal: ")
  verb1=input("Enter verb: ")
  adjective1=input("Enter adjetive: ")
  noun3=input("Enter noun: ")
  adjective2=input("Enter feeling: ")

  #Print the story with the user supplied words.
  print("On Sunday I went to the " + noun1 + " and saw a " + noun2 + " doing " + verb1 + ".")
  print("This " + noun2 + " was very " + adjective1 + " so I gave it " + noun3 + " for some reason this " + noun2 + " was " + adjective2 + " as hell and mauled me to death.")

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
