from tkinter import *
import datetime
from playsound import playsound

root = Tk()
root.geometry('500x300')


def alarme():
    fixar_tempo_alarme = f'{hora.get()}:{minuto.get()}:{segundo.get()}'
    tempo_atual = datetime.datetime.now().strftime('%H:%M:%S')
    if tempo_atual == fixar_tempo_alarme:
        print('Alarme ativado')
        playsound('alarme.mp3')
    else:
        print('O alarme foi definido para:', fixar_tempo_alarme)


def update_clock():
    tempo_atual = datetime.datetime.now().strftime('%H:%M:%S')
    clock_label.config(text=tempo_atual)

    fixar_tempo_alarme = f'{hora.get()}:{minuto.get()}:{segundo.get()}'

    if tempo_atual == fixar_tempo_alarme:
        alarme()

    root.after(1000, update_clock)


root.configure(bg='pink')
root.resizable(False, False)
root.title('Alarme')

clock_label = Label(root, text='', font=('Arial', 36), fg='deep pink', bg='pink')
clock_label.pack(pady=20)

frame = Frame(root, bg='pink')
frame.pack()

Label(frame, text='Hora:', font=('Arial', 12), fg='deep pink', bg='pink').pack(side=LEFT)
hora = StringVar(root)
horas = [str(i).zfill(2) for i in range(24)]
hora.set(horas[0])
h = OptionMenu(frame, hora, *horas)
h.pack(side=LEFT)

Label(frame, text='Minuto:', font=('Arial', 12), fg='deep pink', bg='pink').pack(side=LEFT)
minuto = StringVar(root)
minutos = [str(i).zfill(2) for i in range(60)]
minuto.set(minutos[0])
m = OptionMenu(frame, minuto, *minutos)
m.pack(side=LEFT)

Label(frame, text='Segundo:', font=('Arial', 12), fg='deep pink', bg='pink').pack(side=LEFT)
segundo = StringVar(root)
segundos = [str(i).zfill(2) for i in range(60)]
segundo.set(segundos[0])
s = OptionMenu(frame, segundo, *segundos)
s.pack(side=LEFT)

confirm_button = Button(root, text='Confirmar', font=('Arial', 12), fg='white', bg='deep pink', command=alarme)
confirm_button.pack(pady=20)

update_clock()

root.mainloop()
