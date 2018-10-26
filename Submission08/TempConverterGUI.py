# TempConverterGUI.py
# Submission 08
# Converting Temperature with a GUI

""" The TempConverterGUI.py program runs according to specifications. """

import tkinter
import tkinter.messagebox
from tkinter import *


def information():
    """ This function reports the programmer's information as well as the
        program's information to the user."""
    tkinter.messagebox.showinfo('Program Information',
                                """
    McGowan:Shawnna:A00393797:csc227025
    Submission 08
    Converting Temperature with a GUI

    This program allows the user to convert
    a temperature value given in Celsius
    to Fahrenheit or vice versa.""")


def isNumber(p):
    """ This function checks if the expression entered by the user is a valid
    number.
            Parameters
        ----------
        p: string
            This is the expression first entered by the user.

        Returns
        -------
        The function returns either True or False depending on weather p can
        be converted to a valid number or not. Returns True if p can be casted
        to another value or False if p cannot be casted to another value. """
    try:
        float(p)
        return True
    except ValueError:
        return False


def convert():
    """ This function checks to see that the user has entered a valid number
    and outputs an appropriate error message if that is not the case. This
    function also checks which radio button was chosen by the user and
    computes the correct temperature conversion. """
    if temp_entry.get() == "":
        tkinter.messagebox.showinfo('Error Message',
                                    'A number was not entered to convert.')
    elif not isNumber(temp_entry.get()):
        tkinter.messagebox.showinfo('Error Message',
                                    'An invalid number was entered.'
                                    ' Please enter either a positive'
                                    ' or negative integer or decimal value.')
    elif radio_var.get() == 1:
        temp = float(temp_entry.get())
        f_value = (temp * (9 / 5)) + 32
        tkinter.messagebox.showinfo('Celsius to Fahrenheit Conversion',
                                    "{:2.2f} degrees Celsius is equivalent"
                                    " to {:2.2f} degrees "
                                    "Fahrenheit.".format(temp, f_value))
    elif radio_var.get() == 2:
        temp = float(temp_entry.get())
        c_value = (temp - 32) * (5/9)
        tkinter.messagebox.showinfo('Fahrenheit to Celsius Conversion',
                                    "{:2.2f} degrees Fahrenheit is equivalent"
                                    " to {:2.2f} degrees "
                                    "Celsius.".format(temp, c_value))

main_window = tkinter.Tk()
main_window.title('Temperature Converter')

top_frame = tkinter.Frame()
bottom_frame = tkinter.Frame()

radio_var = tkinter.IntVar()
radio_var.set(1)

temp_label = tkinter.Label(top_frame, text=' Enter a temperature to convert: ')
temp_entry = tkinter.Entry(top_frame, width=10)
cel_to_fah = tkinter.Radiobutton(top_frame, text='Celsius to Fahrenheit',
                                 variable=radio_var,
                                 value=1)
fah_to_cel = tkinter.Radiobutton(top_frame, text='Fahrenheit to Celsius',
                                 variable=radio_var,
                                 value=2)

temp_label.pack(side='top')
temp_entry.pack(side='top')
cel_to_fah.pack()
fah_to_cel.pack()

info_button = tkinter.Button(bottom_frame,
                             text="Get Information",
                             command=information)
convert_button = tkinter.Button(bottom_frame,
                                text='Convert Temperature',
                                command=convert)
quit_button = tkinter.Button(bottom_frame,
                             text='Quit',
                             command=main_window.destroy)

info_button.pack(padx=0, side='left')
convert_button.pack(padx=0, side='left')
quit_button.pack(padx=0, side='left')

top_frame.pack()
bottom_frame.pack()

tkinter.mainloop()
