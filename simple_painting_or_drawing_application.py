import tkinter as tk
from tkinter import *
from tkinter import colorchooser

class Paint:
    def __init__(self):
        self.t=tk.Tk()
        self.t.title("SIMPLE PAINTING/DRAWING APPLICATION")

        # Set desired window size
        window_width = 800
        window_height = 700
        # Get the screen dimensions
        screen_width = self.t.winfo_screenwidth()
        screen_height = self.t.winfo_screenheight()
        # Calculate x and y coordinates to center the window
        center_x = int((screen_width - window_width) / 2)
        center_y = int((screen_height - window_height) / 2)
        # Set the geometry and position
        self.t.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        self.t.resizable(False, False)

        self.color="black"
        self.size=5

        self.last_x=None
        self.last_y=None
        self.canvas=Canvas(self.t, bg="white", width=1000, height=500)
        self.canvas.pack()

        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")

        self.frame1=Frame(self.t)
        self.frame1.pack(pady=10)

        self.label1=Label(self.frame1,text="SIZE: ", font=("Arial",10,"bold"))
        self.label1.pack(side="left",pady=5)
        self.size_entry = Entry(self.frame1,width=5)

        self.size_entry.insert(0,"5")
        self.size_entry.pack(pady=5,side="left")

        color_button = Button(self.frame1, text="SELECT ANY COLOR", activeforeground="lightblue",activebackground="midnightblue",
                              fg="midnightblue",bg="lightblue", width=20, height=3, font=("Arial", 10, "bold"), command=self.choose_color)
        color_button.pack(side="left", padx=5)

        start_button = Button(self.frame1, text="START", activeforeground="lightblue", activebackground="midnightblue",
                              fg="midnightblue", bg="lightblue", width=20, height=3, font=("Arial", 10, "bold"),command=self.start)
        start_button.pack(side="left", padx=5)

        erase_button = Button(self.frame1, text="ERASE", activeforeground="lightblue", activebackground="midnightblue",
                             fg="midnightblue",bg="lightblue", width=10, height=3, font=("Arial", 10, "bold"), command=self.erase)
        erase_button.pack(side="left",padx=5)

        clear_button = Button(self.frame1, text="CLEAR", activeforeground="lightblue", activebackground="midnightblue",
                              fg="midnightblue",bg="lightblue", width=10, height=3, font=("Arial", 10, "bold"), command=self.clear)
        clear_button.pack(side="left",padx=5)

        quit_button = Button(self.frame1, text="QUIT", activeforeground="lightblue", activebackground="midnightblue",
                              fg="midnightblue",bg="lightblue", width=10, height=3, font=("Arial", 10, "bold"), command=self.quit)
        quit_button.pack(side="left",padx=5)

    def draw_(self, event):

    # event.x,event.y: The current mouse position during a drag
    # self.last_x,self.last_y are coordinates of last mouse position
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        try:
            size_ = float(self.size_entry.get())
        except ValueError:
            print("Enter only integers or float values")
            return

        self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                fill=self.color, width=size_, capstyle=ROUND,smooth=True)
        self.last_x = event.x
        self.last_y = event.y

    def start(self):

    #<Button-1 refers to left mouse button click
    #self.start_draw is called when the user clicks the left mouse button on the canvas.
        self.canvas.bind("<Button-1>", self.draw_)

    #<B1-Motion>: Refers to mouse movement while the left button (Button 1) is held down.
    #self.draw is called repeatedly as the mouse moves with the button held down.
        self.canvas.bind("<B1-Motion>", self.draw)

#Opens a color chooser dialog. Sets the brush to the selected color
    def choose_color(self):
        color_=colorchooser.askcolor(title="Colors")
        if color_[1]:
            self.color=color_[1]

    def erase(self):
        self.color="white"

    def clear(self):
        self.canvas.delete("all")

    def quit(self):
        self.t.destroy()

    def run_game(self):
        self.t.mainloop()

paint=Paint()
paint.run_game()
