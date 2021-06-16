# Made by @Saksham Solanki, Date: 16/5/2021 (DD/MM/YYYY) 0:4 (24-hour-format)

# --------------------------------------- Import Libraries ---------------------------------------#
import datetime
import os
import time
import tkinter as tk
from tkinter import END, filedialog
from PIL import Image, ImageTk
# ------------------------------------------------------------------------------------------------#
# ---------------------------------------- Init variables ----------------------------------------#
params = []
current_time = datetime.datetime.now()
# ------------------------------------------------------------------------------------------------#
# --------------------------------------- Get File Content ---------------------------------------#
def read(file):
    with open(file, "r") as f:
        content = f.read()
        f.close()
    return content
# ------------------------------------------------------------------------------------------------#
# --------------------------------------- Param Functions ----------------------------------------#
def add_date():
    params.append("date")

def add_time():
    params.append("time")

def get_auto():
    params.append("auto")
# ------------------------------------------------------------------------------------------------#
# --------------------------------------- Main Signing Func --------------------------------------#
def sign():

    signature = (
        "# Made by @Saksham Solanki, Date: "
        + str(current_time.day)
        + "/"
        + str(current_time.month)
        + "/"
        + str(current_time.year)
        + " (DD/MM/YYYY) "
        + "Time: "
        + str(current_time.hour)
        + ":"
        + str(current_time.minute)
        + " (24-hour-format)"
    )

    file = filedialog.askopenfilenames(
        parent=window,
        initialdir="/",
        initialfile="tmp",
        filetypes=[("PYTHON", "*.py"), ("All files", "*")],
    )
    try:
        data = read(file[0])
    except:
        print("No file found")
        exit()

    Main = main.get("1.0", END)
    Main = list(Main.splitlines())
    Main = Main[0]
    
    if len(Main) > 2:
        signature = "# " + Main
        with open("settings.sign", 'w+') as f:
            f.write(signature)
            f.close()
    if "date" in params:
        signature = (
            signature
            + ", Date: "
            + str(current_time.day)
            + "/"
            + str(current_time.month)
            + "/"
            + str(current_time.year)
            + " (DD/MM/YYYY) "
        )
    if "time" in params:
        signature = (
            signature
            + "Time: "
            + str(current_time.hour)
            + ":"
            + str(current_time.minute)
            + " (24-hour-format)"
        )
    if "auto" in params:
        if len(Main) > 2:
            pass
        else:
            with open("settings.sign", "r") as f:
                signature = f.read()
                f.close()
        c_time = os.path.getctime(file[0])
        c_time = time.ctime(c_time)
        t_object = time.strptime(c_time)
        signature = signature + f"Date: {str(time.strftime('%d/%m/%Y', t_object))} (DD/MM/YYYY), Time: {str(time.strftime('%H:%M', t_object))} (24-hour-format)"
    with open(file[0], "w+") as f:
        f.write(signature + "\n" + data)
        f.close()

# ------------------------------------------------------------------------------------------------#
# -------------------------------------- GUI and main func ---------------------------------------#
if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("400x300")
    window.title("Signature")
    img = Image.open("bg.png")
    imgg = ImageTk.PhotoImage(img)
    tk.Label(window, image=imgg).place(x=88,y=-2)
    tk.Frame(window, bg="#71C9FB",width=90,height=300).place(x=0,y=0)
    tk.Label(window, bg="#71C9FB",text="S\ni\ng\nn\na\nt\nu\nr\ne", font=("Comic Sans MS",15,"bold"),fg="white").place(x=36,y=19)
    button = tk.Button(window, text="Browse Files", bg="#71C9FB",fg="white",font=("Arial", 11), relief='flat', command=lambda: [sign()])
    button.place(x=264, y=208)
    tk.Label(window, text="Enter Your Sign:", bg="#9BE7DE", fg="white",font=("Arial",15)).place(x=109,y=53)
    main = tk.Text(window, height=1, width=10)
    main.place(relx=0.7, rely=0.2)
    date_button = tk.Button(window, text="Include Date",bg="#71C9FB",fg="white",font=("Arial", 12), relief='flat',command=lambda: [add_date()])
    date_button.place(x=122, y=151)
    time_button = tk.Button(window, text="Include Time",bg="#71C9FB",fg="white",font=("Arial", 12), relief="flat", command=lambda: [add_time()])
    time_button.place(x=261, y=151)
    tk.Button(window, text='Automatically',bg="#71C9FB",fg="white",font=("Arial", 11), relief="flat", command=lambda:[get_auto()]).place(x=122, y=208)
    window.mainloop()
# -----------------------------------------------------------------------------------------------#