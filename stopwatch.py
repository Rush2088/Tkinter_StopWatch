# tkinter based stopwatch

import tkinter as tk
import time

window = tk.Tk()
window.title("Stopwatch")
window.geometry("250x100")
window.minsize(100, 100) 
window['bg'] = '#0059b3' 

h=0; m=0; s=0; ms=0
stop_flag=False
reset_txt=f"00:00:00:00"

def clock_run():
    global h, m, s, ms

    if not stop_flag:

    # Delete old text
        clock_lbl['text']=f"{h:02}:{m:02}:{s:02}:{abs(ms):02}"
        ms+=10
        if ms == 100:
            s+=1; ms= 0
        elif s == 60:
            m+=1; s=0
        elif m == 60:
            h+=1; m=0
        # After 1 second, call Run again (start an infinite recursive loop)
        window.after(100, clock_run)
      
def  Start():
    global stop_flag
    stop_flag=False
    clock_run()  


def Stop():
    global stop_flag
    stop_flag=True 


# toggle button (shared for START & STOP)
def clicked_start(event=None):
    # Toggle Button
    if start_btn['text'] in  {"START" , "RESUME"}:
        reset_btn.pack_forget()
        start_btn['text']  ='STOP'
        Start() # process associated with button
    else:
        start_btn['text'] == "STOP"
        start_btn['text']  ='RESUME'
        reset_btn.pack(side =tk.LEFT, ipady=10, expand=True, anchor='w')
        Stop()

# reset button
def reset1(event=None):
    global s,m,h,ms
    global stop_flag
    s=0; m=0; h=0; ms=0
    clock_lbl['text']=reset_txt
    stop_flag=False
    start_btn['text']  ='START'
    reset_btn.pack_forget()

clock_lbl = tk.Label(master=window, height=2, width=10, 
            text=reset_txt,bg= '#0059b3', fg="white",font=(None, 20))
clock_lbl.pack(side =tk.TOP, fill=tk.X , expand=False)


frm_Bot = tk.Frame(master=window, bg= '#beb7e2',height =100, relief=tk.GROOVE, borderwidth=2)
frm_Bot.pack(side =tk.TOP,  expand=False)

start_btn = tk.Button(master=frm_Bot, text="START", width=10, command=clicked_start)
start_btn.pack(side =tk.LEFT, ipady=10 , expand=True, anchor='e')

reset_btn = tk.Button(master=frm_Bot, text="RESET",width=10,command = reset1 )

# key Bindings
window.bind('<Return>', clicked_start)
window.bind('<Control-r>', reset1)
window.bind('<Control-q>', lambda e : window.destroy())

window.mainloop()





