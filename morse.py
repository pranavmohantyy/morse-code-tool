morse_dict = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", " ": " " }

def encode(message):
    return ' '.join(morse_dict.get(char.upper(), '') for char in message)

def decode(morse_code):
    words = morse_code.split(' ')
    return ''.join(next((k for k, v in morse_dict.items() if v == word), '') for word in words)

def visual_playback(morse_code):
    import time
    for char in morse_code:
        if char == '.':
            print('.', end='', flush=True)
        elif char == '-':
            print('-', end='', flush=True)
        time.sleep(0.5)
    print()