
import math
import numpy as np
import simpleaudio as sa
import random

def generate_tone(freq, duration=0.3, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(freq * t * 2 * math.pi)
    # Normalize to 16-bit range
    audio = wave * (2**15 - 1) / np.max(np.abs(wave))
    return audio.astype(np.int16)

def play_scale():
    base_freq = random.choice([220, 261, 329, 392])  # Random base note (A3, C4, E4, G4)
    for i in range(8):
        freq = base_freq * (2 ** (i/12))  # Semi-tone steps
        duration = random.choice([0.2, 0.3, 0.4])
        audio = generate_tone(freq, duration)
        sa.play_buffer(audio, 1, 2, 44100).wait_done()

def generative_jam():
    print("Cooking some glitchy tunes... press Ctrl+C to stop.")
    try:
        while True:
            play_scale()
    except KeyboardInterrupt:
        print("\nJam session ended.")

if __name__ == "__main__":
    generative_jam()