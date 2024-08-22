alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caeser(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1
  
    for letter in original_text:
        if letter not in original_text:
            output_text += letter
        else:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Here is your {encode_or_decode}d result: {output_text}") 

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encode the message and 'decode' to decode the message\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number: "))

    caeser(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_continue = False
        print("GoodBye!")