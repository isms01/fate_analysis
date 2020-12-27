import tkinter as tk

window = tk.Tk()
# greeting = tk.Label(text="Python rocks!")
# greeting.pack()
# label = tk.Label(text="Hello, Tkinter")

# label = tk.Label(
#     text="Hello, Tkinter",
#     fg="white",
#     bg="black",
#     width=10,
#     height=10
# )
# label.pack()

button = tk.Button(
    text="click me!",
    width=10,
    height=5,
    bg="blue",
    fg="yellow",
)
button.place(x=0,y=0)
window.mainloop()
