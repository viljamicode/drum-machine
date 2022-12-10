import tkinter as tk
from tkinter import *
import pygame

# Initialize Pygame and the mixer
pygame.init()
pygame.mixer.init()

# Load the sounds
kick = pygame.mixer.Sound('kick.wav')
snare = pygame.mixer.Sound('snare.wav')
hihat = pygame.mixer.Sound('hihat.wav')

# Create the GUI
root = tk.Tk()
root.title('Drum Machine')


def key_pressed(event):             # Handle keyboard events
    if event.char == 'h':           # Handle keyboard events
        hihat.play()                # Handle keyboard events
    elif event.char == 'k':         # Handle keyboard events
        kick.play()                 # Handle keyboard events
    elif event.char == 's':         # Handle keyboard events
        snare.play()                # Handle keyboard events


root.bind('<Key>', key_pressed)     # Handle keyboard events

# Load the images
kick_img = tk.PhotoImage(file='kick.png')
snare_img = tk.PhotoImage(file='snare.png')
hihat_img = tk.PhotoImage(file='hihat.png')

# Create the buttons
tk.Button(root, image=snare_img,
          command=lambda: snare.play()).pack(side=tk.LEFT)
tk.Button(root, image=hihat_img, command=lambda: hihat.play()).pack()
tk.Button(root, image=kick_img, command=lambda: kick.play()).pack(side=tk.RIGHT)

# Start the GUI event loop
root.mainloop()
