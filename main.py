BACKGROUND_COLOR = "#B1DDC6"
import pandas
import random
from tkinter import *

try:
    data=pandas.read_csv('data/Words to learn.csv')

except:
    data = pandas.read_csv('data/french_words.csv')
    new_data = data.to_dict(orient='records')
else:
    new_data = data.to_dict(orient='records')


french=''
english=''
Language=''




window=Tk()
card = random.choice(new_data)
def flip_card():
    global card,english,time
    canvas.itemconfig(card_flip,image=back_card_image)
    canvas.itemconfig(Lang,text='English')

    english=card['English']
    canvas.itemconfig(word,text=english)



def next():
    global  french,english,Language,card,time

    window.after_cancel(time)

    card = random.choice(new_data)
    french=card['French']


    canvas.itemconfig(Lang,text='French')
    canvas.itemconfig(word,text=french)

    canvas.itemconfig(card_flip,image=front_card_image)
    new_data.remove(card)
    time=window.after(3000, flip_card)
def unknown():
    global french, english, Language, card, time

    window.after_cancel(time)

    card = random.choice(new_data)
    french = card['French']

    canvas.itemconfig(Lang, text='French')
    canvas.itemconfig(word, text=french)

    canvas.itemconfig(card_flip, image=front_card_image)
    time = window.after(3000, flip_card)



time=window.after(3000,flip_card)


window.config(padx=20,pady=20)
window.minsize(800,600)

canvas=Canvas(width=800,height=530,highlightthickness=0,bg=BACKGROUND_COLOR)

canvas.grid(column=0,row=0, columnspan=3)


front_card_image=PhotoImage(file='images/card_front.png')

back_card_image=PhotoImage(file='images/card_back.png')


card_flip=canvas.create_image(400,530/2,image=front_card_image)
Lang=canvas.create_text(400,230/2,text='French',font=('Times New Roman',30,'bold'),fill='black')

word=canvas.create_text(400,630/2,text='french',font=('Times New Roman',30,'normal'),fill='black')


right_image=PhotoImage(file='images/right.png')


right_button=Button(image=right_image,command=next)
right_button.grid(column=2,row=1)

left_image=PhotoImage(file='images/wrong.png')

left_button=Button(image=left_image,command=unknown)

left_button.grid(column=0,row=1)


window.config(bg=BACKGROUND_COLOR)


next()



window.mainloop()

new_data=pandas.DataFrame(new_data)

new_data.to_csv('data/Words to learn.csv',index=False)

