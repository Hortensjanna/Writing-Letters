
with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()


with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter_text = starting_letter.read()
    for name in names_list:
        stripped_name = name.strip()
        new_letter = letter_text.replace("[name]", stripped_name)

with open(f"./Output/ReadyToSend/letter_to_{stripped_name}.txt", "w") as completed_letter:
    completed_letter.write(new_letter)



