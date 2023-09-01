# With Play Button

import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.configure(bg='black')
        self.root.geometry("720x600")

        self.user_score = 0
        self.comp_score = 0

        self.user_choice = tk.StringVar()
        self.result = tk.StringVar()
        self.comp_choice = tk.StringVar()

        title_label = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Helvetica", 20,'bold','underline'), bg='light green',fg = "dark red")
        title_label.pack(pady=20)

        choices_frame = tk.Frame(root, bg='light yellow')
        choices_frame.pack(pady=15)
        
        tk.Label(choices_frame, text="Choose", font=("Helvetica", 16,"bold","underline"), bg='white').grid(row=0, columnspan=3)
        tk.Radiobutton(choices_frame, text="ROCK", font=("Helvetica", 12,"bold"), variable=self.user_choice, value="rock", bg='yellow', indicatoron=0).grid(row=1, column=0)
        tk.Radiobutton(choices_frame, text="PAPER",font=("Helvetica", 12,"bold"), variable=self.user_choice, value="paper", bg='Yellow', indicatoron=0).grid(row=1, column=1)
        tk.Radiobutton(choices_frame, text="SCISSORS",font=("Helvetica", 12,"bold"), variable=self.user_choice, value="scissors", bg='yellow', indicatoron=0).grid(row=1, column=2)

        play_button = tk.Button(root, text="Play", command=self.play, font=("Helvetica", 15,"bold"),bg = "pink")
        play_button.pack(pady=10)
        
        
        tk.Label(root, text="      Result      ", font=("Helvetica", 16,"bold"), bg='dark orange').pack(pady=10)
        tk.Label(root, textvariable=self.result, font=("Helvetica", 12,"bold"), bg='dark red',fg = "white").pack(pady = 5)
        
        tk.Label(root, text="      Computer's Choice      ", font=("Helvetica", 14,'bold'), bg='light yellow',fg = "black").pack(pady=10)
        tk.Label(root, textvariable=self.comp_choice, font=("Helvetica", 12,'bold'), bg='dark red',fg = "white").pack(pady=5)
        
        tk.Label(root, text="      User Score      ", font=("Helvetica", 14,'bold'), bg='sky blue').pack(pady = 10)
        self.user_score_label = tk.Label(root, text=str(self.user_score), font=("Helvetica", 12,'bold'), bg='dark red',fg = "white")
        self.user_score_label.pack(pady = 5)

        tk.Label(root, text="      Computer Score      ", font=("Helvetica", 14), bg='light yellow').pack(pady = 10)
        self.comp_score_label = tk.Label(root, text=str(self.comp_score), font=("Helvetica", 12,'bold'), bg='dark red',fg = "white")
        self.comp_score_label.pack(pady=5)

        self.update_scores()

    def play(self):
        choices = ["rock", "paper", "scissors"]
        comp_choice = random.choice(choices)
        user_choice = self.user_choice.get()

        self.comp_choice.set(comp_choice.capitalize())

        if user_choice == comp_choice:
            self.result.set("It's a tie!")
        elif (
            (user_choice == "rock" and comp_choice == "scissors")
            or (user_choice == "scissors" and comp_choice == "paper")
            or (user_choice == "paper" and comp_choice == "rock")
        ):
            self.result.set("You win!")
            self.user_score += 1
        else:
            self.result.set("You lose!")
            self.comp_score += 1

        self.update_scores()

    def update_scores(self):
        self.user_score_label.config(text=str(self.user_score))
        self.comp_score_label.config(text=str(self.comp_score))

root = tk.Tk()
game = RockPaperScissorsGame(root)
root.mainloop()
