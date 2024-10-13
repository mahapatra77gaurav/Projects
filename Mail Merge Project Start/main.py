#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as invited_names:
    invited_names_list = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    s_name = starting_letter.read()
    for name in invited_names_list:
        stripped_name = name.strip()
        new_letter = s_name.replace("[name]",stripped_name)
        with open(f"./Output/ReadyToSend/{stripped_name}_letter.txt","w") as invitation_letter:
            invitation_letter.write(new_letter)
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp