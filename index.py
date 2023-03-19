import tkinter as tk
import time

# Function to update the clock every second
def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

     # Check if the current time matches the alarm time and change the background color if necessary
    if alarm_time is not None and current_time == alarm_time:
        window.configure(bg='#ff0000')
    else:
        window.configure(bg='#333')

    clock_label.after(1000, update_clock)


def change_color():
    color_window = tk.Toplevel()
    color_window.title('Choose a Color')

    # Create a canvas with rectangles of different colors
    canvas = tk.Canvas(color_window, width=200, height=200)
    canvas.pack()
    colors = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#00ffff','#FFAEBC']
    for i, color in enumerate(colors):
        canvas.create_rectangle(i*30, 0, i*30+30, 30, fill=color, outline='black')

    # Function to set the clock text color when a rectangle is clicked
    def set_color(event):
        x = event.x // 30
        clock_label.config(fg=colors[x])
        color_window.destroy()

    # Bind the set_color function to the canvas click event
    canvas.bind('<Button-1>', set_color)


# Function to set the alarm time
def set_alarm_time():
    global alarm_time
    alarm_time = alarm_entry.get()
    alarm_label.config(text=f'Alarm set for {alarm_time}')



# Create a new window
window = tk.Tk()
window.title('Clock Window')

# Set the window size and background color
window.geometry('600x300')
window.configure(bg='#333')

# Create a label to display the clock
clock_label = tk.Label(window, text='', font=('Arial', 36), fg='#469597', bg='#333')
clock_label.pack(pady=20)


# color button 
color_button = tk.Button(window , text='change color text' , command=change_color)
color_button.pack(pady=10)


# Create a label and entry for setting the alarm time
alarm_label = tk.Label(window, text='Set alarm time (HH:MM:SS):')
alarm_label.pack(pady=10)
alarm_entry = tk.Entry(window)
alarm_entry.pack(pady=5)
set_alarm_button = tk.Button(window, text='Set Alarm', command=set_alarm_time)
set_alarm_button.pack(pady=10)

# Initialize the alarm time to None
alarm_time = None


# Start the clock update loop
update_clock()


# Start the main event loop
window.mainloop()