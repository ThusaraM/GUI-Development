from tkinter import *

#Creating the window
root = Tk()
root.title("Arithmetic and Geometric Calculator")
root.geometry("400x400")

#Defining the sum function
def calculate_sum():
    #Defining each variable
    global first_term
    first_term = float(entry_first_term.get())
    global common_difference
    common_difference = float(entry_common_difference.get())
    global number_of_terms
    number_of_terms = int(entry_number_of_terms.get())
    global common_ratio
    common_ratio = int(entry_common_ratio.get)

#Code for the arithmetic series
def calculate_arithmetic_sum():

    arithmetic_sum = (number_of_terms / 2)*(2*first_term + ((number_of_terms) - 1)*common_difference)

#Code for the geometric series
def calculate_geometric_sum():
    geometric_sum = first_term*(common_ratio**number_of_terms - 1) / common_ratio - 1

#Creating the GUI
label_first_term = Label(root, text="First Term:")
label_first_term.grid(row=0, column=0)
entry_first_term = Entry(root)
entry_first_term.grid(row=0, column=1)

label_number_of_terms = Label(root, text="Number of Terms: ")
label_number_of_terms.grid(row=1, column=0)
entry_number_of_terms = Entry(root)
entry_number_of_terms.grid(row=1, column=1)

label_common_difference = Label(root, text="Common Difference: ")
label_common_difference.grid(row=2, column=0)
entry_common_difference = Entry(root)
entry_common_difference.grid(row=2, column=1)

label_common_ratio = Label(root, text="Common Ratio: ")
label_common_ratio.grid(row=3,column=0)
entry_common_ratio = Entry(root)
entry_common_ratio.grid(row=3, column=1)

calculate_button = Button(root, text="Calculate")
calculate_button.grid(row=6, column=4, pady=(200, 0))
clear_button = Button(root, text="Clear")
clear_button.grid(row=7, column=4, pady=(25, 0))

root.mainloop()