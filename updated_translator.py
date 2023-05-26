import ttkbootstrap as ttkb
import random
import googletrans
import webbrowser
from googletrans import Translator
from tkinter import messagebox

theme_list = ['litera', 'minty', 'lumen', 'sandstone', 'yeti', 'pulse', 'united', 'morph', 'journal', 'darkly', 'superhero', 'solar', 'cyborg', 'vapor', 'simplex', 'cerculean']

theme = 'litera'
root = ttkb.Window(themename=theme)
root.title('Easy Python Translator')
root.geometry('1080x500')
root.resizable(False, False)


def change_show():
    c1 = combo1.get()
    c2 = combo2.get()
    label1['text'] = c1
    label2['text'] = c2
    root.after(1000, change_show)


def translate_now():
    try:
        get_text = text1.get(1.0, 'end')
        t1 = Translator()  # this instance is very important to translate otherwise we got error
        translate_text = t1.translate(
            get_text, src=combo1.get(), dest=combo2.get())
        translate_text = translate_text.text

        text2.delete(1.0, 'end')
        text2.insert('end', translate_text)

    except Exception as e:
        text2.delete(1.0, 'end')
        text2.insert(
            'end', 'Error: An error occurred.\n\nPlease check your internet connection and try again.')


def change_theme(theme_name):
    global theme
    theme = theme_name
    root = ttkb.Window(themename=theme)
    root.destroy()
    return root


def randomtheme():
    global theme_list, theme
    theme = random.choice(theme_list)
    
    change_theme(theme)


def help_menu():
    messagebox.showinfo(
        'Help', "How it's work?\nThis is a simple translator, you need to connect wifi or mobile data to translate any language.")


def source_code():
    m = messagebox.askokcancel('Source Code', "Click 'Ok' to get source code.")

    if m:    # m return boolean value- True, False
        webbrowser.open(
            'https://github.com/mdshakib007/Python-Translator/blob/master/translator.py')
    else:
        pass


def about():
    messagebox.showinfo(
        'About', "This is jsut a simple project of tkinter GUI, made by @Md_Shakib_Ahmed.")


############ menubar to change themes ##################
main_menu = ttkb.Menu(root)
m1 = ttkb.Menu(main_menu, tearoff=0)
theme_menu = ttkb.Menu(m1, tearoff=0)

theme_menu.add_command(label='Random Theme', command=lambda: randomtheme())
theme_menu.add_command(label='Litera', accelerator='Default',
                       command=lambda: change_theme('litera'))
theme_menu.add_command(label='Minty', command=lambda: change_theme('minty'))
theme_menu.add_command(label='Lumen', command=lambda: change_theme('lumen'))
theme_menu.add_command(
    label='Sandstone', command=lambda: change_theme('sandstone'))
theme_menu.add_command(label='Yeti', command=lambda: change_theme('yeti'))
theme_menu.add_command(label='Pulse', command=lambda: change_theme('pulse'))
theme_menu.add_command(label='United', command=lambda: change_theme('united'))
theme_menu.add_command(label='Morph', accelerator='Simple', command=lambda: change_theme('morph'))
theme_menu.add_command(
    label='Journal', command=lambda: change_theme('journal'))
theme_menu.add_separator()
theme_menu.add_command(label='Darkly', accelerator='Dark',
                       command=lambda: change_theme('darkly'))
theme_menu.add_command(
    label='Superhero', command=lambda: change_theme('superhero'))
theme_menu.add_command(label='Solar', command=lambda: change_theme('solar'))
theme_menu.add_command(label='Cyborg', command=lambda: change_theme('cyborg'))
theme_menu.add_command(label='Vapor', command=lambda: change_theme('vapor'))
theme_menu.add_command(
    label='Simplex', command=lambda: change_theme('simplex'))
theme_menu.add_command(
    label='Cerculean', command=lambda: change_theme('cerculean'))

m1.add_cascade(label='Themes', menu=theme_menu)

m1.add_command(label='Help', command=help_menu)
m1.add_command(label='Source Code', command=source_code)
m1.add_command(label='About', command=about)
m1.add_command(label='Exit', accelerator='Ctrl+Q', command=quit)

main_menu.add_cascade(label='View', menu=m1, font='Roboto 13')
root.config(menu=main_menu)


# all languages
lang = googletrans.LANGUAGES
lang_value = list(lang.values())


####### first combobox, label and frame text for output #######
combo1 = ttkb.Combobox(root, values=lang_value, font='Roboto 14', state='r')
combo1.place(x=110, y=20)
combo1.set('auto')

label1 = ttkb.Label(root, font='Roboto 30 bold',
                    background='white', width=14, border=5, relief='groove')
label1.place(x=50, y=70)

frame1 = ttkb.Frame(root, borderwidth=5)
frame1.place(x=45, y=150, width=410, height=210)

text1 = ttkb.Text(frame1, font='Roboto 16', relief='groove', wrap='word')
text1.place(x=0, y=0, width=400, height=200)


########## middle text ########
ttkb.Label(root, text='TO', font='Roboto 30').place(x=470, y=70)


####### first combobox, label and frame text for output #######
combo2 = ttkb.Combobox(root, values=lang_value, font='Roboto 14', state='r')
combo2.place(x=610, y=20)
combo2.set('bangla')

label2 = ttkb.Label(root, font='Roboto 30 bold',
                    background='white', width=14, border=5, relief='groove')
label2.place(x=550, y=70)

frame2 = ttkb.Frame(root, borderwidth=5)
frame2.place(x=545, y=150, width=410, height=210)

text2 = ttkb.Text(frame2, font='Roboto 16', relief='groove', wrap='word')
text2.place(x=0, y=0, width=400, height=200)


### button for translate ###
btn = ttkb.Button(root, text='Translate', cursor='hand2',
                  command=translate_now, bootstyle='-outline')
btn.place(x=457, y=400)


# call the function
change_show()

root.mainloop()
