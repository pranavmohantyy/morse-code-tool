morse_dict = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", " ": " " }

def encode(message):
    return ' '.join(morse_dict.get(char.upper(), '') for char in message)

def decode(morse_code):
    words = morse_code.split('  ')
    decoded = []
    for word in words:
        letters = word.split()
        decoded.append(''.join(next((k for k, v in morse_dict.items() if v == letter), '') for letter in letters))
    return ' '.join(decoded)

if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='Morse code encoder/decoder')
    subparsers = parser.add_subparsers(dest='command')

    encode_parser = subparsers.add_parser('encode')
    encode_parser.add_argument('text', nargs='?', type=str)

    decode_parser = subparsers.add_parser('decode')
    decode_parser.add_argument('morse', nargs='?', type=str)

    args = parser.parse_args()

    if args.command == 'encode':
        text = args.text or sys.stdin.read()
        print(encode(text))
    elif args.command == 'decode':
        morse = args.morse or sys.stdin.read()
        print(decode(morse))
