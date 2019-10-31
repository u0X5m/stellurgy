import tkinter as tk
import re
from modules.generators.rttgen import rttgen
from modules.misc_tools.decode_uwp import decode_uwp
from modules.misc_tools.format import label_format

## Initialise GUI Pt 1

root = tk.Tk()
root.title("Stellurgy - A Traveller Generator")

## Output text box things

out_text = "Hello!"
tk_out_text = tk.StringVar()
frame = tk.Frame(root)
frame.grid(row = 0, column = 0)

## A function to update the label with output text:

def update_label(label, text):
    label.set(text)
    
update_label(tk_out_text, out_text)


## Initialise GUI Pt 2
"""
out_box = tk.Label(root,
                   height = 50,
                   width = 50,
                   bg = "white",
                   bd = 2,
                   anchor = "nw",
                   justify = "left",
                   textvariable = tk_out_text)
out_box.grid(row = 0, column = 1)
"""
## A tool to decode UWPs into plain english
"""
tk.Label(frame, text = "Decode UWP:").grid(row = 0)

def decode_uwp(out_text):
    uwp = uwp_entry.get()
    rex = re.compile("^[ABCDEFGHXY][0-9ABCDEF]{5}[0-9A-M][\\-][0-9A-M]$")
    if rex.match(uwp):
        out_text = "UWP"
    else:
        out_text = "Invalid UWP"
    update_label(tk_out_text, out_text)


uwp_entry = tk.Entry(frame)
uwp_entry.grid(row = 0, column = 1)
uwp_entry.insert(0, "AXXXXXX-X")

uwp_button = tk.Button(frame,
                   text = "Decode",
                   command = lambda: decode_uwp(out_text))
uwp_button.grid(row = 0, column = 2)
"""

## System Generator

tk.Label(frame, text = "System Name:").grid(row = 0)

sysname_entry = tk.Entry(frame)
sysname_entry.grid(row = 1, column = 0)
sysname_entry.insert(0, "Hyperion")

def create_window():
    window = tk.Toplevel(root)

def sysgen_b():
    system = sysgen(sysname_entry.get())
    system = label_format(system)
    window = tk.Toplevel(root)
    tk_out_text = tk.StringVar()
    tk_out_text.set(system)
    win_frame = tk.Frame(window)
    out_box = tk.Text(win_frame,
                       width = 80,
                       height = 50)
    out_box.insert(tk.END, system)    
    scrollbar = tk.Scrollbar(win_frame)
    scrollbar.pack(side="right", fill = "y")
    out_box.pack()
    scrollbar.config(command=out_box.yview)
    out_box.config(yscrollcommand=scrollbar.set)
    win_frame.pack()
    

sysgen_button = tk.Button(frame,
                   text = "Generate System",
                   command = lambda: sysgen_b())

sysgen_button.grid(row = 2, column = 0)
              
quit_button = tk.Button(frame,
                   text = "Quit",
                   fg = "red",
                   command = quit)
quit_button.grid(row = 3, column = 0)

root.mainloop()

