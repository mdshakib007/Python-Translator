import tkinter as tk
import ttkbootstrap as ttkb
import googletrans
from googletrans import Translator

root = ttkb.Window()
root.title('Easy Python Translator')
root.geometry('1080x400')
root.resizable(False, False)


# Functions
def label_change():
    c1 = combo1.get()
    c2 = combo2.get()
    label1['text'] = c1
    label2['text'] = c2
    root.after(1000, label_change)


def translate_now():
    try:
        get_text = text1.get(1.0, 'end')
        t1 = Translator()
        translate_text = t1.translate(get_text, src=combo1.get(), dest=combo2.get())
        translate_text = translate_text.text

        text2.delete(1.0, 'end')
        text2.insert('end', translate_text)
    except Exception as e:
        text2.delete(1.0, 'end')
        text2.insert('end', 'Error: An error occurred.\nPlease check your internet connection and try again.')


# Languages
language = googletrans.LANGUAGES
lang_val = list(language.values())

# First combobox
combo1 = ttkb.Combobox(root, values=lang_val, font='Roboto 14', state='r')
combo1.place(x=110, y=20)
combo1.set('auto')

label1 = ttkb.Label(root, text='ENGLISH', font='segoe 30 bold', background='white', width=14, border=5, relief='groove')
label1.place(x=50, y=70)

# Middle text
ttkb.Label(root, text='TO', font='segoe 30 bold').place(x=470, y=70)

# Second combobox
combo2 = ttkb.Combobox(root, values=lang_val, font='Roboto 14', state='r')
combo2.place(x=610, y=20)
combo2.set('bangla')

label2 = ttkb.Label(root, text='ENGLISH', font='segoe 30 bold', background='white', width=14, border=5, relief='groove')
label2.place(x=550, y=70)

# First frame for input and output
f1 = ttkb.Frame(root, borderwidth=5)
f1.place(x=45, y=150, width=410, height=210)

text1 = ttkb.Text(f1, font='Roboto 16', relief='groove', wrap='word')
text1.place(x=0, y=0, width=400, height=200)

# Second frame for input and output
f2 = ttkb.Frame(root, borderwidth=5)
f2.place(x=545, y=150, width=410, height=210)

text2 = ttkb.Text(f2, font='Roboto 16', relief='groove', wrap='word')
text2.place(x=0, y=0, width=400, height=200)

# Translate button
btn = ttkb.Button(root, text='Translate', cursor='hand2', bootstyle='primary', command=translate_now)
btn.place(x=457, y=350)

label_change()

root.mainloop()
