import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import pyttsx3

class LanguageTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")
        self.root.geometry("800x600")

        self.translator = Translator()
        self.engine = pyttsx3.init()

        self.from_language = tk.StringVar()
        self.to_language = tk.StringVar()

        self.language_data = LANGUAGES
        self.language_values = list(self.language_data.values())
        self.languages = list(self.language_values)

        self.from_language.set(self.languages[0])
        self.to_language.set(self.languages[21])

        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        self.logo_label = tk.Label(self.root, text="Language Translator", font=("Arial", 24))
        self.canvas.create_window(400, 50, window=self.logo_label)

        self.from_language_label = tk.Label(self.root, text="From Language:")
        self.canvas.create_window(150, 100, window=self.from_language_label)

        self.from_language_combobox = ttk.Combobox(self.root, width=36, values=self.languages)
        self.from_language_combobox.current(0)
        self.canvas.create_window(300, 100, window=self.from_language_combobox)

        self.to_language_label = tk.Label(self.root, text="To Language:")
        self.canvas.create_window(150, 150, window=self.to_language_label)

        self.to_language_combobox = ttk.Combobox(self.root, width=36, values=self.languages)
        self.to_language_combobox.current(21)
        self.canvas.create_window(300, 150, window=self.to_language_combobox)

        self.from_text = tk.Text(self.root, width=50, height=10)
        self.canvas.create_window(400, 250, window=self.from_text)

        self.translate_button = tk.Button(self.root, text="Translate", command=self.translate)
        self.canvas.create_window(400, 350, window=self.translate_button)

        self.to_text = tk.Text(self.root, width=50, height=10)
        self.canvas.create_window(400, 450, window=self.to_text)

        self.speak_button = tk.Button(self.root, text="Speak", command=self.speak)
        self.canvas.create_window(400, 550, window=self.speak_button)

    def translate(self):
        try:
            self.source_language = self.from_language_combobox.get()
            self.destination_language = self.to_language_combobox.get()
            self.text = self.from_text.get(1.0, tk.END)
            self.translation = self.translator.translate(self.text, src=self.source_language, dest=self.destination_language)
            self.to_text.delete(1.0, tk.END)
            self.to_text.insert(tk.END, self.translation.text)
        except TypeError as e:
            print("Invalid input")

    def speak(self):
        self.engine.say(self.to_text.get(1.0, tk.END))
        self.engine.runAndWait()

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslator(root)
    root.mainloop()