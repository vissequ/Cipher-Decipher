import sys
import argparse

def cipher(text):
    """
    Converts each letter in the input string to its numerical position in the alphabet (A=1, B=2, ..., Z=26),
    ignoring case and non-letter characters. Groups numbers by words using dashes within words and spaces between words.
    """
    text = text.upper()
    words = text.split()  # Split on whitespace
    result_words = []
    for word in words:
        nums = []
        for char in word:
            if char.isalpha():
                num = ord(char) - ord('A') + 1
                nums.append(str(num))
        if nums:
            result_words.append('-'.join(nums))
    return ' '.join(result_words)

def decipher(text):
    """
    Converts space-separated groups of dash-separated numbers back to letters (1=A, 2=B, ..., 26=Z),
    forming words separated by spaces. Ignores invalid numbers or those out of range.
    Returns the uppercase string with spaces between words.
    """
    words = text.split()  # Split on spaces for word groups
    result_words = []
    for word in words:
        parts = word.split('-')
        letters = []
        for part in parts:
            try:
                num = int(part)
                if 1 <= num <= 26:
                    char = chr(ord('A') + num - 1)
                    letters.append(char)
            except ValueError:
                pass  # Ignore invalid entries
        if letters:
            result_words.append(''.join(letters))
    return ' '.join(result_words)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        mode = input("Enter 'c' for cipher or 'd' for decipher: ").strip().lower()
        if mode not in ['c', 'd']:
            print("Invalid mode")
            sys.exit(1)
        if mode == 'c':
            input_text = input("Enter the string to cipher: ").strip()
        else:
            input_text = input("Enter the numbers to decipher: ").strip()
    else:
        parser = argparse.ArgumentParser(description="Cipher/Decipher script")
        parser.add_argument("--mode", choices=['c', 'd'], default='c', help="c for cipher (default), d for decipher")
        parser.add_argument("input_text", nargs='*', help="Input text or numbers")
        args = parser.parse_args()
        mode = args.mode
        input_text = ' '.join(args.input_text)
        if not input_text:
            if mode == 'c':
                input_text = input("Enter the string to cipher: ").strip()
            else:
                input_text = input("Enter the numbers to decipher: ").strip()

    if mode == 'c':
        print(cipher(input_text))
    elif mode == 'd':
        print(decipher(input_text))
