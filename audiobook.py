# python3
# espeak package for linux
# pyttsx3 to do the translation
# gtts and playsound for online aids

import pyttsx3, gtts, os
from playsound import playsound

languages = ['sw', 'en']
choice = input("chose a language: \n sw - Kiswahili \n en - English \n")

if choice in languages:
    if choice == 'en':
        engine = pyttsx3.init()
        engine.setProperty('voice', voices[1].id)

        engine.say("Hello Daniel How are you")
        engine.runAndWait()

    elif choice == 'sw':
        text2speech = gtts.gTTS("Habari yako Dan, umeshinda aje?", lang= "sw")

        text2speech.save("swa.mp3")

        os.system("vlc -R swa.mp3")

        # speaker.runAndWait()
else:
    text2speech = gtts.gTTS("I will add that language when i feel like it", lang= "en")

    text2speech.save("sass.mp3")

    os.system("vlc -R sass.mp3")
