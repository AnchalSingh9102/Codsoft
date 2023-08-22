import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    process_text(text)

def process_text(text):
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "CE":
        entry.delete(0, tk.END)
    elif text == "←":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text[:-1])
    elif text == "x²":
        try:
            current_text = entry.get()
            result = eval(current_text)**2
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)

def on_key(event):
    key = event.char
    if key in "0123456789./*-+":
        process_text(key)
    elif key == "\r":
        process_text("=")
    elif key == "\x08":
        process_text("←")

root = tk.Tk()
root.title("Calculator")
root.geometry("400x700")
root.configure(bg="black")

entry = tk.Entry(root, font=("Arial", 24, "bold"), justify="right", bg="black", fg="white")
entry.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

button_frame = tk.Frame(root, bg="black")
button_frame.pack()

buttons = [
    "←", "CE", "x²", "+",
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    ".", "0", "00",
    "=", "x²", "00"
]

layout = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15],
    [16, 17, 18, 19]
]

def create_circle_button(frame, text):
    if text in "1234567890":
        bg_color = "light grey"
        fg_color = "black"
    elif text in "/*-+x²":
        bg_color = "sky blue" if text != "=" else "blue"
        fg_color = "black"
    else:
        bg_color = "pink"
        fg_color = "black"
    button = tk.Button(frame, text=text, font=("Arial", 20), width=4, height=2, bd=0,
                       bg=bg_color, fg=fg_color,
                       activebackground="blue" if text == "=" else "red",
                       activeforeground=fg_color,
                       command=lambda t=text: on_click_wrapper(t))
    return button

def on_click_wrapper(text):
    event = tk.Event()
    event.widget = button_dict[text]
    on_click(event)

button_dict = {}

for row, cols in enumerate(layout):
    for col, button_index in enumerate(cols):
        button_text = buttons[button_index]
        button = create_circle_button(button_frame, button_text)
        button.grid(row=row, column=col, padx=5, pady=5)
        button_dict[button_text] = button

root.bind("<Key>", on_key)
root.mainloop()
