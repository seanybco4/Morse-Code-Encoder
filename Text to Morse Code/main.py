# imports
from playsound import playsound
from tkinter import *

# variables
coded_text = "*****your encoded message will appear here*****"
morse_code_dict = {
	'a': '•➖', 'b': '➖•••', 'c': '➖•➖•', 'd': '➖••', 'e': '•',
	'f': '••➖•', 'g': '➖➖•', 'h': '••••', 'i': '••',
	'j': '•➖➖➖', 'k': '➖•➖', 'l': '•➖••', 'm': '➖➖', 'n': '➖•',
	'o': '➖➖➖', 'p': '•➖➖•', 'q': '➖➖•➖', 'r': '•➖•',
	's': '•••', 't': '➖', 'u': '••➖', 'v': '•••➖', 'w': '•➖➖',
	'x': '➖••➖', 'y': '➖•➖➖', 'z': '➖➖••', '0': '➖➖➖➖➖',
	'1': '•➖➖➖➖', '2': '••➖➖➖', '3': '•••➖➖', '4': '••••➖',
	'5': '•••••', '6': '➖••••', '7': '➖➖•••', '8': '➖➖➖••',
	'9': '➖➖➖➖•', ' ': ' / ', ".": "•➖•➖•➖", ",": "➖➖••➖➖",
    "?": "••➖➖••", "!": "➖•➖•➖➖", "=": "➖•••➖", ":": "➖➖➖•••",
    ";": "➖•➖•➖•", "'": "•➖➖➖➖•", "/": "➖••➖•", "➖": "➖••••➖",
    "_": "••➖➖•➖", '"': "•➖••➖•", "(": "➖•➖➖•", ")": "➖•➖➖•➖",
    "$": "•••➖••➖", "&": "•➖•••", "@": "•➖➖•➖•", "+": "•➖•➖•",
}

# create window and canvas
window = Tk()
window.title("Morse Code Encoder")
canvas = Canvas(window, bg="blue", height=700, width=1000)

# create background image
filename = PhotoImage(file="MC.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# create text entry box
entry1 = Entry(window, width=30, fg="red", font=('Courier 24'))
entry1.insert(0, "write message to encode here")
entry1.configure(state=DISABLED)

# create button
button1 = Button(text='*ENCODE MESSAGE*', width=18, fg="red", font=('Courier 14 bold'), command=lambda: convert_to_morse_code(entry1.get()))

# create translation label
label1 = Label(text=coded_text, width=170, fg="blue", font=('Courier 8'))

# FUNCTIONS

# make entry box placeholder text disappear on click
def on_click(event):
    entry1.configure(state=NORMAL)
    entry1.delete(0, END)

    # make the callback only work once
    entry1.unbind('<Button-1>', on_click_id)

on_click_id = entry1.bind('<Button-1>', on_click)

def convert_to_morse_code(text):
	global coded_text
	coded_text = ""
	for char in text:
		try:
			morse_character = morse_code_dict[char]
			coded_text += morse_character + " "
		except KeyError:
			coded_text += f"(could not convert: {char}) "
	label1["text"] = coded_text

# add canvas to window
canvas.pack(expand="yes")

# add widgets to canvas
canvas.create_window(500, 550, window=button1)
canvas.create_window(500, 500, window=entry1)
canvas.create_window(500, 600, window=label1)

# play morse_code sound at start
playsound("MC_sound.wav")

window.mainloop()