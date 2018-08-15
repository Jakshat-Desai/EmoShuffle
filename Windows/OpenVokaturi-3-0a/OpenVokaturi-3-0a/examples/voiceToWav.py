import pyaudio
import wave
import os
 
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"
ip="192.168.56.101"#input("Enter the needed IP")

audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print("recording...")
frames = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print("finished recording")
 
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

os.system("python OpenVokaWavMean-win64.py file.wav")
os.system("pscp -pw redhat current_emotions.txt root@"+ip+":/root/Desktop/music/")
os.system("ssh -t -l root "+ip+" docker run -dit -v /root/Desktop/music/:/music --device /dev/snd -p 1111:3333 emofinal:v5")
os.system("start \"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe\" http://"+ip+":1111")