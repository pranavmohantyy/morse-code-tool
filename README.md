# Morse Code Tool

This is a simple Morse code encoder and decoder that supports letters, numbers, and some punctuation.

## Features
- Encode messages into Morse code.
- Decode Morse code back into readable text.
- Supports file input/output.

## Usage
1. Import the `morse` module.
2. Use `encode(message)` to get Morse code.
3. Use `decode(morse_code)` to revert back to text.

## Example
```python
encoded = encode('Hello, World!')
print(encoded)

decoded = decode(encoded)
print(decoded)
```