# gui.py
import tkinter as tk
from tkinter import messagebox

class EmojiConverterGUI:
    """Handles Tkinter visual components and user interaction."""

    def __init__(self, root, converter):
        self.root = root
        self.converter = converter

        self.root.title("Emoji to Text Converter")
        self.root.geometry("560x620")
        self.root.resizable(False, False)

        # Color Palette
        self.bg_color = "#f4f6f9"
        self.primary_color = "#2b5c8f"
        self.button_color = "#3b82f6"
        self.root.config(bg=self.bg_color)

        self.build_ui()

    def build_ui(self):
        # Header
        title_label = tk.Label(
            self.root, 
            text="Emoji to Text Converter", 
            font=("Helvetica", 16, "bold"), 
            bg=self.bg_color, 
            fg=self.primary_color
        )
        title_label.pack(pady=(15, 2))



        # Input Section
        tk.Label(
            self.root, 
            text="Input Text:", 
            font=("Helvetica", 10, "bold"), 
            bg=self.bg_color
        ).pack(anchor="w", padx=30)
        
        # Specified Segoe UI Emoji font for improved character resolution
        self.input_text = tk.Text(self.root, height=4, width=56, font=("Segoe UI Emoji", 11), wrap="word")
        self.input_text.pack(padx=30, pady=(5, 5))

        # --- EMOJI PALETTE (Quick Insert Buttons) ---
        palette_frame = tk.LabelFrame(
            self.root, 
            text=" Quick Insert Emojis ", 
            font=("Helvetica", 9, "bold"),
            bg=self.bg_color, 
            fg="#444444"
        )
        palette_frame.pack(padx=30, pady=5, fill="x")

        # Extract available emojis directly from converter map
        sample_emojis = list(self.converter.emoji_map.keys())[:10]
        
        for idx, emoji_char in enumerate(sample_emojis):
            btn = tk.Button(
                palette_frame, 
                text=emoji_char, 
                font=("Segoe UI Emoji", 12),
                width=3,
                command=lambda e=emoji_char: self.insert_emoji(e),
                bg="#ffffff",
                relief="groove"
            )
            btn.grid(row=idx // 5, column=idx % 5, padx=4, pady=4)

        # Action Buttons Frame
        btn_frame = tk.Frame(self.root, bg=self.bg_color)
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame, text="Convert Text", command=self.handle_convert, 
            bg=self.button_color, fg="white", font=("Helvetica", 10, "bold"),
            padx=15, pady=5, relief="flat", cursor="hand2"
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            btn_frame, text="Clear", command=self.handle_clear, 
            bg="#ef4444", fg="white", font=("Helvetica", 10, "bold"),
            padx=15, pady=5, relief="flat", cursor="hand2"
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            btn_frame, text="Copy Output", command=self.handle_copy, 
            bg="#10b981", fg="white", font=("Helvetica", 10, "bold"),
            padx=15, pady=5, relief="flat", cursor="hand2"
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            btn_frame, text="Plain Convert", command=self.handle_convert_without_brackets, 
            bg="#6b7280", fg="white", font=("Helvetica", 10, "bold"),
            padx=15, pady=5, relief="flat", cursor="hand2"
        ).grid(row=0, column=3, padx=5)

        # Output Section
        tk.Label(
            self.root, 
            text="Converted Output:", 
            font=("Helvetica", 10, "bold"), 
            bg=self.bg_color
        ).pack(anchor="w", padx=30, pady=(10, 0))
        
        self.output_text = tk.Text(
            self.root, height=4, width=56, font=("Helvetica", 11), 
            wrap="word", bg="#eef2f7"
        )
        self.output_text.pack(padx=30, pady=(5, 15))

    def insert_emoji(self, emoji_char):
        """Inserts selected emoji directly into the text field at cursor position."""
        self.input_text.insert(tk.INSERT, emoji_char)
        self.input_text.focus()

    def handle_convert(self):
        raw_text = self.input_text.get("1.0", tk.END).strip()
        if not raw_text:
            messagebox.showwarning("Empty Input", "Please enter some text containing emojis first!")
            return

        converted_result = self.converter.convert(raw_text)

        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, converted_result)

    def handle_convert_without_brackets(self):
        raw_text = self.input_text.get("1.0", tk.END).strip()
        if not raw_text:
            messagebox.showwarning("Empty Input", "Please enter some text containing emojis first!")
            return

        converted_result = self.converter.convert_without_brackets(raw_text)

        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, converted_result)

    def handle_clear(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)

    def handle_copy(self):
        output_data = self.output_text.get("1.0", tk.END).strip()
        if output_data:
            self.root.clipboard_clear()
            self.root.clipboard_append(output_data)
            messagebox.showinfo("Success", "Converted text copied to clipboard!")
        else:
            messagebox.showwarning("Empty Output", "There is no converted text to copy.")