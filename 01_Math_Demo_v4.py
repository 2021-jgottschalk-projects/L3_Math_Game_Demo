# Math game, GTT, 07/2016
# v1: Create Basic Selection Panel (minus, division and mix of minus / division )
# v2 Link main panel to question dialogue (recycle addition game code)
# v3: Ask subtraction / division questions (and sorts negatives)
# v4: Don't allow text / invalid input in main panel

from tkinter import *
import random
import operator


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

        low = StringVar()
        low.set("1")
        self.low_num_entry = Entry(self.to_from_frame, width="5",
                                   textvariable=low,)
        self.low_num_entry.grid(row=0, column=0, padx=10)

        self.num_entry_and_label = Label(self.to_from_frame,
                                         text="and",
                                         padx=10)
        self.num_entry_and_label.grid(row=0, column=1)

        high = StringVar()
        high.set("10")
        self.high_num_entry = Entry(self.to_from_frame, width="5",
                                    textvariable=high)
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

        how_many = StringVar()
        how_many.set("10")
        self.how_many = Entry(self.num_q_frame, width=5,
                              textvariable=how_many)
        self.how_many.grid(row=0, column=1, padx=10, pady=10)

        # Buttons!!
        self.minus_button = Button(self.math_frame, text="Subtract ( - )",
                                   font="arial 14 bold", width="15",
                                   command=lambda: self.to_quiz(1))
        self.minus_button.grid(row=5)

        self.divide_button = Button(self.math_frame, text="Divide ( / )",
                                    font="arial 14 bold", width="15",
                                    command=lambda: self.to_quiz(2))
        self.divide_button.grid(row=6)

        self.mixed_button = Button(self.math_frame, text="Mixture",
                                   font="arial 14 bold", width="15",
                                   command=lambda: self.to_quiz(3))
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

    def to_quiz(self, operation):
        low = self.low_num_entry.get()
        high = self.high_num_entry.get()
        neg = self.neg.get()
        how_many = self.how_many.get()

        ok = "yes"

        # *** Check that low, high and how many are integers ***
        try:
            int(low)
            self.low_num_entry.config(bg="white")
        except ValueError:
            ok = "no"
            self.low_num_entry.config(bg="pink")
        try:
            int(high)
            self.high_num_entry.config(bg="white")
        except ValueError:
            ok = "no"
            self.high_num_entry.config(bg="pink")
        try:
            int(how_many)
            if int(how_many) > 0:
                self.how_many.config(bg="white")
            else:
                self.how_many.config(bg="pink")
                ok = "no"
        except ValueError:
            ok = "no"
            self.how_many.config(bg="pink")

        if ok == "yes" and int(low) >= int(high):
            self.low_num_entry.config(bg="pink")
            ok = "no"

        if ok == "yes":
            Quiz(low, high, neg, how_many, operation)
            self.math_frame.destroy()

    def help(self):
            get_help = Help()
            get_help.help_text.configure(text="This is the text that goes in the help")

    def quit(self):
        root.destroy()

class Quiz:
    def __init__(self, low, high, neg, how_many, operation):

        # **** Colour Variables ****
        backcol = "light blue"

        # *** Intialise Variables ****
        self.var_num_right = IntVar()
        self.var_asked = IntVar()

        low = int(low)
        high = int(high)
        high += 1
        how_many = int(how_many)
        neg = int(neg)

        # *** GUI Set up ****
        self.quiz_box = Toplevel()
        self.game_frame = Frame(self.quiz_box, padx=20, pady=20, bg=backcol)
        self.game_frame.grid()

        # **** First Row ****
        self.question_frame = Frame(self.game_frame, bg=backcol)
        self.question_frame.grid(row=0)

        self.question_label = Label(self.question_frame, text="? + ? =",
                                    font="Arial 24 bold",
                                    padx=10, pady=10, bg=backcol)
        self.question_label.grid(row=0, column=0)

        user_ans = StringVar()
        self.ansbox_entry = Entry(self.question_frame, width=4,
                                  justify=CENTER,
                                  textvariable=user_ans,
                                  font="Arial 24 bold")
        self.ansbox_entry.bind('<Return>', lambda _: self.check_ans(how_many))
        self.ansbox_entry.grid(row=0, column=1)

        self.next_btn = Button(self.question_frame, text="Next",
                               fg="white", bg="green",
                               state=DISABLED,
                               command=lambda: self.ask_question(low, high, operation, neg),
                               font="Arial 16 bold", padx=5)
        self.next_btn.bind('<Return>', lambda _: self.ask_question(low, high, operation, neg))
        self.next_btn.grid(row=0, column=2, padx=10)

        # Results label and quit button go here
        self.results_label = Label(self.game_frame,
                                   text="",
                                   font="Arial 14", bg=backcol)
        self.results_label.grid(row=1, column=0)

        self.quit_btn = Button(self.game_frame, text="Quit",
                               bg="red3", fg="white",
                               font="Arial 14 bold", width=10,
                               command=self.close_quiz)
        self.quit_btn.bind('<Return>', lambda _:self.close_quiz())
        self.quit_btn.grid(row=2, column=0, pady=10)

        # *** Asks first question ****
        self.ansbox_entry.focus_set()
        self.ask_question(low, high, operation, neg)

    def ask_question(self, low, high, operation, neg):

        self.ansbox_entry.config(bg="white", state=NORMAL)
        self.ansbox_entry.delete(0, END)
        self.ansbox_entry.focus()
        self.next_btn.config(state=DISABLED)

        # generate random numbers for question
        a = random.randrange(low, high)
        b = random.randrange(low, high)

        if neg == 0 and a < b:
            a, b = b, a

        ops = {"-": operator.sub,
               "/": operator.truediv}

        if operation == 1:
            op_char = "-"
        elif operation == 2:
            op_char = "/"
        else:
            op_list = ["-", "/"]
            op_char = random.choice(op_list)

        op_func = ops[op_char]

        # Set up divsion so answer is always an integer
        if op_char == "/":
            times_ans = a * b
            a = times_ans

        self.right_ans = op_func(a, b)

        question = ("{} {} {} = ".format(a, op_char, b))
        self.question_label.configure(text=question)

    def check_ans(self, how_many):
        answer = self.ansbox_entry.get()

        try:
            answer = int(answer)
            asked = self.var_asked.get()
            asked += 1
            self.var_asked.set(asked)

            num_right = self.var_num_right.get()
            if answer == self.right_ans:
                self.ansbox_entry.config(disabledbackground="pale green",
                                         state=DISABLED)
                num_right += 1
            else:
                self.ansbox_entry.config(disabledbackground="light pink",
                                         state=DISABLED)

            self.var_num_right.set(num_right)
            current_score = "{} / {}".format(num_right, asked)
            self.results_label.config(text=current_score)
            self.next_btn.config(state=NORMAL)
            self.next_btn.focus_set()

            if asked < how_many:
                self.next_btn.config(state="normal",
                                     bg="green", foreground="white")
                self.next_btn.focus_set()
            else:
                self.next_btn.config(state="disabled", bg="orange",
                                     fg="white", text="Game Over")
                self.quit_btn.config(bg="green", text="New Game",
                                     font="Arial 14 bold", fg="white")
                self.quit_btn.focus_set()


        except ValueError:
            self.ansbox_entry.config(bg="orange")
            self.results_label.config(text="Please enter an integer")

    def close_quiz(self):
        MathGame(root)
        self.quiz_box.destroy()



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
