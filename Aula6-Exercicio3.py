import tkinter as tk
import time

def relogio():
    tempo = time.strftime("%H:%M:%S") # Obtém a hora atual
    label.config(text=tempo) # Atualiza o label do relógio
    master.after(1000, relogio) # Aguarda um segundo antes de atualizar novamente

# Cria a frame com a label organizado num bloco
master = tk.Tk()
master.title("Relógio Digital")

label = tk.Label(master, font=("arial", 100))
label.pack()

relogio()

master.mainloop()

