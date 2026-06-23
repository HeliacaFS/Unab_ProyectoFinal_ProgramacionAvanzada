# app.py
import tkinter as tk
from ui.interfaz import Main

def main():
    root = tk.Tk()
    root.title("Sistema de Gestión de Biblioteca Digital")
    app = Main(root)
    root.mainloop()

if __name__ == "__main__":
    main()
