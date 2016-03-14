import pyaudio
import wave
import numpy as np
import cv2
import math

 
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 1
WAVE_OUTPUT_FILENAME = "file.wav"
 
audio = pyaudio.PyAudio()


 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print "recording..."

 

# decode the recorded frame
def decode_data(data):
	return np.fromstring(data, 'Float32')

def transforme_data(data):
	try:
		return 20*math.log10(round(data))
	except:
		return 0

frames_decoded = []
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
    spect = decode_data(data)
    restru = np.array(map(transforme_data,spect))

    frames_decoded.append(restru)
 
    print(max(restru))
    print(min(restru))
    print(i)
print "finished recording"
 
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()







#cv2.destroyAllWindows()




#frames_decoded = np.array(map(decode_data, frames))

print(np.array(frames_decoded).shape)

frames_decoded = np.array(frames_decoded)




photo = frames_decoded[32].reshape(32,32)
cv2.imshow('image',photo)
cv2.waitKey(0)
cv2.destroyAllWindows()



# print(frames_decoded.shape)



# waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# waveFile.setnchannels(CHANNELS)
# waveFile.setsampwidth(audio.get_sample_size(FORMAT))
# waveFile.setframerate(RATE)
# waveFile.writeframes(b''.join(frames))
# waveFile.close()

# print(frames_decoded[5])
# print(min(frames_decoded[5]))
# print(max(frames_decoded[5]))

