import tkinter as tk

#Creating the window
root = tk.Tk()
root.title("Arithmetic and Geometric Series Calculator")
root.geometry("600x600")

current_mode = "Arithmetic"
current_colour_index = 0
current_font_index = 0
current_lang_index = 0
fonts = ["Helvetica", "Times New Roman", "Courier"]
font_sizes = [10, 12, 14]
colours = ["black", "white", "gray", "blue"]
languages = ["en", "zh-CN", "fr", "de", "ar", "hi"]

#Making these functions global
first_term = 0
common_difference = 0
number_of_terms = 0
common_ratio = 0

#Creating the clear function
def clear_values():
    entry_first_term.delete(0, tk.END)
    entry_common_difference.delete(0, tk.END)
    entry_number_of_terms.delete(0, tk.END)
    entry_common_ratio.delete(0, tk.END)

#Creating the frames and radiobuttons
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

result_frame = tk.Frame(root)
result_frame.pack(pady=10)

result_label = tk.Label(result_frame, text="Result: ")
result_label.pack()

result_text = tk.Text(result_frame, height=5, width=30)
result_text.pack()

def togglemode():
    global current_mode
    mode_index = int(mode_radio_var.get())
    if mode_index ==0:
        current_mode = "Arithmetic"
    else:
        current_mode = "Geometric"

mode_radio_frame = tk.Frame(root)
mode_radio_frame.pack(pady=5)

mode_radio_var = tk.StringVar()
mode_labels = ["Arithmetic", "Geometric"]
for i, mode in enumerate(mode_labels):
    radiobutton = tk.Radiobutton(mode_radio_frame, text=mode, variable=mode_radio_var, value=i, command= togglemode)
    radiobutton.pack(side="left")


#Defining the sum function
def calculate_sum():
    #Defining each variable
    result_text.delete("1.0", tk.END)

    first_term = float(entry_first_term.get())
    common_difference = float(entry_common_difference.get())
    number_of_terms = int(entry_number_of_terms.get())
    common_ratio = str(entry_common_ratio.get)

    if current_mode == "Arithmetic":
        answer = (int(number_of_terms / 2) * (2 * first_term + ((number_of_terms) - 1) * common_difference))

    else:
        answer = (int(common_ratio ** number_of_terms - 1))

    result_text.insert(tk.END, int(answer))

#Switching colours
def togglecolour():
    current_colour_index = (current_colour_index + 1) % len(colours)
    colour = colours[current_colour_index]
    root.config(bg=colour)
    updateentrycolours(colour)

#Changing the font type
def togglefont():
    current_font_index = (current_font_index + 1) % len(fonts)
    updatefont()

def updatefont():
    selected_font = (fonts[current_font_index], font_sizes[current_font_index])
    root.option_add("Font", selected_font)
    updateentrywidgets()

#Changing the language
def togglelanguage():
    global current_lang_index
    current_lang_index = (current_lang_index + 1) % len(languages)
    updatelanguage()

def updatelanguage():
    lang_type = languages[current_lang_index]
    translator = Translator()
    label_first_term.config(text=translator.translate("First Term: ", dest=lang_type).text)
    label_common_difference.config(text=translator.translate("Common Difference:", dest=lang_type).text)
    label_number_of_terms.config(text=translator.translate("Number of Terms:", dest=lang_type).text)
    label_common_ratio.config(text=translator.translate("Common Ratio:", dest=lang_type).text)

    if lang_type == "en":
        current_lang_index = 0

def labelfont():
    return (fonts[current_font_index], font_sizes[current_font_index])


#Creating functionality widgets
colour_button = tk.Button(root, text="Switch Colours", command=togglecolour)
colour_button.pack(pady=5, padx=10)

font_button = tk.Button(root, text="Switch Font", command=togglefont)
font_button.pack(pady=5, padx=10)

#language_button = tk.Button(root, text="Switch Language", command=togglelanguage)
#language_button.pack(pady=5, padx=10)


#Creating the Labels for variables
label_first_term = tk.Label(entry_frame, text="First Term:")
label_first_term.pack()
label_first_term.config(font=(fonts[current_font_index], font_sizes[current_font_index]))
entry_first_term = tk.Entry(entry_frame)
entry_first_term.pack()

label_number_of_terms = tk.Label(entry_frame, text="Number of Terms: ")
label_number_of_terms.config(font=(fonts[current_font_index], font_sizes[current_font_index]))
label_number_of_terms.pack()
entry_number_of_terms = tk.Entry(entry_frame)
entry_number_of_terms.pack()

label_common_difference = tk.Label(entry_frame, text="Common Difference: ")
label_common_difference.config(font=(fonts[current_font_index], font_sizes[current_font_index]))
label_common_difference.pack()
entry_common_difference = tk.Entry(entry_frame)
entry_common_difference.pack()

label_common_ratio = tk.Label(entry_frame, text="Common Ratio: ")
label_common_ratio.config(font=(fonts[current_font_index], font_sizes[current_font_index]))
label_common_ratio.pack()
entry_common_ratio = tk.Entry(entry_frame)
entry_common_ratio.pack()

label_first_term.config(font=labelfont())
label_common_difference.config(font=labelfont())
label_number_of_terms.config(font=labelfont())

def updateentrywidgets():

    if current_mode == "Arithmetic":
        label_first_term(state=tk.ACTIVE)
        label_number_of_terms(state=tk.ACTIVE)
        label_common_difference(state=tk.ACTIVE)
        label_common_ratio(state=tk.DISABLED)

    else:
        label_first_term(state=tk.ACTIVE)
        label_number_of_terms(state=tk.ACTIVE)
        label_common_difference(state=tk.DISABLED)
        label_common_ratio(state=tk.ACTIVE)

def updateentrycolours(root, colour):
    for entry_widget in [entry_first_term, entry_common_difference, entry_number_of_terms]:
        entry_widget.config(bg=colour, fg="grey")

#Creating the calculate and clear buttons
calculate_button = tk.Button(result_frame, text="Calculate", command=calculate_sum)
calculate_button.pack(pady=10)

clear_button = tk.Button(entry_frame, text="Clear", command=clear_values)
clear_button.pack(pady=5)

root.mainloop()