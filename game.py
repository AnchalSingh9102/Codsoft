import tkinter as tk
import random

quiz_questions = [
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Mercury", "B) Venus", "C) Jupiter", "D) Mars"],
        "correct_answer": "C"
    },
    {
        "question": "Which famous scientist developed the theory of relativity?",
        "options": ["A) Isaac Newton", "B) Galileo Galilei", "C) Albert Einstein", "D) Nikola Tesla"],
        "correct_answer": "C"
    },
    {
        "question": "Which element is represented by the chemical symbol 'Fe'?",
        "options": ["A) Iron", "B) Gold", "C) Silver", "D) Copper"],
        "correct_answer": "A"
    },
    {
        "question": "What is the capital city of Japan?",
        "options": ["A) Beijing", "B) Seoul", "C) Tokyo", "D) Bangkok"],
        "correct_answer": "C"
    },
    {
        "question": "Which famous painting features a woman with a mysterious smile?",
        "options": ["A) The Persistence of Memory", "B) The Starry Night", "C) Mona Lisa", "D) The Scream"],
        "correct_answer": "C"
    }
]

class QuizGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("650x450")
        self.root.configure(bg="light yellow")

        self.score = 0
        self.current_question = 0

        self.question_label = tk.Label(self.root, text="", font=("Arial", 16, "bold"), wraplength=600, bg="light yellow", fg="black")
        self.question_label.pack(pady=20)

        self.option_var = tk.StringVar()
        self.option_var.set("-1")
        self.option_frame = tk.Frame(self.root, bg="light yellow")
        self.option_frame.pack(padx=20, pady=10, anchor="w")
        self.option_buttons = []
        for i in range(4):
            option_button = tk.Radiobutton(self.option_frame, text="", font=("Arial", 12),bg = "light yellow", fg="black", selectcolor="orange",
                                           variable=self.option_var, value=str(i), command=self.evaluate_answer)
            option_button.pack(anchor="w")
            self.option_buttons.append(option_button)

        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 14, "bold"), bg="white", fg="black")
        self.feedback_label.pack()

        self.button_frame = tk.Frame(self.root, bg="light yellow")
        self.button_frame.pack(pady=10, fill="x")
        
        self.quit_button = tk.Button(self.button_frame, text="Quit", font=("Arial", 14),bg = "light green", command=root.quit)
        self.quit_button.pack(side="left", padx=20)

        self.next_button = tk.Button(self.button_frame, text="Next Question", font=("Arial", 14),bg = "light green" ,command=self.load_next_question)
        self.next_button.pack(side="right", padx=20)

        self.load_next_question()

    def load_next_question(self):
        if self.current_question < len(quiz_questions):
            question_info = quiz_questions[self.current_question]
            self.question_label.config(text=question_info["question"])

            options = question_info["options"]
            for i in range(4):
                self.option_buttons[i].config(text=options[i], state=tk.NORMAL)

            self.option_var.set("")
            self.feedback_label.config(text="")
        else:
            self.question_label.config(text="Quiz Completed!", fg="black")
            for button in self.option_buttons:
                button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.DISABLED)
            self.show_result()

    def evaluate_answer(self):
        selected_option_index = self.option_var.get()
        if selected_option_index != "-1":
            question_info = quiz_questions[self.current_question]
            selected_option = chr(ord("A") + int(selected_option_index))

            if selected_option == question_info["correct_answer"]:
                self.score += 1
                self.feedback_label.config(text="Correct!", fg="green")
            else:
                self.feedback_label.config(text="Incorrect. The correct answer was: " + question_info["correct_answer"], fg="red")

            for button in self.option_buttons:
                button.config(state=tk.DISABLED)

            self.current_question += 1
            self.next_button.config(state=tk.NORMAL)

    def show_result(self):
        result = f"You scored {self.score} out of {len(quiz_questions)}"
        self.feedback_label.config(text=result, fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGameApp(root)
    root.mainloop()
