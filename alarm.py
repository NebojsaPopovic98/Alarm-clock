import tkinter as tk
import datetime
import winsound
import time

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime('%H:%M:%S')
        date = current_time.strftime('%d:%m:%Y')
        print('The set date is: ', date)
        print(now)
        if now == set_alarm_timer:
            print('Time to wake up!')
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)
    
clock = tk.Tk()
clock.title('Alarm clock')
clock.geometry('300x200')
time_format = tk.Label(clock, text='Enter time in 24 hour format!', fg = 'white', bg = 'blue', font = 'Arial').place(x = 60, y = 120)
addTime = tk.Label(clock, text= 'Hour    Min     Sec', font= 60).place(x = 110)
setYourAlarm = tk.Label(clock, text='When to wake you up', fg = 'blue', relief= 'solid', font=('Helvetica',7,'bold')).place(x = 0, y = 29)

hour = tk.StringVar()
min = tk.StringVar()
sec = tk.StringVar()

hourTime = tk.Entry(clock, textvariable=hour, bg = 'pink', width=15).place(x=110, y=30)
minTime = tk.Entry(clock, textvariable= min, bg= 'pink', width=15).place(x = 150, y = 30)
secTime = tk.Entry(clock, textvariable= sec, bg= 'pink', width=7).place(x = 200, y = 30)

submit = tk.Button(clock, text='Set alarm', fg='black', width=10, command=actual_time).place(x=110, y=70)

clock.mainloop()