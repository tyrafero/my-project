from gtts import gTTS
from playsound import playsound

# Function to convert text to voice
def text_to_speech(text, filename):
    tts = gTTS(text)
    tts.save(filename)
    playsound(filename)

# Example usage
num = 5
text = f'{num} completed'
filename = "output.mp3"
text_to_speech(text, filename)