import tkinter as tk

import tk_geometry

root = tk.Tk()


window = root

tk_geometry.geometry(window)


def create():
    top = tk.Toplevel()
    top.title("Python")
    tk_geometry.geometry(top, width=300, height=150)

    msg = tk.Message(top, text="I love Python!")
    msg.pack()


tk.Button(root, text="创建顶级窗口", command=create).pack()

root.mainloop()
