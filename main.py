import random
import unicodedata

def main():
    katakana_list = [chr(code) for code in range(0x30A0, 0x30FB) if code not in [0x30F7, 0x30F8, 0x30F9, 0x30FA, 0x30F5, 0x30F6, 0x30FB, 0x30F0, 0x30A0]]

    n = int(input("Enter the number of katakana characters to be generated: "))
    result = []
    for _ in range(n):
        result.append(random.choice(katakana_list))

    katakana_string = " ".join(result)

    with open('katakana_output.txt', 'w', encoding='utf-8') as file:
        file.write(katakana_string)

if __name__ == "__main__":
    main()
