import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("550x250")
        
        self.current_song = tk.StringVar()
        self.current_song.set("No song selected.")
        
        self.create_widgets()
        
        pygame.init()
        pygame.mixer.init()
        
    def create_widgets(self):
        self.style = ttk.Style(self.root)
        self.style.configure("TFrame", background="#000000")  # Set background color
        
        self.frame = ttk.Frame(self.root, style="TFrame")
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        self.song_label = ttk.Label(self.frame, textvariable=self.current_song)
        self.song_label.pack(pady=10)
    
        
        self.select_button = ttk.Button(self.frame, text="Select Song", command=self.select_song)
        self.select_button.pack(pady=15)
        
        self.play_button = ttk.Button(self.frame, text="Play", command=self.play_song)
        self.play_button.pack(pady=15)
        
        self.stop_button = ttk.Button(self.frame, text="Stop", command=self.stop_song)
        self.stop_button.pack(pady=15)
        
    def select_song(self):
        song_path = filedialog.askopenfilename(initialdir="/", title="Select a Song",
                                               filetypes=(("MP3 Files", "*.mp3"), ("All Files", "*.*")))
        if song_path:
            self.current_song.set(song_path)
            
    def play_song(self):
        song_path = self.current_song.get()
        if song_path:
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
        
    def stop_song(self):
        pygame.mixer.music.stop()
        
if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
