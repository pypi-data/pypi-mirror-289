get_ipython().system('pip install sounddevice')
get_ipython().system('pip install scipy')
get_ipython().system('pip install wavio')
get_ipython().system('pip install SpeechRecognition')
get_ipython().system('pip install simpleaudio')
get_ipython().system('pip install JarvisVoice==0.0.2')
from JarvisVoice import voice
import simpleaudio as sa
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import speech_recognition as sr
import time
import tkinter as Tk
from tkinter import *
from tkinter import Button
text = "Пусто"
bt_st = False
st_st = True
def pusk():
    global text
    text = "пусто"
    slushayu_name = 'slushayu.wav'
    wave_obj = sa.WaveObject.from_wave_file(slushayu_name)
    play = wave_obj.play()
    play.wait_done()
    play.stop()
    recording = sd.rec(int(5 * 44100), samplerate=44100, channels=2)
    sd.wait(2)
    write("recording.wav", 44100, recording)
    wv.write("recording.wav", recording, 44100, sampwidth=2)
    r = sr.Recognizer()
    with sr.AudioFile("recording.wav") as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio, language="ru-RU")
        print("Text: "+text)
    except Exception as e:
        print("Exception: "+str(e))
    hour = int(datetime.datetime.now().hour)
    voice()
def potok():
    global text
    while text != "пока" and st_st == True:
        recording = sd.rec(int(5 * 44100), samplerate=44100, channels=2)
        sd.wait(0.7)
        write("recording.wav", 44100, recording)
        wv.write("recording.wav", recording, 44100, sampwidth=2)
        r = sr.Recognizer()
        with sr.AudioFile("recording.wav") as source:
            audio = r.record(source)
        try:
            text = r.recognize_google(audio, language="ru-RU")
            print("Text: "+text)
        except Exception as e:
            print("Exception: "+str(e))
        if text == "Джарвис" or text == "Джар" or text == "джар":
            pusk()
            time.sleep(0.7)
            potok()
        elif text == "пока":
            continue
        else:
            potok()
