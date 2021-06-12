import os
import time
import difflib
import keyboard
import pyautogui
import speech_recognition as stt

r = stt.Recognizer()

while True: 
    with stt.Microphone() as source:
        recording = r.listen(source)    
        try:
            text = r.recognize_google(recording)
            print(text)

        except Exception as e:
            print('Could not process audio.', e)

            if text.startswith('send'):
                keyboard.write(text.split('send ')[1])
                keyboard.press_and_release('enter')

            else:
                for image in os.listdir('media/'):
                    if difflib.SequenceMatcher(image, text).ratio() > .85:
                        print('Detected', image)
                        pyautogui.click(pyautogui.locateCenterOnScreen('media/' + image + '.png'))
                        break

