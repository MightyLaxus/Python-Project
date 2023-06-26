import tkinter as tk
import time
import threading

class AutoTyperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AutoTyper")
        self.text = tk.StringVar()
        self.interval = tk.DoubleVar()
        self.is_running = False
        self.thread = None
        
        self.create_widgets()

    def create_widgets(self):
        # Text Entry
        text_label = tk.Label(self.root, text="Text to type:")
        text_label.pack()
        text_entry = tk.Entry(self.root, textvariable=self.text)
        text_entry.pack()

        # Interval Entry
        interval_label = tk.Label(self.root, text="Interval (in seconds):")
        interval_label.pack()
        interval_entry = tk.Entry(self.root, textvariable=self.interval)
        interval_entry.pack()

        # Start Button
        start_button = tk.Button(self.root, text="Start", command=self.start_typing)
        start_button.pack()

        # Stop Button
        stop_button = tk.Button(self.root, text="Stop", command=self.stop_typing)
        stop_button.pack()

    def start_typing(self):
        if self.is_running:
            return

        self.is_running = True
        self.thread = threading.Thread(target=self.type_text)
        self.thread.start()

    def stop_typing(self):
        self.is_running = False

    def type_text(self):
        while self.is_running:
            current_text = self.text.get()
            current_interval = self.interval.get()

            for char in current_text:
                if not self.is_running:
                    return

                time.sleep(current_interval)
                self.press_key(char)

    def press_key(self, char):
        # Replace this with the logic to actually press the key in your target application
        print("Typing:", char)

if __name__ == '__main__':
    root = tk.Tk()
    app = AutoTyperGUI(root)
    root.mainloop()
