import pyttsx3 # this module for voices
import speech_recognition as sr # this module for voice command
import wikipedia # this module for wikipedia story
import webbrowser # this is for open website browser
import os # this is for play any kind of music
import smtplib # this is for send email, gmail
from datetime import datetime, date # this is for date time set 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') # tow voice here male and female
#print(voices[0].id)
engine.setProperty('voice', voices[1].id) # set female voice
#engine.setProperty('voice', voices[0].id) # set male voice
#print(male_voice)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    houre = int(datetime.now().hour)
    
    if houre >=0 and houre < 12:
        speak("good morning sagar")
    elif houre >= 12 and houre < 18:
        speak("good afternoon sagar")
    elif houre >= 18 and houre < 20:
        speak("good evening sagar")
    else:
        speak("good night sagar")

    speak('hei!i am jarvis ai developer sagar ahmed here.how may i help you')

def takecommand():
    # it takes microphone speech and return the string output
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language="en-in")
        print(f'he/she said: {query}\n')

    except Exception as ex:
        #print(ex) # don't show the error 
        print('Please say that agin!')
        return 'None'
    return query

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() # build in function of smtplib
    server.starttls() # build in function of smtplib
    server.login('droptosagor@gmail.com', 'sagor102030')  # build in function of smtplib
    server.sendmail('mdsagorluc@gmail.com', to, content)  # build in function of smtplib
    server.close()

       





# if __name__ == '__main__':
#     speak("have a good time")
#     wishme()
