import random
import unicodedata

def main():
    def get_all_katakana():
        katakana_list = []
        for code_point in range(0x30A0, 0x30FF + 1):
            char = chr(code_point)
            if unicodedata.name(char, '').startswith('KATAKANA'):
                katakana_list.append(char)
        return katakana_list

# Example usage:
    katakana_chars = get_all_katakana()
    n = int(input("enter: "))
    result = []
    for number in range (n):
        result.append(random.choice(katakana_chars))

    katakana_string = " ".join(result)

    with open('katakana_output.txt', 'w', encoding='utf-8') as file:
        file.write(katakana_string)


if __name__ == "__main__":
    main()