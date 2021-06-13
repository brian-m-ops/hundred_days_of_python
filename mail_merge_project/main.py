PLACEHOLDER = "[name]"

with open("input/names/invited_names.txt") as invited_names:
    names = invited_names.readlines()
    print(names)

with open("input/letters/starting_letter.txt") as starting_letter:
    letter_contents = starting_letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # print(new_letter)
        with open(f"output/ready_to_send/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
