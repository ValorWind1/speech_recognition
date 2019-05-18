from gtts import gTTS

import os

print("write something:")
textinput=input()

languague = "en"

audio = gTTS(text=textinput,lang=languague,slow=False)

audio.save("audio.mp3")

os.system("audio.mp3")