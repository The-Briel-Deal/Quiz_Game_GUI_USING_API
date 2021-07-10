import tkinter
from PIL import ImageTk, Image

THEME_COLOR = "#EFDD8D"


class UserInterface:
    def __init__(self):
        # -----create window----- #
        self.window = tkinter.Tk()
        self.window.configure(bg=THEME_COLOR)

        # -----canvas----- #
        self.canvas_question = tkinter.Canvas(width=600, height=600, bg=THEME_COLOR, highlightthickness=0)

        # -----true button----- #
        true_button_img = Image.open("images/true.png")  # reference path
        true_button_img = true_button_img.resize((100, 100), Image.ANTIALIAS)  # resizing and anti-aliasing
        self.true_image = ImageTk.PhotoImage(true_button_img)  # turning into tkinter photo class
        self.button_true = tkinter.Button(image=self.true_image)  # putting button image in button

        # -----false button----- #
        false_button_img = Image.open("images/false.png")  # reference path
        false_button_img = false_button_img.resize((100, 100), Image.ANTIALIAS)  # resizing and anti-aliasing
        self.false_image = ImageTk.PhotoImage(false_button_img)  # turning into tkinter photo class
        self.button_false = tkinter.Button(image=self.false_image)  # putting button image in button

        # -----place objects----- #
        self.canvas_question.grid(column=0, row=0, columnspan=2)
        self.button_true.grid(column=0, row=1)
        self.button_false.grid(column=1, row=1)

        self.score = 0

    def change_question(self, question):
        self.canvas_question.delete('all')
        self.canvas_question.create_text(300, 300,
                                         text=question,
                                         font="Times 20 italic bold",
                                         width=600,
                                         justify="center")
        self.canvas_question.create_text(300, 100,
                                         text=f"Your score is: {self.score}",
                                         font="Times 20 italic bold",
                                         width=600,
                                         justify="center")

    def main_loop(self):
        tkinter.mainloop()

