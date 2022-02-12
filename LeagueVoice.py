
import speech_recognition as sr
import numpy as np
import sounddevice as sd
import wave
import keyboard
import pyautogui as pag
from googletrans import Translator
from time import sleep
import os
os.system("cls") 


COLORS = {\
"magenta":"\u001b[35m",
}

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

while True: 
    r = """ [[magenta]] (                                                  
 )\ )                                               
(()/(   (    ) (  (    (    (  (   (   (        (   
 /(_)) ))\( /( )\))(  ))\  ))\ )\  )\( )\  (   ))\  
(_))  /((_)(_)|(_))\ /((_)/((_|(_)((_)((_) )\ /((_) 
| |  (_))((_)_ (()(_|_))((_)) \ \ / ((_|_)((_|_))   
| |__/ -_) _` / _` || || / -_) \ V / _ \ / _|/ -_)  
|____\___\__,_\__, | \_,_\___|  \_/\___/_\__|\___|  
              |___/                                 """

    print(colorText(r))
    t0 = '[[magenta]]Starting... y/n'
    query = input(colorText(t0)) 
    Fl = query[0].lower() 
    if query == '' or not Fl in ['y','n']: 
       t1 = "[[magenta]]Please answer with yes or no!"
       print(colorText(t1))
    else: 
       break 

if Fl == 'y': 
    clear = lambda: os.system('cls')
    clear()
    t2 = f"[[magenta]]Started successfully.\nPress Y to record."
    print(colorText(t2))
    FILE_NAME = './sound.wav'  
    wave_length = 4 
    sample_rate = 16_000  
    while True:
        keyboard.wait('y')
        t3 = "[[magenta]]RECORDING..."
        print(colorText(t3))
        data = sd.rec(int(wave_length * sample_rate), sample_rate, channels=1)
        sd.wait()
    
        data = data / data.max() * np.iinfo(np.int16).max
    
        data = data.astype(np.int16)
    
        with wave.open(FILE_NAME, mode='wb') as wb:
            wb.setnchannels(1)  #monaural
            wb.setsampwidth(2)  # 16bit=2byte
            wb.setframerate(sample_rate)
            wb.writeframes(data.tobytes())  #Convert to byte string
        
        
    
    
        filename = "sound.wav"
        r = sr.Recognizer()
    
        with sr.AudioFile(filename) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data, language="de-DE")
            t4 = "[[magenta]]Erkannter Text: " + text
            print(colorText(t4))
            translator = Translator()
            result = translator.translate(text, src='de', dest='en')
            t5 = "[[magenta]]Übersetzter Text: " + result.text
            print(colorText(t5))
            keyboard.press_and_release('enter')
            sleep(0.01)
            pag.write(result.text)
            keyboard.press_and_release('enter')
            t6 = "[[magenta]]Nachricht wurde gesendet.\n \n \n"
            print(colorText(t6))



if Fl == 'n': 
    quit()
