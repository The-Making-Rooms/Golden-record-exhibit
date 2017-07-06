import RPi.GPIO as GPIO
import pygame.mixer

GPIO.setmode(GPIO.BCM)

GPIO.setup(2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(14,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)

pygame.mixer.init(8000)

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

while True:
	for pin in sound_pins:
		if GPIO.input(pin)==GPIO.LOW:
			pygame.mixer.music.load(sound_pins[pin])
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy() == True:
				continue
			while GPIO.input(pin) == GPIO.LOW:
				continue
