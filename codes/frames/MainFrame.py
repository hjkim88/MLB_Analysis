###
#   File name  : MainFrame.py
#   Author     : Hyunjin Kim
#   Date       : December 7, 2019
#   Email      : firadazer@gmail.com
#   Purpose    : The GUI main frame for the MLB Analysis
#
#   * The GUI was created by PAGE - A Python GUI generator
#
#   Instruction
#               1. import MainFrame.py
#               2. Run the function MainFrame.start()
#               3. The results will be generated in the output path
###

### import modules
import tkinter as tk

### a class for the main frame
class MainApp():
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack(fill=tk.BOTH, expand=True)

        ### set title of the frame
        master.title("Analysis Main Frame")

        ### Pitcher
        self.pLbl = tk.Label(frame, text="Pitcher Name:")
        self.pEty = tk.Entry(frame)

        ### Batter
        self.bLbl = tk.Label(frame, text="Batter Name:")
        self.bEty = tk.Entry(frame)

        ### start year
        self.sLbl = tk.Label(frame, text="Start Year:")
        self.sEty = tk.Entry(frame)

        ### end year
        self.eLbl = tk.Label(frame, text="End Year:")
        self.eEty = tk.Entry(frame)

        ### Log in button
        self.okBtn = tk.Button(frame,
                               text="Stats", fg="black", width=20,
                               command=self.print_info)

        ### Quit button
        self.qBtn = tk.Button(frame,
                              text="Quit", fg="black", width=20,
                              command=frame.quit)

        ### set location of all the components of the frame
        self.pLbl.place
        self.pLbl.grid(row=0, column=0)
        self.pEty.grid(row=0, column=1, columnspan=2, sticky='nesw')
        self.bLbl.grid(row=1, column=0)
        self.bEty.grid(row=1, column=1, columnspan=2, sticky='nesw')
        self.sLbl.grid(row=2, column=0)
        self.sEty.grid(row=2, column=1, columnspan=2, sticky='nesw')
        self.eLbl.grid(row=3, column=0)
        self.eEty.grid(row=3, column=1, columnspan=2, sticky='nesw')
        self.okBtn.grid(row=4, column=0)
        self.qBtn.grid(row=4, column=2)

    def print_info(self):
        print("Pitcher = ", self.pEty.get(), ", Batter = ", self.bEty.get())
        print("Start Year = ", self.sEty.get(), ", End Year = ", self.eEty.get())


### a function to make a tkinter frame centered
"""
:param win: the root or top level window to be centered
"""
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


###  call the main frame
def print_frame():
    print("print_frame()")

    main_frm = tk.Tk()
    main_frm.geometry("1200x800")
    MainApp(main_frm)
    center(main_frm)
    main_frm.mainloop()


### a function starting this script
def start():
    print("MainFrame.py")

    print_frame()


start()
