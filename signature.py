# Made by @Saksham Solanki, Date: 16/5/2021 (DD/MM/YYYY) 0:4 (24-hour-format)

#--------------------------------------- Import Libraries ---------------------------------------#
import datetime
import tkinter as tk
from tkinter import filedialog
from tkinter import END
#------------------------------------------------------------------------------------------------#
#---------------------------------------- Init variables ----------------------------------------#
params = []
current_time = datetime.datetime.now()
#------------------------------------------------------------------------------------------------#
#--------------------------------------- Get File Content ---------------------------------------#
def read(file):
    with open(file,'r') as f:
        content = f.read()
        f.close()
    return content
#------------------------------------------------------------------------------------------------#
#--------------------------------------- Param Functions ----------------------------------------#
def add_date():
    params.append("date")

def add_time():
    params.append("time")
#------------------------------------------------------------------------------------------------#
#--------------------------------------- Main Signing Func --------------------------------------#
def sign():

    signature = "# Made by @Saksham Solanki, Date: "+ \
    str(current_time.day)+"/"+str(current_time.month)+"/"+str(current_time.year)+" (DD/MM/YYYY) "+ \
    "Time: "+str(current_time.hour)+":"+str(current_time.minute)+" (24-hour-format)"

    file = filedialog.askopenfilenames(parent=window, initialdir='/', \
    initialfile='tmp',filetypes=[("PYTHON","*.py"), ("All files", "*")])
    try: 
        data = read(file[0])
    except:
        print("No file found")
        exit()

    Main = main.get('1.0',END)
    Date = date.get('1.0',END)
    Time = time.get('1.0',END)
    Main = list(Main.splitlines())
    Main = Main[0]
    Date = list(Date.splitlines())
    Date = Date[0]
    Time = list(Time.splitlines())
    Time = Time[0]

    print(Main)
    if len(Main) > 2:
        signature = "# "+ Main
    if len(Date) > 2:
        signature = signature + ", " + "Date: " +Date+" (DD/MM/YYYY)"
    if len(Time) > 2:
        signature = signature + " Time: "+Time+" (24-hour-format)"
    if len(Date) < 2 and "date" in params:
        signature = signature + ", Date: "+str(current_time.day)+"/"+str(current_time.month)+"/"+str(current_time.year)+" (DD/MM/YYYY) "
    if len(Time) < 2 and "time" in params:
        signature = signature + "Time: "+str(current_time.hour)+":"+str(current_time.minute)+" (24-hour-format)"
    with open(file[0],'w+') as f:
        f.write(signature+'\n'+data)
        f.close()
#------------------------------------------------------------------------------------------------#
#-------------------------------------- GUI and main func ---------------------------------------#
if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("400x300")
    window.title("Signature")
    button = tk.Button(window, text="Browse File",command=lambda:[sign()])
    button.place(relx=0.4,rely=0.75)
    comment = tk.Label(window,text="Main comment (Like - Made by @XYZ): ")
    comment.place(relx=0.1,rely=0.2)
    main = tk.Text(window,height=1,width=10)
    main.place(relx=0.7,rely=0.2)
    date_label = tk.Label(window,text="Enter Date (DD/MM/YYYY): ").place(relx=0.1,rely=0.3)
    date = tk.Text(window,height=1,width=10)
    date.place(relx=0.7,rely=0.3)
    time_label = tk.Label(window,text="Enter Time (24-hour-format): ").place(relx=0.1,rely=0.4)
    time = tk.Text(window, height=1,width=10)
    time.place(relx=0.7,rely=0.4)
    formatt = tk.Label(window,text="(HH:MM)").place(relx=0.73,rely=0.47)
    date_button = tk.Button(window,text="Date",command=lambda:[add_date()])
    date_button.place(relx=0.39,rely=0.6)
    time_button = tk.Button(window,text="Time",command=lambda:[add_time()])
    time_button.place(relx=0.5,rely=0.6)
    window.mainloop()
#-----------------------------------------------------------------------------------------------#