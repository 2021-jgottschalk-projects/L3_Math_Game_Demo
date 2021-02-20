# Math game, GTT, 07/2016
# v1: Create Basic Selection Panel (minus, division and mix of minus / division )
# Link main panel to question dialogue (recycle addition game code)

# To Do
# Get negatives sorted (default is not to allow).
# Don't allow text / invalid input in main panel
# Add 'exit' and 'help' on main console

from tkinter import *
import random


class MathGame:
    def __init__(self, parent):

        # Main Panel GUI
        self.math_frame = Frame(parent)
        self.math_frame.grid()

        self.gameheading_label = Label(self.math_frame,
                                       text="Maths Game",
                                       font="Arial 16 bold",
                                       padx=10, pady=10)
        self.gameheading_label.grid(row=0)

        self.numq_label = Label(self.math_frame,
                                text="Number in questions should be "
                                     "between...",
                                padx=10, pady=10)
        self.numq_label.grid(row=1)

        # Frame for 3 column number input....
        self.to_from_frame = Frame(self.math_frame, padx=10, pady=10)
        self.to_from_frame.grid(row=2)

        self.low_num_entry = Entry(self.to_from_frame, width="5")
        self.low_num_entry.grid(row=0, column=0, padx=10)

        self.num_entry_and_label = Label(self.to_from_frame,
                                         text="and",
                                         padx=10)
        self.num_entry_and_label.grid(row=0, column=1)

        self.high_num_entry = Entry(self.to_from_frame, width="5")
        self.high_num_entry.grid(row=0, column=2, padx=10)

        # Checkbox - no negatives ==> 0 <default>
        self.neg = IntVar()
        self.negcheck = Checkbutton(self.math_frame,
                                    variable=self.neg,
                                    text="Allow negative answers?")
        self.negcheck.grid(row=3, padx=10, pady=10)

        # Number of questions frame...
        self.num_q_frame = Frame(self.math_frame, padx=10, pady=10)
        self.num_q_frame.grid(row=4)

        self.num_qs_label = Label(self.num_q_frame,
                                  text="# of questions")
        self.num_qs_label.grid(row=0, column=0)

        self.how_many = Entry(self.num_q_frame, width=5)
        self.how_many.grid(row=0, column=1, padx=10, pady=10)

        # Buttons!!
        self.minus_button = Button(self.math_frame, text="Subtract ( - )",
                                   font="arial 14 bold", width="15")
        self.minus_button.grid(row=5)

        self.divide_button = Button(self.math_frame, text="Divide ( / )",
                                    font="arial 14 bold", width="15")
        self.divide_button.grid(row=6)

        self.mixed_button = Button(self.math_frame, text="Mixture",
                                   font="arial 14 bold", width="15")
        self.mixed_button.grid(row=7)

        # **** Help / Exit Buttons ****

        self.hq_frame = Frame(self.math_frame)
        self.hq_frame.grid(row=8, padx=10, pady=10)

        self.help_btn = Button(self.hq_frame, text="Help",
                               width=5, font="Arial 12 bold",
                               padx=10, pady=10, bg="orange",
                               command=self.help)
        self.help_btn.grid(row=0, column=0)

        self.quit_btn = Button(self.hq_frame, text="Quit",
                               width=5, font="Arial 12 bold",
                               padx=10, pady=10, bg="maroon",
                               foreground="white", command=self.quit)
        self.quit_btn.grid(row=0, column=1)

    def help(self):
            get_help = Help()
            get_help.help_text.configure(text="help text goes here")

    def quit(self):
        root.destroy()


class Help:
    def __init__(self):

        background = "light blue"

        self.help_box = Toplevel()

        self.help_frame = Frame(self.help_box, width=300,
                                height=200, bg=background)
        self.help_frame.grid()

        how_heading = Label(self.help_frame,
                            text="Help / Instructions",
                            font="arial 10 bold", bg=background)
        how_heading.grid(row=0)

        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40,
                               bg=background, wrap=250)
        self.help_text.grid(column=0, row=1)

        dismiss_btn = Button(self.help_frame, text="Dismiss",
                             width=10, bg="orange",
                             font="arial 10 bold",
                             command=self.close_help)
        dismiss_btn.grid(row=2, pady=10)

    def close_help(self):
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Basic Facts Game")
    something = MathGame(root)
    root.mainloop()
