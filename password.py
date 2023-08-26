import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("420x500")
        self.root.configure(bg="light yellow")

        self.heading_label = tk.Label(root, text="Password Generator", font=("Arial", 18, "bold", "underline"),bg="light yellow", fg="dark blue")
        self.heading_label.pack(pady=2)

        self.username_label = tk.Label(root, text="Enter User Name:",  font=("Arial", 14, "bold"), fg="orange",bg="light yellow")
        self.username_label.pack(pady=15)

        self.username_entry = tk.Entry(root, font=("Arial", 14))
        self.username_entry.pack(pady=10)

        self.length_label = tk.Label(root, text="Enter Password Length:", font=("Arial", 14, "bold"),fg = "green",bg="light yellow")
        self.length_label.pack(pady=10)

        self.length_entry = tk.Entry(root, font=("Arial", 14))
        self.length_entry.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, bg="blue", fg="white", font=("Arial", 14))
        self.generate_button.pack(pady=20)

        self.generated_password_label = tk.Label(root, text="Generated Password:", font=("Arial", 10),bg ="light pink")
        self.generated_password_label.pack(pady=10)

        self.generated_password_frame = tk.Frame(root, bg="gray", height=100, width=300)
        self.generated_password_frame.pack(padx=10, pady=5, fill=tk.X)

        self.generated_password = tk.Label(self.generated_password_frame, text="", font=("Arial", 16))
        self.generated_password.pack(pady=10)

        self.accept_button = tk.Button(root, text="Accept", command=self.accept_password, font=("Arial", 12),bg = "orange")
        self.accept_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_password, font=("Arial", 12),bg = "light green")
        self.reset_button.pack(side=tk.RIGHT, padx=10, pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            complexity = 3

            if length <= 0:
                raise ValueError("Invalid length. Please enter a positive integer.")

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            self.generated_password.config(text=password)
        except ValueError as e:
            self.generated_password.config(text=str(e))

    def accept_password(self):
        generated_password = self.generated_password.cget("text")
        self.username_entry.delete(0, tk.END)
        self.length_entry.delete(0, tk.END)
        self.generated_password.config(text="")
        print("Accepted Password:", generated_password)

    def reset_password(self):
        self.username_entry.delete(0, tk.END)
        self.length_entry.delete(0, tk.END)
        self.generated_password.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    password_generator = PasswordGenerator(root)
    root.mainloop()
