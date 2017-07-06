from gpiozero import Button
import pygame.mixer
from pygame.mixer import Sound
#from pygame.mixer import Music
from signal import pause

pygame.mixer.init(8000)

sound_pins = {
    2: Music("LANGUAGES/WAV/japanese.wav"),
    3: Music("LANGUAGES/WAV/welsh.wav"),
    4: Music("LANGUAGES/WAV/hindi.wav"),
    14: Music("LANGUAGES/WAV/english.wav"),
    15: Music("LANGUAGES/WAV/spanish.wav"),
    18: Music("LANGUAGES/WAV/cantonese.wav"),
    17: Music("LANGUAGES/WAV/italian.wav"),
    27: Music("LANGUAGES/WAV/arabic.wav"),
    22: Music("LANGUAGES/WAV/german.wav"),
    23: Music("LANGUAGES/WAV/french.wav"),
}

buttons = [Button(pin) for pin in sound_pins]
for button in buttons:
    sound = sound_pins[button.pin.number]
    button.when_pressed = sound.play

pause()

# Adapted from: https://www.raspberrypi.org/learning/gpio-music-box/ under Creative Commons licence.
