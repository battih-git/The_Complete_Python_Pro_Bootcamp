from Tkinter import *
import ttkbootstrap as ttk
import ttkbootstrap.widgets

window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=500)

# Label
my_label = Label(text='I am a label', font=('Arial',24,'bold'))
my_label.pack()

def button_clicked():
    my_label.config(text=my_input.get())

button = Button(text='Clik me',command=button_clicked)
button.pack()


# Entry component
my_input = Entry(width=50)
my_input.insert(END, string="Some text to begin with.")
my_input.pack()
my_input.get()


# Text component
my_text = Text(height=5,width=20)
my_text.focus()
my_text.insert(END,"Write something here.")
my_text.pack()
my_text.get('1.0', END)

# Spinbox
def spin_box_use():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10,width=5,command=spin_box_use)
spinbox.pack()

# Scale
def scale_used(value):
    print(scale.get())
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Check box
def check_button():
    print(checked_state.get())
    # Prints 1 on checkbox state else 0
checked_state = BooleanVar()
checkbox = Checkbutton(text='is On?', variable=checked_state, command=check_button)
checkbox.pack()

# Radio button
def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radio_button_1 = Radiobutton(text='Option 1', value= 1, variable= radio_state, command=radio_used)
radio_button_2 = Radiobutton(text='Option 2', value= 2, variable=radio_state, command=radio_used)
radio_button_1.pack()
radio_button_2.pack()

# List box
def listbox_used():
    print(Listbox.get(listbox.curselection()))
listbox = Listbox(height=4)
fruits = ['Apple', 'Cherry', 'Banana', 'Orange']
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()