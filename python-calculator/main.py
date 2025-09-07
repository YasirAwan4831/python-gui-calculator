import tkinter as tk
import math

# Create the main application window
root = tk.Tk()
# Set window title
root.title("Python Calculator")
# Set  window size          
root.geometry("380x640")                         
root.resizable(False, False)
#  background color
root.configure(bg="#1e1e1e")                     

# Create the input display (entry widget)
entry = tk.Entry(
    root,
    font=("Helvetica", 24),
    justify="right",
    bg="#252526",
    fg="white",
    insertbackground="white"
)
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=5) 

# Function to handle button clicks
def press(key):
    if key == "=":
        try:
            # Replace symbols with Python equivalents before evaluation
            expression = entry.get().replace("×", "*").replace("÷", "/").replace("^", "**").replace("−", "-")
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")       
    elif key == "C":
        entry.delete(0, tk.END)                 # Clear the display
    elif key == "√":
        try:
            value = float(entry.get())
            result = math.sqrt(value)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))   # print  result
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")       # Display error invalid input
    else:
        entry.insert(tk.END, key)

# Define the layout of buttons
buttons = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "−"],
    ["0", ".", "=", "+"],
    ["C", "√", "^", "%"]
]

# Button style settings
btn_bg = "#3c3c3c"
btn_fg = "#f3eded"
btn_active_bg = "#007acc"
btn_font = ("Helvetica", 18)

# Create buttons dynamically using loops
for row in buttons:
    frame = tk.Frame(root, bg="#272323") 
    frame.pack(expand=True, fill="both", padx=5, pady=5)
    for btn in row:
        # Use lambda to pass the button label to the press function
        action = lambda x=btn: press(x)
        tk.Button(
            frame,
            text=btn,
            command=action,
            font=btn_font,
            bg=btn_bg,
            fg=btn_fg,
            activebackground=btn_active_bg,
            activeforeground="white",
            relief="raised",
            bd=2,
            height=2,                           # Consistent button height
            width=4                             # Consistent button width
        ).pack(side="left", expand=True, fill="both", padx=5, pady=5)

# Start the GUI event loop
root.mainloop()
# end of the code 