import tkinter as tk
from tkinter import messagebox
import random
import os

class JokeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Joke Telling Assistant")
        self.root.geometry("400x300")
        
        # Load jokes from file
        self.jokes = self.load_jokes()
        if not self.jokes:
            messagebox.showerror("Error", "randomJokes.txt not found or empty in the resources folder.")
            self.root.quit()
            return
        
        self.current_joke = None
        self.setup_shown = False
        self.punchline_shown = False
        
        # Initial button
        self.start_button = tk.Button(self.root, text="Alexa tell me a Joke", command=self.tell_joke, font=("Arial", 14))
        self.start_button.pack(pady=20)
        
        # Labels for joke
        self.setup_label = tk.Label(self.root, text="", font=("Arial", 12), wraplength=350)
        self.punchline_label = tk.Label(self.root, text="", font=("Arial", 12), wraplength=350, fg="blue")
        
        # Buttons
        self.show_punchline_button = tk.Button(self.root, text="Show Punchline", command=self.show_punchline, state=tk.DISABLED)
        self.next_joke_button = tk.Button(self.root, text="Next Joke", command=self.next_joke, state=tk.DISABLED)
        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit_app)
        
        self.quit_button.pack(side=tk.BOTTOM, pady=10)

    def load_jokes(self):
        file_path = os.path.join("resources", "randomJokes.txt")
        if not os.path.exists(file_path):
            return []
        with open(file_path, "r") as file:
            jokes = []
            for line in file:
                if "?" in line:
                    setup, punchline = line.split("?", 1)
                    jokes.append((setup.strip() + "?", punchline.strip()))
            return jokes

    def tell_joke(self):
        if not self.jokes:
            return
        self.current_joke = random.choice(self.jokes)
        self.setup_shown = True
        self.punchline_shown = False
        
        # Update UI
        self.start_button.pack_forget()
        self.setup_label.config(text=self.current_joke[0])
        self.setup_label.pack(pady=10)
        self.punchline_label.config(text="")
        self.punchline_label.pack_forget()
        
        self.show_punchline_button.config(state=tk.NORMAL)
        self.show_punchline_button.pack(pady=10)
        self.next_joke_button.config(state=tk.NORMAL)
        self.next_joke_button.pack(pady=10)

    def show_punchline(self):
        if self.current_joke and not self.punchline_shown:
            self.punchline_shown = True
            self.punchline_label.config(text=self.current_joke[1])
            self.punchline_label.pack(pady=10)
            self.show_punchline_button.config(state=tk.DISABLED)

    def next_joke(self):
        self.tell_joke()

    def quit_app(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = JokeApp(root)
    root.mainloop()
