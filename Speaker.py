import pyttsx3

speaker = pyttsx3.init()
voices = speaker.getProperty('voices')

# Задать голос по умолчанию
speaker.setProperty('voice', 'ru') 

# Попробовать установить предпочтительный голос
#for voice in voices:
#    if voice.name == 'Aleksandr':
#        speaker.setProperty('voice', voice.id)

speaker.say('Здравствуйте!!!')
speaker.save_to_file('Здравствуйте!!!', 'test.mp3')
speaker.runAndWait()
