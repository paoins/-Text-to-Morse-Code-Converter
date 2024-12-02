morse_code = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}


def text_morse(text_input):
    text_input = text_input.upper()
    morse = []
    for letter in input:
        if letter in morse_code:
            morse.append(morse_code[letter])
        elif letter == ' ':
            morse.append(' ')
        else:
            return f'Invalid character: {letter}'
    morse_result = '/'.join(morse)
    return morse_result


def morse_text(morse_input):
    morse_input = morse_input.split('/')
    reversed_morse_code = {v: k for k, v in morse_code.items()}
    text = []
    for char in input:
        if char in morse_input:
            text.append(morse_code[char])
        else:
            return f'Invalid character: {char}'
    return ''.join(text)

mode = input('Enter M for text to morse and T for Morse to T')
input = input('Enter text: ')

if mode == 'M':
    result = text_morse(input)
    print(result)
elif mode == 'T':
    result = morse_text(input, morse_code)
    print(result)
else:
    print('Invalid mode! Please enter M for text to Morse or T for Morse to Text.')


