POSITION = "[name]"

with open("./Input/Names/invited_names.txt") as name_files:
    names = name_files.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_files:
    content_letter = letter_files.read()
    for name in names:
        stripped_name = name.strip()
        letter_with_name = content_letter.replace(POSITION,stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}",mode="w") as letter:
            letter.write(letter_with_name)