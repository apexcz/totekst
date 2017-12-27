#!/usr/bin/env python3

import pydub
import speech_recognition as sr

# load audio file from same directory
from os import path


AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), 'obama.mp3')
NEW_FILE = 'converted.wav'
temp_files = []

sound = pydub.AudioSegment.from_mp3(AUDIO_FILE)

print(len(sound))
chunk_size = 2048 #instead use 2048 it is advisable to use powers of 2 such as 1024 or 2048
fragments = [sound[i:i+chunk_size] for i in range(0, len(sound), chunk_size)]

for i,fragment in enumerate(fragments):
    temp_file = str(i) + NEW_FILE
    temp_files.append(temp_file)
    fragment.export(temp_file, format="wav")


print(len(fragments))
result = ''
for partial_file in temp_files:
    # use audio file as input
    r = sr.Recognizer()
    with sr.AudioFile(partial_file) as source:
        audio = r.record(source)  # read the entire audio file
    try:
        result += r.recognize_google(audio) + ' '
        #print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

print("Final result is %s" % result)