import tkinter as tk

def update_label():
    label.config(text="Hello,Tkinter!")


root = tk.Tk()
root.title("Simple Tkinter GUI")
root.geometry("300x200")


label = tk.Label(root, text ="Click the button")
label.pack(pady=20)


button = tk.Button(root, text ="Click Me", command=update_label)
button.pack(pady=10)


root.mainloop()
