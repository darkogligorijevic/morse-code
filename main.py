import tkinter as tk
import winsound
import time

# Morse code dictionary
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

# Function that transform a text to a morse code
def text_to_morse():

    text = entry.get()

    for letter in text.upper():
        if letter == ' ':
            time.sleep(1)
        else:
            for char in morse_code_dict[letter]:
                if char == '.':
                    winsound.Beep(1000, 200)
                elif char == '-':
                    winsound.Beep(1000, 400)
        time.sleep(0.2)

# Function that transform a morse code to a text
def morse_to_text():

    morse_result = ""
    morse_entry = entry.get()
    morse_list = morse_entry.split(' ')

    for each_morse in morse_list:
        morse_key = [k for k, v in morse_code_dict.items() if v == each_morse]
        morse_result += ''.join(morse_key)
        label_result.config(text=morse_result)
        


root = tk.Tk()
root.title("Morse Code Converter")

# Window size
root.minsize(400, 200)
root.maxsize(800, 400)

# Frame for a better style
frame = tk.Frame(root, pady=10)
frame.pack(expand=True, fill="both")

# Label for entry field
label_text = tk.Label(frame, text="Enter text: ", font=("Helvetica", 12))
label_text.pack(padx=8)

# Entry widget
entry = tk.Entry(frame, font=("Helvetica", 14))
entry.pack(pady=10, padx=10, fill="both")

# Button for text to morse
button1 = tk.Button(frame, text="Convert to Morse Code", command=text_to_morse, font=("Helvetica", 12))
button1.pack(pady=10)

# Button for morse to text
button2 = tk.Button(frame, text="Convert to Text", command=morse_to_text, font=("Helvetica", 12))
button2.pack(pady=10)

# Label that displays result 
label_result = tk.Label(frame, text="", font=("Helvetica", 24))
label_result.pack(padx=20)

# Main loop
root.mainloop()
