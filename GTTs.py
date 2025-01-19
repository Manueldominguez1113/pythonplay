from gtts import gTTS

text_to_say = "this will be read by google text to speech"
language = "en"

tts = gTTS(text=text_to_say, lang=language)
path = "output/test.mp3"
tts.save(path)
