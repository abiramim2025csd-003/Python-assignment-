import tkinter as tk
import random

# Game Settings
WIDTH = 400
HEIGHT = 350

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("NUMBER GUESSING GAME")
        self.root.geometry("400x350")
        self.root.configure(bg="#172554")
        self.root.resizable(False, False)

        tk.Label(
            root,
            text="NUMBER GUESSING GAME",
            font=("Arial Black", 16),
            bg="#172554",
            fg="white"
        ).pack(pady=15)

        tk.Label(
            root,
            text="Guess a number between 1 and 100",
            font=("Arial", 12),
            bg="#172554",
            fg="#FACC15"
        ).pack(pady=5)

        self.entry = tk.Entry(
            root,
            font=("Arial", 16),
            justify="center"
        )
        self.entry.pack(pady=10)

        tk.Button(
            root,
            text="GUESS",
            font=("Arial", 12, "bold"),
            bg="#22C55E",
            command=self.check_guess
        ).pack(pady=5)

        self.message = tk.Label(
            root,
            text="Enter your guess!",
            font=("Arial", 12, "bold"),
            bg="#172554",
            fg="white"
        )
        self.message.pack(pady=10)

        self.attempt_label = tk.Label(
            root,
            text="Attempts: 0",
            font=("Arial", 12),
            bg="#172554",
            fg="#FACC15"
        )
        self.attempt_label.pack(pady=5)

        button_frame = tk.Frame(root, bg="#172554")
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="RESTART GAME",
            font=("Arial", 10, "bold"),
            bg="#38BDF8",
            command=self.restart
        ).pack(side="left", padx=5)

        tk.Button(
            button_frame,
            text="EXIT",
            font=("Arial", 10, "bold"),
            bg="#EF4444",
            fg="white",
            command=root.destroy
        ).pack(side="left", padx=5)

        self.restart()

    def restart(self):
        self.number = random.randint(1, 100)
        self.attempts = 0
        self.running = True

        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.message.config(
            text="Enter your guess!",
            fg="white"
        )
        self.attempt_label.config(text="Attempts: 0")

    def check_guess(self):
        if not self.running:
            return

        try:
            guess = int(self.entry.get())

            if guess < 1 or guess > 100:
                self.message.config(
                    text="Enter a number from 1 to 100!",
                    fg="#EF4444"
                )
                return

            self.attempts += 1
            self.attempt_label.config(
                text=f"Attempts: {self.attempts}"
            )

            if guess < self.number:
                self.message.config(
                    text="Too Low! Try Again.",
                    fg="#FACC15"
                )

            elif guess > self.number:
                self.message.config(
                    text="Too High! Try Again.",
                    fg="#FACC15"
                )

            else:
                self.message.config(
                    text=f"Correct! You Won in {self.attempts} Attempts!",
                    fg="#22C55E"
                )
                self.running = False

        except ValueError:
            self.message.config(
                text="Please enter a valid number!",
                fg="#EF4444"
            )

# Main Application
root = tk.Tk()
game = NumberGuessingGame(root)
root.mainloop()
