import os
import librosa
import librosa.display
import numpy as np 
import matplotlib.pyplot as plt

sesiones = ["Session1","Session2","Session3","Session4","Session5"]

path = "IEMOCAP_full_release/" + sesiones[0] + "/sentences/wav"
dirs = os.listdir( path )


listadeaudios = []

for d in dirs:
    for di in os.listdir( path + "/" + d ) :
        listadeaudios.append( path + "/" + d + "/" +di )

print( len(listadeaudios) )

print( listadeaudios[0]   )
y, sr = librosa.load( listadeaudios[0] )


## Borramos Silencio AL inicio y Final 
y,index = librosa.effects.trim(y)
print(len(y))
print(index)



# plt.figure(figsize=(14, 5))
librosa.display.waveplot(y, sr=sr)


X = librosa.stft(y,n_fft=512)
# print(X)
Xdb = librosa.amplitude_to_db(abs(X))
# plt.figure(figsize=(14, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='mel')
# plt.show()


import cv2 
data = np.array(Xdb)
print ( data.shape )
data = cv2.resize(data,(64,64))
plt.figure(figsize=(10,10))
plt.imshow(data)
plt.show()