#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
PLACEHOLDER ="[name]"



with open("./Input/Names/invited_names.txt") as name_file:
    names= name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_files:
    letter_content=letter_files.read()
    for name in names:
        stripped_names=name.strip()
        new_letter=letter_content.replace(PLACEHOLDER,stripped_names)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_names}.txt", mode="w") as completed_letter:
          completed_letter.write(new_letter)
      

