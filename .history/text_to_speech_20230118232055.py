import sys
# Import the required module for text 
# to speech conversion
from gtts import gTTS

# This module is imported so that we can 
# play the converted audio
import os
# The text that you want to convert to audio


def main(args):
    mytext = sys.args[0]

    # Language in which you want to convert
    language = 'pt'

    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save(f"{sys.args[1]}.mp3")
    # Playing the converted file


if __name__ == '__main__':
    main(sys.args)
