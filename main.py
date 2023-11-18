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

    text_result = ''

    text_entry = entry.get().upper()
    split_space = text_entry.split(' ')

    for word in split_space:
        for letter in word:
            for symbol in morse_code_dict[letter]:
                if symbol == '.':
                    winsound.Beep(1000, 200)
                elif symbol == '-':
                    winsound.Beep(1000, 400)
            text_result += ''.join(morse_code_dict[letter]) + ' '
            time.sleep(0.2)
        time.sleep(0.5)
        text_result += '/'

    label_result.config(text=text_result[:-1])

# Function that transform a morse code to a text
def morse_to_text():

    morse_result = ''
    current_morse = ''
    morse_entry = entry.get()

    split_slash = morse_entry.split('/')

    for word in split_slash:
        split_space = word.split(' ')
        current_morse = ''
        for symbol in split_space:
            morse_key = [k for k, v in morse_code_dict.items() if v == symbol]
            current_morse += ''.join(morse_key)
        morse_result += current_morse + ' '
    
    label_result.config(text=morse_result)
        

# Declaring tkinter 
root = tk.Tk()
root.title('Morse Code Converter')

# Window size
root.minsize(400, 200)
root.maxsize(800, 400)

# Frame for a better style
frame = tk.Frame(root, pady=10)
frame.pack(expand=True, fill='both')

# Label for entry field
label_text = tk.Label(frame, text='Enter text: ', font=('Helvetica', 12))
label_text.pack(padx=8)

# Entry widget (input field)
entry = tk.Entry(frame, font=('Helvetica', 14))
entry.pack(pady=10, padx=10, fill='both')

# Button for text to morse
button1 = tk.Button(frame, text='Convert to Morse Code', command=text_to_morse, font=('Helvetica', 12))
button1.pack(pady=10)

# Button for morse to text
button2 = tk.Button(frame, text='Convert to Text', command=morse_to_text, font=('Helvetica', 12))
button2.pack(pady=10)

# Label that displays results 
label_result = tk.Label(frame, text='', font=('Helvetica', 24))
label_result.pack(padx=20)

# Main loop
root.mainloop()
