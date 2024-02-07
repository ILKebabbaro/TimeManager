# Import delle librerie tkinter per la creazione dell'interfaccia grafica
import tkinter as tk
from tkinter import ttk

# Creazione della finestra principale
windows = tk.Tk()
windows.title("Timer Manager")  # Titolo della finestra
windows.geometry("600x600")  # Dimensioni della finestra
windows.resizable(True, True)  # Reizzabilità della finestra
windows.configure(bg="#2E4057")  # Colore di sfondo della finestra

# Creazione etichetta per chiedere all'utente di inserire il tipo di programma
label = ttk.Label(windows, text="Inserisci il tipo di programma", font=("Lato", 14), background="#2E4057", foreground="#FFFFFF")
label.place(x=20, y=30)  # Posizionamento dell'etichetta nella finestra

# Creazione della casella combinata per la selezione del tipo di programma
combobox = ttk.Combobox(windows, font=("Lato", 14), values=["Weekend","Weekend con sorvegliante", "Infrasettimanale", "Infrasettimanale con sorvegliante"], state="readonly")
combobox.place(x=20, y=60)  # Posizionamento della casella combinata nella finestra
combobox.current(0)  # Impostazione del valore predefinito

windows.mainloop()  # Avvio del loop principale per mostrare la finestra e gestire gli eventi
