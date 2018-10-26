# time_converter_gui.py
# Submission 07
# Converting Time with a GUI

""" The time_converter_gui.py program runs according to specifications. """

import tkinter
import tkinter.messagebox


def convert():
    """ This function converts the time entered by the user in seconds
        to the hh:mm:ss format. """
    sec_input = int(seconds_entry.get())
    seconds = sec_input % 60
    mins = sec_input // 60
    minutes = mins % 60
    hours = mins // 60
    final_form = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    one_case = oneSecondCase(sec_input)
    tkinter.messagebox.showinfo('Conversion Result', '{} {} in hh:mm:ss format'
                                " is {}".format(sec_input,
                                                one_case,
                                                final_form))


def oneSecondCase(sec_input):
    """ This function deals with the case where the time entered by the user
        was 1 second and requires the output sentence to read '1 second'...
        instead of '1 seconds'...
        Parameters
        ----------
        sec_input: int
            This value is the number of seconds inputted by the user.

        Returns
        -------
        string
            The returned value is a string that says 'second' should the
            if statement prove true or it returns the string 'seconds'
            which occurs in every other case.
        """
    if sec_input == 1:
        return "second"
    else:
        return "seconds"


def information():
    """ This function reports the programmer's information as well as the
        program's information to the user."""
    tkinter.messagebox.showinfo('Program Information',
                                """
    McGowan:Shawnna:A00393797:csc227025
    Submission 07
    Converting Time with a GUI

    This program allows the user to convert
    a time value given as a total number of
    seconds to the corresponding equivalent
    hours, minutes and seconds.""")

main_window = tkinter.Tk()

top_frame = tkinter.Frame()
bottom_frame = tkinter.Frame()

title_label = tkinter.Label(top_frame, text='Time Converter for Seconds to '
                                            'hh:mm:ss')
seconds_label = tkinter.Label(top_frame, text=' Enter a number of seconds: ')
seconds_entry = tkinter.Entry(top_frame, width=10)
title_label.pack(side='top')
seconds_label.pack(side='left')
seconds_entry.pack(side='left')

info_button = tkinter.Button(bottom_frame,
                             text="Get Information",
                             command=information)
convert_button = tkinter.Button(bottom_frame,
                                text='Convert Seconds',
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
