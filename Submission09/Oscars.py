# Oscars.py
# Submission 09
# Oscar Best Picture Award with a GUI

""" Both the Oscars.py and Oscars.txt
programs run according to specifications.
I've tried every which way to Sunday but
can't format the enter year or show year
buttons correctly. That should be the only
issue."""

import tkinter
import tkinter.messagebox
from tkinter import E
from tkinter import W
from tkinter import StringVar


class Oscars:
    def __init__(self):
        """The class "constructor" for the program."""

        self.main_window = tkinter.Tk()
        self.main_window.title('Academy Awards')

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.year_text = tkinter.Label(self.top_frame, text='Enter Year (1928'
                                                            '-2016): ')
        self.year_text.grid()
        self.year_entry = tkinter.Entry(self.top_frame, width=4)
        self.year_entry.grid(row=0, column=6)
        self.show_button = tkinter.Button(self.mid_frame,
                                          text="Show That Year's Best Picture",
                                          command=self.__showInfo)
        self.show_button.grid()
        self.film_title_label = tkinter.Label(self.bottom_frame, text='  Film '
                                                                      'Title:'
                                              '').grid(row=2, column=0,
                                                       sticky=W, columnspan=2)
        self.film_genre_label = tkinter.Label(self.bottom_frame, text='Film '
                                                                      'Genre:'
                                              '').grid(row=3, column=0,
                                                       sticky=W, columnspan=2)
        self.title_cont = StringVar()
        self.film_title_entry_box = tkinter.Entry(self.bottom_frame,
                                                  state="readonly", width=30,
                                                  textvariable=self.title_cont)
        self.film_title_entry_box.grid(row=2, column=2, columnspan=2, pady=3,
                                       padx=5)
        self.genre_cont = StringVar()
        self.film_genre_entry_box = tkinter.Entry(self.bottom_frame,
                                                  state='readonly', width=30,
                                                  textvariable=self.genre_cont)
        self.film_genre_entry_box.grid(row=3, column=2, columnspan=2, pady=5,
                                       padx=5)

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def __isInteger(self, p):
        """ This function checks if the expression entered by the user is a
        valid integer.
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

    def __showInfo(self):
        """ This function checks to see that the user's inputted year is valid
        i.e. is an integer value between 1928 and 2016 as well as checking that
        it's not a string. If the user's input is invalid an appropriate error
        message is displayed. And if the user's input is valid than the program
        reads in the text file, finds the desired year and display's the title
        and the genre of the winning film.
         """
        if not self.__isInteger(self.year_entry.get()):
            tkinter.messagebox.showinfo('Error', 'Input value for year cannot '
                                                 'be converted to an integer'
                                                 ' year.')
        elif int(self.year_entry.get()) < 1928:
            tkinter.messagebox.showinfo('Error', 'Requested year is out of '
                                                 'range.\n It must lie in the '
                                                 'interval 1928 to 2016.')
        elif int(self.year_entry.get()) > 2016:
            tkinter.messagebox.showinfo('Error', 'Requested year is out of '
                                                 'range.\n It must lie in the '
                                                 'interval 1928 to 2016.')
        else:
            f = open('Oscars.txt')
            year = 1928
            user_year = int(self.year_entry.get())
            line = f.readline()
            while user_year > year:
                year += 1
                line = f.readline()
            info_list = line.split(',')
            self.title_cont.set(info_list[0])
            self.genre_cont.set(info_list[1])
            f.close()

oscars = Oscars()
