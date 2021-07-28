import pyttsx3
 speaker = pyttsx3.init()
 speaker.setProperty('voice', 'ru')
 voices = speaker.getProperty('voices')
 for voice in voices:
     if voice.name =='Aleksandr':
         speaker.setProperty('voice', voice.id)

speaker.setProperty('rate', 200)
speaker.setProperty('volume', 100)
 speaker.say('Здравствуйте')
 speaker.runAndWait()
 speaker.save_to_file('Здравствуйте', 'hello.mp3')
