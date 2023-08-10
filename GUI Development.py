from tkinter import *

#Defining the sum function
def calculate_sum():
    #Defining each variable
    first_term = float(enter_first_term())
    common_difference = float(enter_common_difference())
    number_of_terms = int(enter_number_of_terms())
    common_ratio = int(enter_common_ratio)

#Code for the arithmetic series
def calculate_arithmetic_sum():

    arithmetic_sum = (number_of_terms / 2)*(2*first_term + ((number_of_terms) - 1)*common_difference)

#Code for the geometric series
def calculate_geometric_sum():
    geometric_sum = first_term*(common_ratio**number_of_terms - 1) / common_ratio - 1

#Creating the GUI
label_first_term = Label(window, text="First Term:")
label_first_term.grid(row=0, column=0)
entry_first_term = Entry(window)
entry_first_term.grid()

label_number_of_terms = Label(window, text="Number of Terms: ")
label_number_of_terms.grid()
entry_number_of_terms = Entry(window)
entry_number_of_terms.grid(row=0, column=1)

label_common_difference = Label(window, text="Common Difference: ")
label_common_difference.grid(row=1, column=0)
entry_common_difference = Entry(window)
entry_common_difference.grid(row=1, column=1)

label_common_ratio = Label(window, text="Common Ratio: ")
label_common_ratio.grid(row=2,column=0)
entry_common_ratio = Entry(window)
entry_common_ratio.grid(row=2, column=1)


root.mainloop()