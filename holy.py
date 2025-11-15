import tkinter as tk

def click(button_text):
    if button_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Modern Calculator")
root.configure(bg="#2b2b2b")

entry = tk.Entry(root, width=16, font=("Helvetica", 28), bg="#2b2b2b", fg="#ffffff", bd=0, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

colors = {
    "bg": "#444444",
    "fg": "#ffffff",
    "op": "#ff9500",
    "hover": "#555555"
}

def make_button(text, row, col, colspan=1):
    bg_color = colors["op"] if text in "+-*/=" else colors["bg"]
    button = tk.Button(root, text=text, bg=bg_color, fg=colors["fg"],
                       font=("Helvetica", 22), bd=0, activebackground=colors["hover"],
                       command=lambda ch=text: click(ch))
    button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)
    return button

for r, row in enumerate(buttons, 1):
    for c, char in enumerate(row):
        colspan = 2 if char == "0" else 1
        make_button(char, r, c, colspan)
        if char == "0":
            break

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
