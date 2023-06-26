#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import pyaudio
import wave
import os

def sestanıma():
    model_path = "/home/ahmet/catkin_ws/src/elrf/robot_interface_control/models/vosk-model-small-en-us-0.15"
    sample_rate = 16000
    chunk_size = 1024
        
    model = Model(model_path)
    rec = KaldiRecognizer(model, sample_rate)
        
    audio = pyaudio.PyAudio()
    stream =audio.open(format=pyaudio.paInt16,
                                      channels=1,
                                      rate=sample_rate,
                                      input=True,
                                      frames_per_buffer=chunk_size)
        
    
        
    while True:
       
            data =stream.read(chunk_size, exception_on_overflow=False)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result =rec.Result()
                return result[14:-3]
                



