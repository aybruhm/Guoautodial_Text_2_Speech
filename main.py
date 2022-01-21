from gtts import gTTS

"""
LOCALISED ACCENTS: 

For a given language, Google Translate text-to-speech can speak in different 
local `accents` depending on the Google domain (google.<tld>) of the request, 
with some examples shown in the table below.

-----------------------------------------------------------------------------
| Local accent           | Language code (lang) | Top-level domain (tdl)    |
| ---------------------------------------------------------------------------
| English (Austrailia)   | en                   | com.au                    |
| English (UK)           | en                   | co.uk                     |
| English (US)           | en                   | com (default)             |
| English (Canada)       | en                   | ca                        |
| English (India)        | en                   | co.in                     |
| English (Ireland)      | en                   | ie                        |
| English (South Africa) | en                   | co.za                     |
| French (Canada)        | fr                   | ca                        |
| French(France)         | fr                   | fr                        |
| Mandarin (China)       | zh-CN                | any                       |
| Mandarin (Taiwan)      | zh-TW                | any                       |
| Portuguese (Brazil)    | pt                   | com.br                    |
| Portuguese (Portugal)  | pt                   | pt                        |
| Spanish (Mexico)       | es                   | com.mx                    |
| Spanish (Spain)        | es                   | es                        |
| Spanish (US)           | es                   | com                       |
| Italy                  | it                   |                           y|
----------------------------------------------------------------------------
"""

# Opens path to text that will be translated
file = open("translate_text.txt", "r")

# Replave any new line to empty whitespace
text = file.read().replace("\n", "")

# Set a language for the voice assistance to be read in
language = "it"

# Set a top level domain to know which country accent you want
# top_level_domain = "co.uk"

# Initiate the Class, and passed arguments
output = gTTS(
    text=text, lang=language,
    # tld=top_level_domain
)

# Save the conversion to a mp3 file
output.save("output.mp3")

# Close the file
file.close()

# Print out to terminal console
print("======== TEXT CONVERTED TO AUDIO ========")