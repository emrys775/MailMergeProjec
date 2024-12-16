
# PlaceHolder = "[Name]"
# Open and read the starting letter
with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_template = letter_file.read()

# Open and read the names from the invited_names file
with open("./Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()

# Folder name where letters will be saved
output_folder = "ReadyToSend"

# Generate and save letters for each name
for name in names:
    # Strip any extra whitespace/newline
    clean_name = name.strip()

    # Replace [name] placeholder with the actual name
    personalized_letter = letter_template.replace("[name]", clean_name)

    # Save the personalized letter in a new file
    with open(f"./Output/ReadyToSend/letter_for_{clean_name}.txt", "w") as output_file:
        output_file.write(personalized_letter)

print("Letters generated and saved successfully!")
