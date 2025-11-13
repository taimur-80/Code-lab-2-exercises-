import tkinter as tk
from tkinter import messagebox
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Arithmetic Quiz")
        self.difficulty = None
        self.score = 0
        self.question_num = 0
        self.current_problem = ""
        self.correct_answer = 0
        self.attempt = 1
        self.displayMenu()

    def displayMenu(self):
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(pady=20)
        tk.Label(self.menu_frame, text="DIFFICULTY LEVEL", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.menu_frame, text="1. Easy", command=lambda: self.setDifficulty('easy')).pack(pady=5)
        tk.Button(self.menu_frame, text="2. Moderate", command=lambda: self.setDifficulty('moderate')).pack(pady=5)
        tk.Button(self.menu_frame, text="3. Advanced", command=lambda: self.setDifficulty('advanced')).pack(pady=5)

    def setDifficulty(self, diff):
        self.difficulty = diff
        self.menu_frame.destroy()
        self.startQuiz()

    def startQuiz(self):
        self.score = 0
        self.question_num = 0
        self.nextQuestion()

    def nextQuestion(self):
        if self.question_num < 10:
            self.question_num += 1
            op = self.decideOperation()
            num1, num2 = self.randomInt(op)
            self.current_problem = f"{num1} {op} {num2} ="
            self.correct_answer = num1 + num2 if op == '+' else num1 - num2
            self.attempt = 1
            self.displayProblem()
        else:
            self.displayResults()

    def displayProblem(self):
        if hasattr(self, 'problem_frame'):
            self.problem_frame.destroy()
        self.problem_frame = tk.Frame(self.root)
        self.problem_frame.pack(pady=20)
        tk.Label(self.problem_frame, text=f"Question {self.question_num}: {self.current_problem}", font=("Arial", 14)).pack(pady=10)
        self.entry = tk.Entry(self.problem_frame, font=("Arial", 14))
        self.entry.pack(pady=5)
        self.entry.focus()
        tk.Button(self.problem_frame, text="Submit", command=self.submitAnswer).pack(pady=10)

    def submitAnswer(self):
        try:
            answer = int(self.entry.get())
            if self.isCorrect(answer):
                if self.attempt == 1:
                    self.score += 10
                else:
                    self.score += 5
                self.nextQuestion()
            else:
                if self.attempt == 1:
                    self.attempt = 2
                    self.entry.delete(0, tk.END)
                    self.entry.focus()
                else:
                    self.nextQuestion()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")

    def isCorrect(self, answer):
        if answer == self.correct_answer:
            messagebox.showinfo("Correct", "Good job!")
            return True
        else:
            if self.attempt == 1:
                messagebox.showerror("Incorrect", "Try again.")
            else:
                messagebox.showerror("Incorrect", "Wrong, moving to next question.")
            return False

    def displayResults(self):
        rank = self.getRank()
        messagebox.showinfo("Results", f"Your score: {self.score}/100\nRank: {rank}")
        response = messagebox.askyesno("Play Again?", "Do you want to play again?")
        if response:
            self.displayMenu()
        else:
            self.root.quit()

    def getRank(self):
        if self.score > 90:
            return "A+"
        elif self.score > 80:
            return "A"
        elif self.score > 70:
            return "B"
        elif self.score > 60:
            return "C"
        elif self.score > 50:
            return "D"
        else:
            return "F"

    def randomInt(self, op):
        if self.difficulty == 'easy':
            min_val, max_val = 0, 9
        elif self.difficulty == 'moderate':
            min_val, max_val = 10, 99
        else:
            min_val, max_val = 1000, 9999
        num1 = random.randint(min_val, max_val)
        num2 = random.randint(min_val, max_val)
        if op == '-' and num1 < num2:
            num1, num2 = num2, num1
        return num1, num2

    def decideOperation(self):
        return random.choice(['+', '-'])

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
