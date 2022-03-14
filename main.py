import sounddevice as sd
import numpy as np
from playsound import playsound

sample_duration = 10  # seconds
audio_path = 'C:/sh.mp3'  # path to the
sum_of_too_high = 0


def print_sound(in_data, out_data, frames, time, status):
    volume_norm = np.linalg.norm(in_data) * 10
    print(int(volume_norm))
    if int(volume_norm) > 8:
        print("too high")
        playsound(audio_path)
        # global sum_of_too_high
        # sum_of_too_high += 1


with sd.Stream(callback=print_sound):
    sd.sleep(sample_duration * 1000)
    # print("", sum_of_too_high)
