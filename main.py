import tkinter as tk
from tkinter import messagebox
from converter import EmojiConverter
from gui import EmojiConverterGUI

def main():
    try:
        # Initialize backend converter engine
        converter = EmojiConverter("emojis.json")
    except Exception as e:
        # Handle initialization errors gracefully before launching GUI
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Startup Error", str(e))
        return

    # Launch GUI with injected converter engine
    root = tk.Tk()
    app = EmojiConverterGUI(root, converter)
    root.mainloop()

if __name__ == "__main__":
    main()