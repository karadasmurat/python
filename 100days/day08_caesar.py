cache = {}

def main():
    title = '''
_________                                      
\_   ___ \_____    ____   ___________ _______  
/    \  \/\__  \ _/ __ \ /  ___/\__  \\_  __ \ 
\     \____/ __ \\  ___/ \___ \  / __ \|  | \/ 
 \______  (____  /\___  >____  >(____  /__|    
        \/     \/     \/     \/      \/        
              .__       .__                    
         ____ |__|_____ |  |__   ___________   
       _/ ___\|  \____ \|  |  \_/ __ \_  __ \  
       \  \___|  |  |_> >   Y  \  ___/|  | \/  
        \___  >__|   __/|___|  /\___  >__|     
            \/   |__|        \/     \/       
    '''
    print(title)
    
    operation = get_input("Welcome.", ["Encrypt", "Decrypt"]).lower()
    message = input("Type your message: ")
    result_header = "Here is the encoded result: "
    shift = int(input("Type shift number: "))

    if operation in ['d', "decode"]:
        shift *= -1
        result_header = "Here is the decoded result: "

    encoded_message = ""
    for c in message:
        encoded_message += encode_letter(c, shift)
    
    print(result_header, encoded_message)

def get_input(question, options):
    # surround first char of option with [ ]
    ops = ""
    for option in options:
        option = ' [' + option[:1] + ']' + option[1:]
        ops += option
    
    return input(f"{question} {ops}: ")

def encode_letter(letter, shift):

    # first check the cache if the letter has already been mapped before
    # if key in dict
    if letter in cache:
        print(f"found in cache :) {letter} -> {cache[letter]}")
        return cache[letter]

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    length_of_base = len(letters)
    for i in range(length_of_base):
        if letters[i] == letter:
            # put in cache first, for later reuse
            mapped_letter = letters[(i + shift) % length_of_base]
            cache[letter] = mapped_letter

            print("calculated and cached mapping: ", mapped_letter)
            return mapped_letter



if __name__ == "__main__" :
    main()