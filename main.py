from gtts import gTTS
import os

# Opens path to text that will be translated
file = open("translate_text.txt", "r")

# Replave any new line to empty whitespace
text = file.read().replace("\n", "")

# Set a language for the voice assistance to be read in
language = "en"

# Initiate the Class, and passed arguments
output = gTTS(
    text=text, lang=language,
    slow=False
)

# Save the conversion to a mp3 file
output.save("output.mp3")

# Close the file
file.close()

# Open your system default audio player to listen to the mp3 file
os.system("start output.mp3")