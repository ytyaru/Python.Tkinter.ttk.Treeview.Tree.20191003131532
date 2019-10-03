#!/usr/bin/env python3
# coding: utf-8
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title('Application')
root.minsize(640, 480)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

tree = ttk.Treeview(root)
tree.insert('', 0, 'item1', text='item1')
tree.insert('', 'end', 'item2', text='item2', open=True) 
tree.insert('item2', 'end', text='item21')
tree.insert('item2', 'end', text='item22')
tree.insert('', 'end', text='item3')
tree.grid(sticky="SNEW")
tree.focus(tree.identify_row(0))
tree.focus_set()
tree.selection_set(tree.identify_row(0))
root.mainloop()

