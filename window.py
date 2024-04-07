from tkinter import *
from PIL import Image, ImageTk
import random

def guess():
    wait.config(state = NORMAL)
    wait.delete(0, END)
    prediction.delete(0, END)
    answer.delete(0, END)

    username = name.get()
    thinking_color = color.get()
    wait_time = random.randint(5, 10)

    thinking_color = thinking_color.lower()

    wait.insert(0, f"Please wait for {wait_time} seconds to get your result")
    wait.config(state = DISABLED)
    prediction.insert(0, "The prediction is below: ")
    prediction.config(state = DISABLED)

    window.after(wait_time * 1000, lambda: print_message(username, thinking_color))

def print_message(username, thinking_color):
    answer.delete(0, END)
    if thinking_color == "blackpink" :
        answer.insert(0, f"{username} is thinking the color: {thinking_color}")
        window.configure(bg = blackpink)
    elif thinking_color in color_names :
        answer.insert(0, f"{username} is thinking the color: {thinking_color}")
        window.configure(bg = f"{thinking_color}")
    else :  
        answer.insert(0, f"FUCK YOU, {thinking_color} is not a color!!!")

def clear_name():
    name.delete(0, END)

def backspace_name():
    name.delete(len(name.get()) - 1, END)

def keyboard(press):
    if press.keysym == 'Escape':
        window.quit()

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y - 25}")


window = Tk()
window.configure(bg = "BLACK")
window.title('Guess what you are thinking!')
center_window(window, 1000, 800)

image = Image.open("/Users/edmondhuang/Desktop/Coding/python/blackpink.png")
blackpink = ImageTk.PhotoImage(image)

color_names = [
    "aliceblue", "antiquewhite", "aqua", "aquamarine", "azure",
    "beige", "bisque", "blanchedalmond", "burlywood", "blue",  
    "cadetblue", "chartreuse", "chocolate", "coral", "cornflowerblue", 
    "cornsilk", "crimson", "cyan", "darkgoldenrod", "darkkhaki", 
    "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", 
    "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", 
    "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", 
    "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia",
    "gainsboro", "ghostwhite", "gold", "goldenrod", "gray", "green", 
    "greenyellow", "honeydew", "hotpink", "indianred", "ivory", "indigo",
    "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", 
    "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", 
    "lightgray", "lightgreen", "lightpink", "lightsalmon", "lightseagreen", 
    "lightskyblue", "lightslategray", "lightsteelblue", "lightyellow", 
    "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine", 
    "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", 
    "mediumslateblue", "mediumspringgreen", "mediumturquoise", 
    "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin",
    "navajowhite", "navy", "oldlace", "olive", "olivedrab", "orange", 
    "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise", 
    "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum", 
    "powderblue", "purple", "rebeccapurple", "red", "rosybrown", "royalblue",
    "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell", 
    "sienna", "silver", "skyblue", "slateblue", "slategray", "snow", 
    "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", 
    "turquoise", "violet", "wheat", "white", "whitesmoke",
    "yellow", "yellowgreen"
]


enter_button = Button(window, text="Enter", command = guess)
enter_button.pack(side = BOTTOM)
enter_button.config(width = 20)
enter_button.config(height = 6)


asking_name = Entry(window, width = 50)
name = Entry(window, width = 50)
asking_color = Entry(window, width = 50)
color = Entry(window, width = 50)
wait = Entry(window, width = 50)
prediction = Entry(window, width = 50)
answer = Entry(window, width = 50)

asking_name.config(font=('Ink Free', 20))
asking_name.config(bg='#111111')
asking_name.config(fg='WHITE')
asking_name.insert(0, 'Please tell me your name below:')
asking_name.config(state = DISABLED)
asking_name.pack()

name.config(font=('Ink Free', 20))
name.config(bg='#111111')
name.config(fg='WHITE')
name.pack()

asking_color.config(font=('Ink Free', 20))
asking_color.config(bg='WHITE')
asking_color.config(fg='#111111')
asking_color.insert(0, 'Please tell me what color are you thinking below:')
asking_color.config(state = DISABLED)
asking_color.pack()

color.config(font=('Ink Free', 20))
color.config(bg='#111111')
color.config(fg='WHITE')
color.pack()

wait.config(font=('Ink Free', 20))
wait.config(bg='#111111')
wait.config(fg='WHITE')
wait.pack()

prediction.config(font=('Ink Free', 20))
prediction.config(bg='#111111')
prediction.config(fg='WHITE')
prediction.pack(padx = +10)

answer.config(font=('Ink Free', 20))
answer.config(bg='#111111')
answer.config(fg='WHITE')
answer.pack()

window.bind('<KeyPress>', keyboard)

window.mainloop()