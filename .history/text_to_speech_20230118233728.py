from gtts import gTTS
import os
import sys
module_path = os.path.abspath(os.getcwd() + '\\..')
if module_path not in sys.path:
    sys.path.append(module_path)
# Import the required module for text 
# to speech conversion

# This module is imported so that we can 
# play the converted audio
# The text that you want to convert to audio


def main(argv):
    mytext = sys.argv[0]

    # Language in which you want to convert
    language = 'pt'

    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save(f"{sys.argv[1]}.mp3")
    # Playing the converted file


if __name__ == '__main__':
    sys.argv = "Atenção"
    main(sys.argv)
