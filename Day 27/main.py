from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(height=300, width=500)
window.config(padx=100, pady=100)

# Label
my_label = Label(text="I am a Label", font=('Arial', 24, 'bold'))
my_label.config(text = 'New Text')
my_label.grid(column=0, row=0, padx=10, pady=10)

# Button
button = Button(text="I am a button")
button.grid(column=0, row=1, padx=10, pady=10)

# Button
new_button = Button(text='I am a new button')
new_button.grid(column=2,row=0, padx=10, pady=10)

# Entry
my_input = Entry(width=10)
print(my_input.get())
my_input.grid(row=2, column=3, padx=10, pady=10)

window.mainloop()

