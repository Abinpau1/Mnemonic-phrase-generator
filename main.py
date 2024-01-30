import tkinter as tk

window = tk.Tk()
window.title("ANSPDR")
window.geometry("900x700")
window.configure(bg="#F8DFD4")
heading = tk.Label(window, text="Mnemonic Phrase Generator", font=("Arial", 28, "bold"), fg="#43766C", bg="#F8DFD4")

heading.place(relx=0.5, rely=0.4, anchor='center')
auther = tk.Label(window, text="by @anspdr", bg='#F8DFD4')
auther.place(relx=0.6, rely=0.3, anchor='center')

# # Create a label for the input bar
# input_label = tk.Label(window, text='Enter ',font=("Arial",20, "bold"))
# input_label.place(relx=0.5, rely=0.4, anchor='center')


# Create the input bar with centered text
input_bar = tk.Entry(window, justify='center', width=50)
input_bar.place(relx=0.5, rely=0.5, anchor='center')

submit_button = tk.Button(window, text="Generate", fg="black")
submit_button.place(relx=0.3, rely=0.5, anchor='center')

window.mainloop()
