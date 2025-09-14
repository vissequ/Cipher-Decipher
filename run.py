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
        input_file = input("Enter the path to the input file: ").strip()
        with open(input_file, 'r', encoding='utf-8') as f:
            input_text = f.read().strip()
    else:
        parser = argparse.ArgumentParser(description="Cipher/Decipher script")
        parser.add_argument("--mode", choices=['c', 'd'], default='c', help="c for cipher (default), d for decipher")
        parser.add_argument("input_file", nargs='?', help="Input file path")
        args = parser.parse_args()
        mode = args.mode
        if args.input_file:
            input_file = args.input_file
        else:
            input_file = input("Enter the path to the input file: ").strip()
        with open(input_file, 'r', encoding='utf-8') as f:
            input_text = f.read().strip()

    if mode == 'c':
        print(cipher(input_text))
    elif mode == 'd':
        print(decipher(input_text))
