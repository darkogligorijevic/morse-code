import winsound
import time

# Function that transform a text to a morse code
def text_to_morse(text):
    morse_code_dict = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..'
    }

    for letter in text.upper():
        for char in morse_code_dict[letter]:
            if char == '.':
                winsound.Beep(1000, 200)
            elif char == '-':
                winsound.Beep(1000, 400)
        time.sleep(0.4)

if __name__ == "__main__":
    input_text = input("Enter text to convert to Morse code: ")
    morse_code = text_to_morse(input_text)
