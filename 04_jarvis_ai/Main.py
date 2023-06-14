from jarvis import*

def main():
    #speak('jarvis is a ai module')
    wishme()
    while True:
        take_query = takecommand().lower()

        if 'wikipedia' in take_query:
            speak('Searching wikipedia...')
            take_query = take_query.replace('wikipedia', '')
            result = wikipedia.summary(take_query, sentences=2)
            speak('According to wikipedia')
            print(result)
            speak(result)
            
        elif 'open youtube' in take_query:
            webbrowser.open('youtube.com')

        elif 'open google' in take_query:
            webbrowser.open('google.com')

        elif 'open facebook' in take_query:
            webbrowser.open('facebook.com')

        elif 'open instagram' in take_query:
            webbrowser.open('instagram.com')

        elif 'open twitter' in take_query:
            webbrowser.open('twitter.com')

        elif 'open linkedin' in take_query:
            webbrowser.open('linkedin.com')

        elif 'open messenger' in take_query:
            webbrowser.open('messenger.com')

        elif 'open whatsapp' in take_query:
            webbrowser.open('whatsapp.com')

        elif 'open blogger' in take_query:
            webbrowser.open('blogger.com')

        elif 'play music' in take_query:
            # local drive path

            # music_drive = "D\\drive\\path"   
            # result = os.listdir(music_drive)
            # print(result)
            # os.startfile(os.path.join(music_drive, result[0]))

            # website link
            webbrowser.open('jango.com')

        elif 'the time' in take_query:
            start_time = datetime.now().strftime('%H: %M: %S')
            cur_date = date.today()
            day_of_week = cur_date.weekday()
            dayy = cur_date.strftime('%D')
            month = cur_date.strftime('%B')
            speak(f'sir, the time is {start_time}') 
            speak(f'and today is {cur_date}')
            speak(f'and week day {day_of_week}')
            speak(f'and today is {dayy}')
            speak(f'and the month is {month}')

        elif 'open code' in take_query:
            vs_code_path = '"C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(vs_code_path)

        elif 'open email' in take_query:
            webbrowser.open('gmail.com')

        elif 'email to sagar' in take_query:

            try:
                speak('what should i say!')
                contant = takecommand()
                to = 'mdsagorluc@gmail.com'
                send_email(to, contant)
                speak('Email has been send!')
            except Exception as e:
                print(e)
                speak('sorry sagar i am not able to send this email')

        elif 'break' in take_query:
            break
        


if __name__ == '__main__':
    main()