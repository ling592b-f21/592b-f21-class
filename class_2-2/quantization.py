import scipy.io.wavfile as wavfile
import numpy as np
import glob

#Parameters:
#   audio_file_name: the name of a .wav file
#Returns:
# 1)Sampling rate of file
# 2)Data type of amplitude values(tells us the bit depth- 16 bit integer vs 32 bit integer)
# 3)Minimum amplitude value
# 4)Maximum amplitude value
def get_quantization_stats(audio_file_name):
    fs, sine = wavfile.read(audio_file_name)
    return fs, sine.dtype, min(sine), max(sine)

#Get all the file names in 'audio' that have the .wav extension
wavfile_names = [f for f in glob.glob("audio/*.wav")]
#Compute and print the sampling rate, bit depth, and amplitude range for each file
for file_name in wavfile_names:
    print(file_name,get_quantization_stats(file_name))

#Sandbox- What's the difference between 2 adjancent values in the sine wave? Can that tell us anything about the step size?
fs, sine0_5 = wavfile.read(wavfile_names[0])
start_sample = 4096
print("Some 0.5 Amplitude values, 16bit: ", sine0_5[start_sample:start_sample+5])
differences0_5 = np.diff(np.array(sine0_5[start_sample:start_sample+5]))
print("The differences between them:", str(differences0_5))

#Repeat for wave with an amplitude of "1"
fs, sine1 = wavfile.read(wavfile_names[1])
print("Some 1 Amplitude values, 16bit: ", sine1[start_sample:start_sample+5])
differences1 = np.diff(np.array(sine1[start_sample:start_sample+5]))
print("The differences between them:", str(differences1))
