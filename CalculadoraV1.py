import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)
    
def button_clear():
    entry.delete(0, tk.END)
    
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        
window = tk.Tk()
window.title("Calculadora")

# create the calculator buttons
entry = tk.Entry(window, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 3, 1), ("=", 4, 2), ("+", 4, 3),
    ("DelAll", 5, 0)
]

for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(window, text=text, width=10, height=3, font=("Arial", 18), command=button_equal)
    elif text == "DELAll":
        button = tk.Button(window, text=text, width=10, height=3, font=("Arial", 18), command=button_clear)
    else:
        button = tk.Button(window, text=text, width=10, height=3, font=("Arial", 18), command=lambda value=text: button_click(value))
        
    button.grid(row=row, column=col)
    
window.mainloop()