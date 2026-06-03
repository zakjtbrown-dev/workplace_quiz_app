import tkinter as tk
from tkinter import messagebox
from quiz import Quiz, validate_name
from storage import load_questions, save_result


class QuizApp:
    """Creates the graphical user interface for the quiz application."""

    def __init__(self, root):
        self.root = root
        self.root.title("Workplace Quiz App")
        self.root.geometry("600x400")

        self.questions = load_questions("questions.csv")
        self.quiz = Quiz(self.questions)
        self.current_question = 0
        self.name = tk.StringVar()
        self.selected_answer = tk.StringVar()

        self.start_screen()

    def clear_screen(self):
        """Removes all widgets from the screen."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def start_screen(self):
        """Displays the starting screen."""
        self.clear_screen()

        tk.Label(self.root, text="Workplace Cyber Security Quiz", font=("Arial", 18)).pack(pady=20)
        tk.Label(self.root, text="Enter your name:").pack()

        tk.Entry(self.root, textvariable=self.name).pack(pady=10)
        tk.Button(self.root, text="Start Quiz", command=self.start_quiz).pack(pady=20)

    def start_quiz(self):
        """Starts the quiz after validating the user's name."""
        if not validate_name(self.name.get()):
            messagebox.showerror("Input Error", "Please enter your name.")
            return

        if len(self.questions) == 0:
            messagebox.showerror("File Error", "No questions could be loaded.")
            return

        self.show_question()

    def show_question(self):
        """Displays the current quiz question and answer options."""
        self.clear_screen()
        self.selected_answer.set("")

        question = self.questions[self.current_question]

        tk.Label(
            self.root,
            text=f"Question {self.current_question + 1} of {len(self.questions)}",
            font=("Arial", 14)
        ).pack(pady=10)

        tk.Label(
            self.root,
            text=question.question,
            wraplength=500,
            font=("Arial", 12)
        ).pack(pady=10)

        for key, value in question.options.items():
            tk.Radiobutton(
                self.root,
                text=f"{key}: {value}",
                variable=self.selected_answer,
                value=key
            ).pack(anchor="w", padx=80)

        tk.Button(self.root, text="Next", command=self.next_question).pack(pady=20)

    def next_question(self):
        """Stores the selected answer and moves to the next question."""
        if self.selected_answer.get() == "":
            messagebox.showerror("Input Error", "Please select an answer.")
            return

        self.quiz.add_answer(self.selected_answer.get())

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        """Displays and saves the user's final result."""
        self.clear_screen()

        score = self.quiz.calculate_score()
        total = len(self.questions)

        save_result("results.csv", self.name.get(), score, total)

        tk.Label(self.root, text="Quiz Complete", font=("Arial", 18)).pack(pady=20)
        tk.Label(self.root, text=f"{self.name.get()}, you scored {score} out of {total}.").pack(pady=10)

        tk.Button(self.root, text="Exit", command=self.root.destroy).pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()