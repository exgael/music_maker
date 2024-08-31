import numpy as np
import simpleaudio as sa
from mario_angel_synth import MarioAngelSynth
from violin_instrument import Violin
from harp_instrument import Harp
from kalimba_instrument import Kalimba

# Initialize instruments
sample_rate = 44100
synth = MarioAngelSynth(sample_rate=sample_rate)
violin = Violin(sample_rate=sample_rate)
harp = Harp(sample_rate=sample_rate)
kalimba = Kalimba(sample_rate=sample_rate)

# Define a simple chord progression
chords = [
    ('C', [261.63, 329.63, 392.00]),  # C major
    ('G', [392.00, 493.88, 587.33]),  # G major
    ('Am', [220.00, 261.63, 329.63]),  # A minor
    ('F', [349.23, 440.00, 523.25]),  # F major
]

def create_synth_layer(duration):
    samples = int(duration * sample_rate)
    layer = np.zeros(samples)
    chunk_samples = samples // 4
    for i, (_, frequencies) in enumerate(chords):
        start = i * chunk_samples
        end = (i + 1) * chunk_samples
        layer[start:end] = synth.generate_chord(frequencies, duration/4, 0.2)
    return layer

def create_violin_layer(duration):
    samples = int(duration * sample_rate)
    layer = np.zeros(samples)
    melody = [440.00, 392.00, 349.23, 329.63, 349.23, 392.00, 440.00, 493.88]
    chunk_samples = samples // 8
    for i, note in enumerate(melody):
        start = i * chunk_samples
        end = (i + 1) * chunk_samples
        layer[start:end] = violin.generate_wave(note, duration/8, 0.3)
    return layer

def create_harp_layer(duration):
    samples = int(duration * sample_rate)
    layer = np.zeros(samples)
    chunk_samples = samples // 4
    for i, (_, frequencies) in enumerate(chords):
        start = i * chunk_samples
        end = (i + 1) * chunk_samples
        arpeggio = harp.generate_phrase(frequencies, [duration/12]*3, [0.25]*3)
        layer[start:end] = np.resize(arpeggio, chunk_samples)
    return layer

def create_kalimba_layer(duration):
    samples = int(duration * sample_rate)
    layer = np.zeros(samples)
    ostinato = [261.63, 329.63, 392.00, 329.63] * 2
    chunk_samples = samples // 8
    for i, note in enumerate(ostinato):
        start = i * chunk_samples
        end = (i + 1) * chunk_samples
        layer[start:end] = kalimba.generate_wave(note, duration/8, 0.2)
    return layer

# Create the composition
duration = 16  # 16 seconds total
composition = np.zeros(sample_rate * duration)

# Add layers
composition += create_synth_layer(duration)
composition[sample_rate*4:sample_rate*12] += create_violin_layer(8)  # Violin comes in after 4 seconds
composition += create_harp_layer(duration)
composition[sample_rate*2:sample_rate*14] += create_kalimba_layer(12)  # Kalimba plays for 12 seconds in the middle

# Normalize and play the composition
composition = composition / np.max(np.abs(composition))
composition = (composition * 32767).astype(np.int16)

play_obj = sa.play_buffer(composition, 1, 2, sample_rate)
play_obj.wait_done()