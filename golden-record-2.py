from gpiozero import Button
import pygame.mixer as mixer
from pygame.mixer import Sound

#from pygame.mixer import Music
from signal import pause

mixer.init(8000)

def play_language(r_sound):
	mixer.music.load(r_sound)
	mixer.music.play()
	

sound_pins = {
    2: "LANGUAGES/WAV/japanese.wav",
    3: "LANGUAGES/WAV/welsh.wav",
    4: "LANGUAGES/WAV/hindi.wav",
    14: "LANGUAGES/WAV/english.wav",
    15: "LANGUAGES/WAV/spanish.wav",
    18: "LANGUAGES/WAV/cantonese.wav",
    17: "LANGUAGES/WAV/italian.wav",
    27: "LANGUAGES/WAV/arabic.wav",
    22: "LANGUAGES/WAV/german.wav",
    23: "LANGUAGES/WAV/french.wav",
}

buttons = [Button(pin) for pin in sound_pins]
for button in buttons:
    sound = sound_pins[button.pin.number]
    button.when_pressed = play_language(sound)

pause()

# Adapted from: https://www.raspberrypi.org/learning/gpio-music-box/ under Creative Commons licence.

