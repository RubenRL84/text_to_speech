import sys
from gtts import gTTS
import os

sys.path.append("/absolute/module/path")
# Import the required module for text 
# to speech conversion


# This module is imported so that we can 
# play the converted audio
# The text that you want to convert to audio

if __name__ == '__main__':

    with open("Text.txt", "r", encoding="utf-8") as f:
        contents = f.read()
        print(contents)
    mytext = contents

    # Language in which you want to convert
    language = 'pt'

    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save("audio.mp3")
    # Playing the converted file
