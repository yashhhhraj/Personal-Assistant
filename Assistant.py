import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)#0 for male voice
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')
    elif hour>=12 and hour<18:
        speak('Good Afternoon')
    else:
        speak('Good evening')
    speak('I am your personal assistant, please tell me how may I help you?')    

def takeCommand():
    '''
    it takes microphone input from the user and 
    returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print('Recognising...')
        query = r.recognize_google(audio,language = 'en-in' )
        print(f'User: {query}\n')

    except Exception as e:
        #print(e)
        print('Pardon, can you please repeat?')
        return 'None'
    return query

if __name__ == "__main__":
    wishme()
    takeCommand()
