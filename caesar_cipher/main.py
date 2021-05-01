from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    result = ''

    for char in start_text:
        if cipher_direction == 'encode':
            if char not in alphabet:
                result += char
            else:
                cipher_index = alphabet.index(char) + shift_amount
                result += alphabet[cipher_index]
        elif cipher_direction == 'decode':
            if char not in alphabet:
                result += char
            else:
                text_index = alphabet.index(char) - shift_amount
                result += alphabet[text_index]

    print(f'The {cipher_direction}d text is {result}\n')


print(logo)

game_end = False
while not game_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26  # Allows for users inputting large shift numbers

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == 'no':
        game_end = True
        print("Bye")
