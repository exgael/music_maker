from mario_angel_synth import MarioAngelSynth
import numpy as np

# Create our instrument
synth = MarioAngelSynth()

# Define the God chords progression (in C major)
god_chords = [
    ('C', [261.63, 329.63, 392.00]),  # C major
    ('G', [392.00, 493.88, 587.33]),  # G major
    ('Am', [220.00, 261.63, 329.63]), # A minor
    ('Em', [329.63, 392.00, 493.88]), # E minor
    ('F', [349.23, 440.00, 523.25]),  # F major
    ('C', [261.63, 329.63, 392.00]),  # C major
    ('F', [349.23, 440.00, 523.25]),  # F major
    ('G', [392.00, 493.88, 587.33])   # G major
]

# Function to create a full progression
def create_progression(chord_duration=2.0, arpeggio_duration=1.0):
    progression = np.array([])
    for _, frequencies in god_chords:
        chord = synth.generate_chord(frequencies, chord_duration, 0.3)
        arpeggio = synth.generate_arpeggio(frequencies, arpeggio_duration, 0.2)
        progression = np.concatenate([progression, chord, arpeggio])
    return progression

# Create our composition
composition = np.array([])

# Intro: Simple arpeggios
for _, frequencies in god_chords:
    composition = np.concatenate([composition, synth.generate_arpeggio(frequencies, 1.0, 0.2)])

# Main theme: Full progression, repeated twice
for _ in range(2):
    composition = np.concatenate([composition, create_progression()])

# Bridge: Slower chords
for _, frequencies in god_chords:
    composition = np.concatenate([composition, synth.generate_chord(frequencies, 3.0, 0.25)])

# Final progression: Mixture of chords and arpeggios
composition = np.concatenate([composition, create_progression(1.5, 0.75)])

# Outro: Fading arpeggios
outro = np.array([])
for _, frequencies in god_chords:
    outro = np.concatenate([outro, synth.generate_arpeggio(frequencies, 1.0, 0.2)])
fade_out = np.linspace(1, 0, len(outro))
outro *= fade_out
composition = np.concatenate([composition, outro])

# Normalize and play the composition
composition = composition / np.max(np.abs(composition))
composition = (composition * 32767).astype(np.int16)

import simpleaudio as sa
play_obj = sa.play_buffer(composition, 1, 2, synth.sample_rate)
play_obj.wait_done()