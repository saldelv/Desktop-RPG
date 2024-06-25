import tkinter as tk

# Tooltip hover class
class Tooltip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tiproot = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text, h, w):
        self.text = text
        if self.tiproot or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + w
        y = y + cy + self.widget.winfo_rooty() - h
        self.tiproot = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        tw.wm_attributes('-topmost', '1')
        tlabel = tk.Label(tw, text=self.text, justify=tk.LEFT, bg='white', relief=tk.SOLID, borderwidth=1, font='Gill')
        tlabel.pack(ipadx=1)

    def hidetip(self):
        tw = self.tiproot
        self.tiproot = None
        if tw:
            tw.destroy()

# creates tool tip with text and relative location
def CreateToolTip(widget, text, h, w):
    tooltip = Tooltip(widget)
    def enter(set_event):
        tooltip.showtip(text, h, w)
    def leave(set_event):
        tooltip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

# deletes tooltip
def UnbindToolTip(widget):
    widget.unbind('<Enter>')
    widget.unbind('<Leave')

# creates right click menues
def do_menu(event, menu):
    try:
        menu.tk_popup(event.x_root, event.y_root)
    finally:
        menu.grab_release()

# saves stats and inventory
def do_quit(character):
    character.save()
    quit()