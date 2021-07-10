from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import ui
import html

user_interface = ui.UserInterface()

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

user_interface.change_question(html.unescape(quiz.next_question()))


def right():
    try:
        qa = question_bank[quiz.question_number].answer
        if qa == "True":
            user_interface.score += 1
        user_interface.change_question(html.unescape(quiz.next_question()))
    except IndexError:
        user_interface.canvas_question.delete("all")
        user_interface.canvas_question.create_text(300, 300, text="That is all the questions!!",
                                                   font="Times 20 italic bold",
                                                   width=600,
                                                   justify="center")


def wrong():
    try:
        qa = question_bank[quiz.question_number].answer
        if qa == "False":
            user_interface.score += 1
        user_interface.change_question(html.unescape(quiz.next_question()))
    except IndexError:
        user_interface.canvas_question.delete("all")
        user_interface.canvas_question.create_text(300, 300, text="That is all the questions!!",
                                                   font="Times 20 italic bold",
                                                   width=600,
                                                   justify="center")


user_interface.button_true.configure(command=right)
user_interface.button_false.configure(command=wrong)
user_interface.main_loop()
