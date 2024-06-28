import tkinter as tk
import tkinter.font as font
import random
import wordlist

bg_color = "white"

window = tk.Tk()
window.geometry("300x600")
window.title("Pride Conversation")
window.configure(background=bg_color)


# Customised Fonts
big_text = font.Font(family="Helvetica", size=24, weight="bold")
default_text = font.Font(family="Helvetica", size=12)
button_text = font.Font(family="Helvetica", size=14, weight="bold")

# Customised Widgets
class BigText(tk.Label):
    def __init__(self, parent, **kwargs):
        kwargs["font"] = big_text
        kwargs["bg"] = bg_color
        super().__init__(parent, **kwargs)

class DefaultText(tk.Label):
    def __init__(self, parent, **kwargs):
        kwargs["font"] = default_text
        kwargs["wrap"] = 200
        kwargs["bg"] = bg_color
        super().__init__(parent, **kwargs)

class DefaultButton(tk.Button):
    def __init__(self, parent, **kwargs):
        kwargs["font"] = button_text
        kwargs["fg"] = "white"
        super().__init__(parent, **kwargs)

word_list = wordlist.word_list

known_words = []    # Contains the words known by user

# Randomly choose a word from the word list
word_to_display = random.choice(word_list)

# Functions

def show_meaning(user_knows:bool):
    global word_to_display
    
    if user_knows:
        known_words.append(word_to_display)
        word_list.remove(word_to_display)
        # Display the "I got this" and "I understood it differently" buttons but not the "I understand now" button
        correct_button.pack(pady=20)
        wrong_button.pack()

        understand_button.pack_forget()
    else:
        # Only display the "I understand now" button
        correct_button.pack_forget()
        wrong_button.pack_forget()

        understand_button.pack(pady=50)
        
        
    WORD_screen.pack_forget()
    MEANING_screen.pack()

def next_word(user_got_this:bool):
    global word_list, word_to_display

    if len(word_list) > 0:

        if not(user_got_this):
            if word_to_display in known_words:
                word_list.append(word_to_display)
                known_words.remove(word_to_display)
        
        word_to_display = random.choice(word_list)
        
        MEANING_screen.pack_forget()
        word_label.configure(text=word_to_display["word"])
        meaning_label.configure(text=word_to_display["word"] + " means " + word_to_display["meaning"])
        WORD_screen.pack()

    else:
        # Show the end screen
        pass


question_label = DefaultText(window, text="Do you know the words used in the rainbow community?")
question_label.pack()

# Widgets for the screen containing the word
WORD_screen = tk.Frame(window, height=600, bg=bg_color)
WORD_screen.pack()

word_label = BigText(WORD_screen, text=word_to_display["word"])
word_label.pack(pady=50)

yes_button = DefaultButton(WORD_screen, text="I know this!", bg="green", command=lambda: show_meaning(True))
yes_button.pack(pady=20)

no_button = DefaultButton(WORD_screen, text="Not sure.", bg="red", command=lambda: show_meaning(False))
no_button.pack()

# Widgets for the screen containing the meaning
MEANING_screen = tk.Frame(window, bg=bg_color)

meaning_label = DefaultText(MEANING_screen, text=word_to_display["word"] + " means " + word_to_display["meaning"])
meaning_label.pack(pady=50)

correct_button = DefaultButton(MEANING_screen, text="I got this!", bg="green", command=lambda: next_word(True))
wrong_button = DefaultButton(MEANING_screen, text="I understood it differently", bg="red", command=lambda: next_word(False))
understand_button = DefaultButton(MEANING_screen, text="I understand now.", bg="orange", command=lambda: next_word(False))

window.mainloop()
