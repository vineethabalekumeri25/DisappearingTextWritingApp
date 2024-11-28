from tkinter import *

# LOGIC
user_text = ""
timer = None


def start_calculating(event):
    global timer, user_text

    if timer is not None:
        window.after_cancel(timer)

    if event.keysym == "BackSpace":
        user_text = user_text[0: len(user_text) - 1]

    elif event.char:
        user_text += event.char
        timer = window.after(5000, reset_app)

    return


def reset_app():
    global timer, user_text
    typing_area.delete('1.0', 'end')
    user_text = ""
    timer = None
    return


def save_text():
    global user_text
    if user_text == "":
        return
    try:
        f = open('writeups.txt', 'r')
    except FileNotFoundError:
        f = open('writeups.txt', 'w')
        f.write(user_text)
        user_text = ""
        return
    else:
        cont = f.read()
        if cont == "":
            text_to_write = user_text
        else:
            text_to_write = f'\n{user_text}'

        with open('writeups.txt', 'a') as f:
            f.write(text_to_write)
            user_text = ""
    finally:
        return


# UI SETUP

BORDER = "#E0E0E0"
FG = '#333333'
BG = "#F7F7F7"

FONT_FAMILY1 = 'Times New Roman'
FONT_FAMILY2 = 'Times New Roman'

FONT_SIZE1 = 14
FONT_SIZE2 = 16
FONT_SIZE3 = 20

FONT_STYLE1 = 'bold'
FONT_STYLE2 = 'italic'
FONT_STYLE3 = 'normal'

PARA_FONT = (FONT_FAMILY1, FONT_SIZE1, FONT_STYLE3)
PARA_FONT2 = (FONT_FAMILY2, 12, FONT_STYLE2)
HEAD_FONT = (FONT_FAMILY2, FONT_SIZE3, FONT_STYLE1)

heading = "Disappearing Text Writing App"
instruction = "If you don't press any key for 5 seconds, \
the text you have written will disappear"

window = Tk()
window.title('Disappearing Text Desktop App')
window.config(bg=BG, padx=20, pady=10)

heading = Label(text=heading, font=HEAD_FONT,
                bg=BG, fg=FG, padx=10, pady=10)
instruction = Label(text=instruction, font=PARA_FONT2,
                    fg=FG, bg=BG, pady=10)
typing_area = Text(font=PARA_FONT, bg="white", fg=FG,
                   width=100, height=15, wrap='w',
                   highlightcolor=BORDER,
                   highlightthickness=2,
                   highlightbackground=BORDER,
                   padx=5, pady=5)
typing_area.bind('<KeyPress>', start_calculating)
reset_btn = Button(text='Reset', fg="white", bg="#5A9BD4",
                   font=PARA_FONT,
                   highlightbackground="#5A9BD4",
                   highlightcolor="#5A9BD4",
                   highlightthickness=0, border=3,
                   command=reset_app, width=50)

save_btn = Button(text='Save', fg="white", bg="#5A9BD4",
                  font=PARA_FONT,
                  highlightbackground="#5A9BD4",
                  highlightcolor="#5A9BD4",
                  highlightthickness=0, border=3,
                  command=save_text, width=50)

heading.grid(row=0, column=0, columnspan=3)
instruction.grid(row=2, column=0, columnspan=3)
typing_area.grid(row=3, column=0, columnspan=3)
reset_btn.grid(row=4, column=0)
save_btn.grid(row=4, column=2)

window.mainloop()