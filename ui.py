from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300)
        self.q_text = self.canvas.create_text(150, 125,
                                              text="Question Text Goes here!",
                                              fill=THEME_COLOR,
                                              width=280,
                                              font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed, bd=0)
        self.false_button.grid(column=1, row=2)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed, bd=0)
        self.true_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.q_text, text=self.quiz.next_question())
        else:
            messagebox.showinfo(title="Well Done!",
                                message="You've completed the quiz. "
                                        f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.window.destroy()

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.score.config(text=f"Score: {self.quiz.score}")
            self.show_right()
        else:
            self.show_wrong()

        self.window.after(1000, self.get_next_question)

    def show_right(self):
        self.canvas.config(bg="green")

    def show_wrong(self):
        self.canvas.config(bg="red")


