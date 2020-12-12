import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
#import PyAudio




#ignore any warning
warnings.filterwarnings("ignore")

#record audio and return as string

def recordaudio():
    #record the audio
    r=sr.Recognizer() #recognizer object

    #open mic and recording
    with sr.Microphone() as source:
        print("Say Something:")
        audio=r.listen(source)

    #use google speech recognizition
    data=''
    try:
        data=r.recognize_google(audio)
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I could not understand your voice")
    except sr.RequestError as e:
        print("Request result from google speech recognization service error"+e)
    return data
#recordaudio()

#virtual assistant response
def AssistantResponse(text):
    print(text)

    #convert text to speech
    myobj=gTTS(text=text,lang="en",slow=False)

    #save converted audio file
    myobj.save("Assistant_Response.mp3")

    #play converted mp3
    os.system('start Assistant_Response.mp3')
#A function for wake words
def wakeWord(text):
    wake_word=['hey computer','alright riya','ok baby']
    text=text.lower()
    #check to see if the user text contain a wake word
    for phrase in wake_word:
        if phrase in text:
            return True
    return False

#function for get date

def getdate():
    now=datetime.datetime.now()
    my_date=datetime.datetime.today()
    weekday=calendar.day_name[my_date.weekday()]
    monthNum=now.month
    dayNum=now.day

    #list of month
    month_names=['January','February','March','April','May','June','July','August','September','October','November','December']

    #list of ordinal number
    ordinalNumbers=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th',
                    '16th','17th','18th','19yh','20th','21st','22nd','23rd','24th','25th','26th','27th','28th',
                    '29th','30th','31st']
    return 'Today is '+weekday+', the '+ordinalNumbers[dayNum-1]+' ' +month_names[monthNum-1]+'.'
#print(getdate())


#A function for greetings
def greeting(text):
    Greeting_Input=['hi','hey','hola']
    Greeting_Response=['hello','hey there','whats good']

    #if the users input is a greeting,then return a randomly chossen greeting response
    for word in text.split():
        if word.lower() in Greeting_Input:
            return random.choice(Greeting_Response)+'.'

    return ''

#A function to get a persons first & last name
def getPerson(text):
    wordList=text.split()

    for i in range(0,len(wordList)):
        if i+3<=len(wordList)-1 and wordList[i].lower()=="who"and wordList[i+1].lower()=="is":
            return wordList[i+2]+' '+wordList[i+3]


while True:
    text=recordaudio()
    response=''

    #check wake word

    if(wakeWord(text)==True):
        #check gor greetingd
        response = response + greeting(text)

        # check comment
        if ('date' in text):
            get_date = getdate()
            response = response + ' ' + get_date
        # check who is
        if ('who is' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response + ' ' + wiki

        # response back audio
        AssistantResponse(response)
