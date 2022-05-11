import tkinter as tk
from model import *
import time
from datetime import datetime

import model

# Main window
main = None


class Window(tk.Frame):
    def play(self):
        icon = tk.PhotoImage(file='assets/pause.png')
        self.button.config(image=icon)
        self.button.image = icon
        self.button.config(command=self.pause)
        self.start_timer() if (time.time() -
                               self.timestamp) <= 0 else self.resume()

    def resume(self):
        self.timestamp = time.time() - self.timeElapsed
        self.loop()

    def replay(self):
        self.timeElapsed = 0
        self.text.config(text=format_time(self.timeElapsed))
        self.isPlaying = False
        icon = tk.PhotoImage(file='assets/play.png')
        self.button.config(image=icon)
        self.button.image = icon
        self.button.config(command=self.play)

    def pause(self):
        icon = tk.PhotoImage(file='assets/play.png')
        self.button.config(image=icon)
        self.button.image = icon
        self.button.config(command=self.play)
        self.isPlaying = False
        self.timeElapsed = (time.time() - self.timestamp)

    def start_timer(self):
        self.timestamp = time.time()
        self.loop()

    def loop(self):
        self.isPlaying = True
        while self.isPlaying:
            self.text.config(text=format_time((time.time() - self.timestamp)))
            self.update()

    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width) / self.width
        hscale = float(event.height) / self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0, 0, wscale, hscale)

    def __init__(self, parent):
        super(Window, self).__init__(parent)

        self.text = tk.Label(self, text=format_time(0), font=("Helvetica", 28))

        # Play/pause
        icon = tk.PhotoImage(file='assets/play.png')
        self.button = tk.Button(
            root,
            image=icon,
            width=50,
            height=50,
            # relief=tk.FLAT,
            command=self.play)
        self.button.image = icon

        # Restart
        icon2 = tk.PhotoImage(file='assets/replay.png')
        self.button2 = tk.Button(
            root,
            image=icon2,
            width=50,
            height=50,
            # relief=tk.FLAT,
            command=self.replay)
        self.button2.image = icon2

        self.button.pack(side=tk.RIGHT)
        self.button2.pack(side=tk.LEFT)
        self.text.pack(ipadx=10, ipady=10)

        self.isPlaying = False

        # Timestamp for stopwatch
        self.timestamp = time.time()
        self.timeElapsed = 0


if __name__ == "__main__":
    # Create an instance of tkinter
    root = tk.Tk()

    # Create the main window
    main = Window(root)

    # Fill the window with content
    main.pack(fill="both", expand=True)

    #Makes it so you can't resize it
    root.resizable(False, False)

    # Set window title
    root.title("Stopwatch")

    # Display the window
    root.mainloop()