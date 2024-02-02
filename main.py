import tkinter as tk

window = tk.Tk()
window.title("ANSPDR")
window.geometry("900x700")
window.configure(bg="#F8DFD4")
heading = tk.Label(window, text="Mnemonic Phrase Generator", font=("Arial", 28, "bold"), fg="#030637", bg="#F8DFD4")

heading.place(relx=0.5, rely=0.4, anchor='center')
auther = tk.Label(window, text="by @anspdr", bg='#F8DFD4')
auther.place(relx=0.6, rely=0.3, anchor='center')

input_bar = tk.Entry(window, justify='center', width=50)
input_bar.place(relx=0.5, rely=0.5, anchor='center')

# Create a label for the output
output_label = tk.Label(window, text="", font=("Arial", 20), bg="#F8DFD4")
output_label.place(relx=0.5, rely=0.7, anchor='center')


def create_mnemonic():
    word_dict = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
    words = input_bar.get().split()

    meaningful_words = [word_dict.get(word[0], word[0]) for word in words]
    mnemonic = '\n'.join(meaningful_words)
    output_label['text'] = mnemonic

def clear_text():
    input_bar.delete(0, 'end')
    output_label['text'] = ""

submit_button = tk.Button(window, text="Generate", command=create_mnemonic, bg="#F8DFD4")
submit_button.place(relx=0.3, rely=0.5, anchor='center')

clear_button = tk.Button(window, text="Clear", command=clear_text, bg="#F8DFD4")
clear_button.place(relx=0.65, rely=0.5, anchor='center')

window.mainloop()
