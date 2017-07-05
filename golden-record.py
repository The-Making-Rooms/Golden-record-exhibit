from gpiozero import Button
import pygame.mixer
from pygame.mixer import Sound
from signal import pause

pygame.mixer.init()

sound_pins = {
    2: Sound("LANGUAGES/akkadian"),
    3: Sound("LANGUAGES/amoy"),
}

buttons = [Button(pin) for pin in sound_pins]
for button in buttons:
    sound = sound_pins[button.pin.number]
    button.when_pressed = sound.play

pause()

# Adapted from: https://www.raspberrypi.org/learning/gpio-music-box/ under Creative Commons licence.