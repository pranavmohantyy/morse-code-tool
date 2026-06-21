morse_dict = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", " ": " " }

def encode(message):
    return ' '.join(morse_dict.get(char.upper(), '') for char in message)

def decode(morse_code):
    return ''.join([next(key for key, value in morse_dict.items() if value == code) for code in morse_code.split()])

import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Morse code encoder/decoder')
    parser.add_argument('--file', '-f', help='input file with text or morse code')
    parser.add_argument('--output', '-o', help='output file for results')
    parser.add_argument('text', nargs='?', help='text to encode or decode')
    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as f:
            text = f.read().strip()
    else:
        text = args.text

    if text:
        if all(char in '.- ' for char in text):
            result = decode(text)
        else:
            result = encode(text)

        if args.output:
            with open(args.output, 'w') as f:
                f.write(result)
        else:
            print(result)

if __name__ == '__main__':
    main()